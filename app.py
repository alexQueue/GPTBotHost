from flask import Flask
from gptbots import bot

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


# if __name__ == '__main__':
#     # single test message:
bot.test_message()
bot.run_discord_bot()

