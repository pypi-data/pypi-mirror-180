from colorama import Fore, Back, Style
from rich.console import Console

from .markdown import SmartMarkdown

rich_console = Console(color_system="truecolor", legacy_windows=False)

TrueColors = {

  "bg": {
    "blue": "\u001b[48;5;24m",
    "turquoise": "\u001b[48;5;29m",
    "red": "\u001b[48;5;88m"
  },

}

def render_markdown_to_html(text, title=''):
  svg = SmartMarkdown(f" \n{text}\n ", code_theme="monokai").to_svg(title=title)

  # The laziest hack ever
  svg = svg.replace('<g transform="translate(26,22)"', '<g transform="translate(-100,-100)"');
  svg = svg.replace('<rect fill="#292929"', '<rect fill="#000d1a"');

  return f"<div style=\"resize: horizontal; overflow: hidden; width: 1000px; height: auto;\">{svg}</div>"

def print_markdown(text):
  rich_console.print(SmartMarkdown(text))

def print_banner(text, bg_color, prefix=""):
  color_code = TrueColors["bg"][bg_color]
  formatted_text = f"\u001b[48;5;236m\u001b[38;5;249m{prefix}{Fore.WHITE}\x1b[1m{color_code}{text}"

  print(f"{formatted_text}\u001b[K{Style.RESET_ALL}")

def print_thread_saved(thread_id):
  print(f"#\x1b[1m{thread_id}{Style.RESET_ALL} saved")
