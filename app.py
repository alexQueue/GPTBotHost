# from flask import Flask
# from gptbots import bot
import discord
from gptbots import davinci_client
import os
import traceback
from discord.ext import commands
from discord import app_commands
import logging

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'


# if __name__ == '__main__':
#     # single test message:
# bot.test_message()
# bot.run_discord_bot()



# Send messages
async def send_message(message, user_message, is_private):
    try:
        thinking_message = "Thinking. Give me a moment..."
        if is_private:
            reply = await message.author.send(thinking_message)
        else:
            reply = await message.channel.send(thinking_message)

        # streamed
        # response = gpt_chat_client.streamed_response(user_message)
        # content = ""
        # for res in response:
        #     # print(res['message'])
        #     content = res['message'] + '...'
        #     await reply.edit(content=content)
        # print("finished")
        # content = res['message'] + " ■"
        # await reply.edit(content=content)

        # not streamed
        response = davinci_client.handle_response(user_message)
        await reply.edit(content=response)

    except Exception as e:
        print(traceback.format_exc())


intents = discord.Intents(messages=True)


def test_message():
    # msg = gpt_chat_client.handle_response("Are you working?")
    msg = davinci_client.handle_response("Are you alive?")
    
    print(msg)


# def run_discord_bot():
# Change your token here
TOKEN = os.getenv("DISCORD_BOT_TOKEN")
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name="chatgpt", description="Use ChatGPT")
async def chat(interaction):
    await interaction.response.send_message("Hello!")

async def on_ready():
    await tree.sync()
    print(f'{client.user} is now running!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)
    if len(user_message) == 0:
        return

    print(f"{username} said: '{user_message}' ({channel})")

    if user_message[0] == '?':
        user_message = user_message[1:]
        await send_message(message, user_message, is_private=True)
    else:
        await send_message(message, user_message, is_private=False)

test_message()

client.run(TOKEN)


print("Got here")

####
import socket

# Create a socket object
s = socket.socket()

# Bind the socket to the IP address and port
s.bind(('0.0.0.0', 1234))

# Start listening for incoming connections
s.listen()

# Accept a connection
conn, addr = s.accept()

# Print the client address
print("Connection from: ", addr)

# import socket

# HOST = '0.0.0.0'  # Standard loopback interface address (localhost)

# PORT = 5000 # Don't know which pot

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen()

#     conn, addr = s.accept()

#     with conn:

#         print('Connected by', addr)
