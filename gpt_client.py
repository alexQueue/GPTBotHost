from revChatGPT.revChatGPT import Chatbot
import os

SESSION_TOKEN = os.getenv("CHAT_GPT_SESSION_TOKEN")
# EMAIL = os.getenv("USER_EMAIL")
# PASSWORD = os.getenv("USER_PASSWORD")

# config = {
#     "email": "<YOUR_EMAIL>",
#     "password": "<YOUR_PASSWORD>"#,
#     #"session_token": "<SESSION_TOKEN>", # Deprecated. Use only if you encounter captcha with email/password
#     #"proxy": "<HTTP/HTTPS_PROXY>"
# }

config = {"Authorization": '<Auth>', "session_token": SESSION_TOKEN}

chatbot = Chatbot(config, conversation_id=None)
chatbot.refresh_session()


def streamed_response(message) -> str:
    return chatbot.get_chat_response(message, output="stream")


def handle_response(message) -> str:
    response = chatbot.get_chat_response(message, output="text")
    print(response)
    responseMessage = response["message"]
    return responseMessage

