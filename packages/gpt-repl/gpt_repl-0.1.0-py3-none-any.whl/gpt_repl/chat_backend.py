from pychatgpt import Chat as PyChatGPT
from pychatgpt.classes import chat as ChatHandler
from pychatgpt.classes import openai as OpenAI

from colorama import Fore

class ChatBackend:

  def __init__(self, email, password, conversation_id=None, previous_conversation_id=None):
    self.email = email
    self.password = password

    self.conversation_id = conversation_id if conversation_id != "" else None
    self.previous_conversation_id = previous_conversation_id if previous_conversation_id != "" else None

    self.ChatGPT = PyChatGPT(
      self.email,
      self.password,
      conversation_id=self.conversation_id,
      previous_convo_id=self.previous_conversation_id
    )
    self.access_token = self.auth()


  def auth(self):
    return OpenAI.get_access_token()

  def ask(self, text):
    answer, previous_convo, convo_id = ChatHandler.ask(
      auth_token=self.access_token,
      prompt=text,
      conversation_id=self.conversation_id,
      previous_convo_id=self.previous_conversation_id,
      proxies=''
    )

    if answer == "400" or answer == "401":
        print(f"{Fore.RED}>> Failed to get a response from the API.")
        return None

    self.conversation_id = convo_id
    self.previous_conversation_id = previous_convo

    return answer.strip()
