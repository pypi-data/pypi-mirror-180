from jinja2 import Environment, FileSystemLoader, select_autoescape, Template
from pathlib import Path
from os.path import join
from shutil import copytree
import sass
from http.server import HTTPServer, SimpleHTTPRequestHandler
from .logger import get_logger
from .filters.to_markdown import to_markdown
from dataclasses import dataclass
import tomllib
from pathlib import Path


@dataclass
class Page:
    base_name: str
    rel_path: str
    template: Template
    variables: dict


class SiteConfig:
    """Creates a configuration dictionary from `site.toml`"""

    def __init__(self, project_root: Path = Path.cwd()) -> None:
        self.logger = get_logger(__name__)
        self.project_root = Path(project_root)
        self.config_filename_defaults = ["site"]
        self.config_filename = join(self.project_root, "site.toml")
        self.default_section = "site"
        self.config = {
            "SITE_NAME": "My Site",
            "SITE_URL": "/",
            "SASS_ENABLED": True,
            "MARKDOWN_EXTENSION": ".md",
            "MARKDOWN_TEMPLATE": "markdown.j2",
            "IGNORE_FILES": [],
            "ENCODING": "utf-8",
            "SASS_DIR": "sass",
            "STATIC_DIR": "static",
            "STATIC_OUTPUT_DIR": "static",
            "OUTPUT_DIR": "output",
            "CSS_OUTPUT_DIR": "css",
            "TEMPLATES_DIR": "templates",
            "CONTENT_DIR": "content",
            "IGNORE_DIRS": [".git", "venv"],
            "SITEMAP_STRUCTURE": "directory_structure"
        }

    def read_config_file(self) -> dict:
        """Reads a config file from `site.toml`.

        :return: A dictionary of config variables
        """
        with open(self.config_filename, "rb") as f:
            config = tomllib.load(f)
            self.config.update(config["site"])
        self._absolute_paths()
        return self.config

    def _absolute_paths(self) -> None:
        """Ensures input/output directories are absolute paths"""
        project_dirs = [
            "CONTENT_DIR",
            "TEMPLATES_DIR",
            "SASS_DIR",
            "STATIC_DIR",
            "OUTPUT_DIR",
        ]
        for key in project_dirs:
            self.config[key] = (self.project_root / self.config.get(key)).absolute()
        full_ignore_dirs = []
        for path in self.config["IGNORE_DIRS"]:
            p = Path(path)
            if not p.is_absolute():
                p = p.absolute()
            full_ignore_dirs.append(p)
        self.config["IGNORE_DIRS"] = full_ignore_dirs
        sod = Path(self.config["STATIC_OUTPUT_DIR"])
        if not sod.is_absolute():
            self.config["STATIC_OUTPUT_DIR"] = self.config["OUTPUT_DIR"] / sod
        cod = Path(self.config["CSS_OUTPUT_DIR"])
        if not cod.is_absolute():
            self.config["CSS_OUTPUT_DIR"] = (
                self.config["STATIC_OUTPUT_DIR"] / self.config["CSS_OUTPUT_DIR"]
            )


class SiteCreator:
    """Renders the specified directory into the output directory."""

    def __init__(self, project_root: Path) -> None:
        self.logger = get_logger(__name__)
        self.project_root = project_root
        self.config = SiteConfig(project_root).read_config_file()
        self.logger.debug(self.config)
        self.config["OUTPUT_DIR"].mkdir(exist_ok=True)
        self.render_queue = []
        self.config["SITEMAP"] = {"items": []}
        self.env = Environment(
            loader=FileSystemLoader(
                [
                    self.config["TEMPLATES_DIR"],
                    self.config["CONTENT_DIR"],
                ]
            ),
            autoescape=select_autoescape(["html", "xml"]),
        )
        self.env.filters.update({"to_markdown": to_markdown})

    def _get_markdown_content(self, filepath: Path) -> str:
        """Reads a file

        Args:
            filepath (Path): The file to read

        Returns:
            str: The file contents
        """
        with open(filepath, "r", encoding=self.config["ENCODING"]) as m:
            return m.read()

    def _add_sitemap_parent(self, rel_path: str, base_name: str) -> tuple:
        """Adds an item to the sitemap using the `parent_folder` strategy

        Args:
            rel_path (str): PosixPath-like string
            base_name (str): A filename without extension

        Returns:
            tuple: The title and relative url of the page
        """
        rel_path = Path(rel_path)
        url = Path(self.config["SITE_URL"]) / rel_path / base_name
        menu_item = (base_name.title(), f"{url.as_posix()}.html")
        parent = self.config["SITEMAP"]["items"]
        if rel_path not in [Path("."), Path("/")]:
            if self.config["SITEMAP"].get(rel_path.stem):
                parent = self.config["SITEMAP"][rel_path.stem]["items"]
            else:
                self.config["SITEMAP"][rel_path.stem] = {"items": []}
                parent = self.config["SITEMAP"][rel_path.stem]["items"]
        parent.append(menu_item)
        return menu_item

    def _add_sitemap_directory(self, rel_path: Path, base_name: str) -> tuple:
        """Adds an item to the sitemap

        Args:
            rel_path (str): PosixPath-like string
            base_name (str): A filename without extension

        Returns:
            tuple: The title and relative url of the page
        """
        rel_path = Path(rel_path)
        parts = rel_path.parts
        self.logger.debug(parts)
        parent = self.config["SITEMAP"]
        url = Path(self.config["SITE_URL"]) / rel_path / base_name
        menu_item = (base_name.title(), f"{url.as_posix()}.html")
        for part in parts:
            if part not in [".", "/"]:
                if not isinstance(parent.get(part), dict):
                    parent[part] = {"items": []}
                parent = parent[part]
        parent["items"].append(menu_item)
        self.logger.debug(self.config)
        return menu_item

    def _add_sitemap_item(self, rel_path: str, base_name: str) -> tuple:
        """Adds an item to the sitemap

        Args:
            rel_path (str): PosixPath-like string
            base_name (str): A filename without extension

        Returns:
            tuple: The title and relative url of the page
        """
        if self.config["SITEMAP_STRUCTURE"] == "parent_directory":
            item = self._add_sitemap_parent(rel_path, base_name)
        else:
            item = self._add_sitemap_directory(rel_path, base_name)
        return item

    def discover(self) -> list:
        """Iterates over the content directory, discovering pages to render

        Returns:
            list: List of pages to render
        """
        content_dir = self.config["CONTENT_DIR"]
        for f in content_dir.rglob("*"):
            if f.is_file():
                ignore = False
                for dir in self.config["IGNORE_DIRS"]:
                    if f.is_relative_to(dir):
                        ignore = True
                if f.name in self.config["IGNORE_FILES"]:
                    ignore = True
                if ignore:
                    ignore = False
                    continue
                rel_path = f.parent.relative_to(content_dir).as_posix()
                base_name = f.stem
                self._add_sitemap_item(rel_path, base_name)
                template_path = str(f.name)
                page_vars = self.config
                if f.suffix == self.config["MARKDOWN_EXTENSION"]:
                    template_path = self.config["MARKDOWN_TEMPLATE"]
                    page_vars["md_content"] = self._get_markdown_content(f)
                template = self.env.get_template(template_path)
                self.render_queue.append(
                    Page(
                        base_name=base_name,
                        rel_path=rel_path,
                        template=template,
                        variables=page_vars,
                    )
                )
        return self.render_queue

    def copy_static(self) -> None:
        """Copies the static site data from STATIC_DIR to the output
        directory.

        Returns: The static output directory
        """
        self.logger.info("Copying static content...")
        copytree(
            self.config["STATIC_DIR"],
            self.config["STATIC_OUTPUT_DIR"],
            dirs_exist_ok=True,
        )
        return self.config["STATIC_OUTPUT_DIR"]

    def create_page(self, page: Page) -> None:
        """Renders the render_queue queued by discover.

        :param page: Page
        :return:
        """
        output_dir = self.config["OUTPUT_DIR"] / page.rel_path
        Path.mkdir(output_dir, parents=True, exist_ok=True)
        output_file = output_dir / f"{page.base_name}.html"
        self.logger.debug(f"Writing {output_file} using {page.template}")
        with output_file.open(mode="w+") as o:
            o.write(page.template.render(page.variables))

    def compile_sass(self) -> None:
        """Compiles SASS to CSS in the OUTPUT_DIR.

        :return: None
        """
        self.logger.info(f"Compiling CSS...")
        sass.compile(
            dirname=(self.config["SASS_DIR"], self.config["CSS_OUTPUT_DIR"]),
            output_style="compressed",
        )

    def create_site(self) -> None:
        """Discovers and renders pages, copies static data, and compiles CSS.

        :return: None
        """
        self.discover()
        self.copy_static()
        if self.config["SASS_ENABLED"]:
            self.compile_sass()
        self.logger.info(f"Rendering pages...")
        for page in self.render_queue:
            self.logger.debug(f"Adding page: {page.base_name}")
            self.create_page(page)

    def start_dev_server(self) -> None:
        """Starts a development server.
        This server should not be run in production.

        :return: None
        """
        dev_port = 8088
        self.logger.info(f"Starting server on http://localhost:{dev_port}")
        server_address = ("", dev_port)
        httpd = HTTPServer(server_address, DevHandler)
        httpd.serve_forever()


class DevHandler(SimpleHTTPRequestHandler):
    """Class to handle simple http dev server."""

    def __init__(self, *args, **kwargs) -> None:
        self.logger = get_logger(__name__)
        self.config = SiteConfig().read_config_file()
        super().__init__(*args, directory=self.config["OUTPUT_DIR"], **kwargs)
