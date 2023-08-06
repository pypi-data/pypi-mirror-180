from jinja2 import pass_eval_context
from jinja2.runtime import Context
from markdown import markdown


@pass_eval_context
def to_markdown(context: Context, text: str) -> str:
    """Transforms markdown to html.

    Args:
        context (Context): Jinja context from pass_eval_context decorator
        text (str): Markdown text to transform

    Returns:
        str: HTML rendered from markdown text
    """
    return markdown(text)
