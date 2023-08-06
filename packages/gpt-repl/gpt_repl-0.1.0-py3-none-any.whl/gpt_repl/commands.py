import os, re, pyperclip

from .printer import print_banner
from .publish import PublishGPT

class CommandsClass:

  def __init__(self):
    pass

  def exec(self, cli, text):
    text = text.strip()

    if text == '':
      pass

    elif text == '.clear' or text == '.cl':
      os.system('cls' if os.name == 'nt' else 'clear')

    elif text == '.editor' or text == '.e':
      print('')
      cli.session.layout.current_buffer.text = ""
      cli.session.layout.current_buffer.open_in_editor()

    elif text == '.exit':
      print('')
      raise KeyboardInterrupt

    elif text == '.copy' or text == '.cp':
      self.print_command_banner('.copy')
      code_block = self.extract_recent_code_block(cli.thread["history"])
      if code_block == None:
        print("No code block found")
      else:
        success = self.copy_to_clipboard(code_block)
        if success:
          print('Copied the first code block in the most recent response to the clipboard')
        else:
          print("Failed to copy to the clipboard")
      print('')

    elif text == '.publish' or text == '.pub':
      self.print_command_banner('.publish')
      publisher = PublishGPT(cli.thread)
      url = publisher.publish()
      print(url)
      print('')

    elif text == ('.name'):
      self.print_command_banner('.name')
      print(f"Thread name is \"{cli.thread_id}\"")
      print('')

    elif text.startswith('.rename'):
      self.print_command_banner('.rename')

      parts = text.split(' ')
      if len(parts) == 1:
        print(f"Thread name is \"{cli.thread_id}\"")
      elif len(parts) == 2:
        cli.thread_id = parts[1]
        print(f"Thread renamed to \"{cli.thread_id}\"")
      else:
        print("Invalid thread name")

      print('')

    elif text.startswith('.save'):
      cli.save_thread()

      self.print_command_banner('.save')
      print(f"Thread \"{cli.thread_id}\" saved")
      print('')

    elif text == '.help' or text == 'help':
      self.print_command_banner('.help')
      print("""
• .clear or .cl: Clears the terminal screen.
• .copy or .cp: Copies the first code block in the most recent response to the clipboard.
• .editor or .e: Opens the current buffer in the text editor specified by $EDITOR.
• .exit: Closes the REPL.
• .help or help: Prints a list of available commands and a brief description of each.
• .name: Prints the current thread name.
• .publish or .pub: Publishes the current thread online and prints the URL.
• .rename: Renames the current thread. The new name must be provided as an argument to this command, e.g. ".rename my_new_name"
• .save: Saves the current thread. Always happens on exit.
      """)

    else:
      return False

    return True

  def print_command_banner(self, name):
    print_banner(f'\n[ {name} ] =>', 'red')

  def extract_recent_code_block(self, history):
    responses = [ entry["text"] for entry in history if entry["type"] == 'gpt' ]
    if len(responses) == 0:
      return None
    last_response = responses[-1]

    # This regex is too naive but is easy
    code_block_pattern = re.compile(r"```[a-zA-Z0-9]*?\n(.*?)```", re.DOTALL)
    code_blocks = code_block_pattern.findall(last_response)

    if len(code_blocks) == 0:
      return None

    return code_blocks[0]

  def copy_to_clipboard(self, text):
    try:
      pyperclip.copy(text)
      return True
    except Exception as e:
      return False

Commands = CommandsClass()
