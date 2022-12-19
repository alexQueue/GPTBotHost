# from dotenv import load_dotenv

from gptbots import davinci_client
import os
import traceback
import nextcord

# from nextcord import app_commands
from nextcord.ext import commands
# import logging

print("Starting up.")

# Send messages
async def send_message(message, user_message, is_private):
    try:    
        # await message.channel.trigger_typing()
        # response = davinci_client.handle_response(user_message)
        async with message.channel.typing():
            response = davinci_client.handle_response(user_message)

        if is_private:
            reply = await message.author.send(response)
        else:
            reply = await message.channel.send(response)


# except Exception as e:
#     print(traceback.format_exc())


intents = nextcord.Intents(messages=True)

def test_message():
    print("Firing off test message:")
    # msg = gpt_chat_client.handle_response("Are you working?")
    msg = davinci_client.handle_response("You're alive now. Greet the world.")
    
    print(msg)

test_message()

def run_discord_bot():
    print("Setting up bot.")
    # Change your token here
    # load_dotenv()
    TOKEN = os.getenv("DISCORD_BOT_TOKEN")
    client = nextcord.Client(intents=intents)
    # tree = app_commands.CommandTree(client)

    # @tree.command(name="chatgpt", description="Use ChatGPT")
    # async def chat(interaction):
    #     await interaction.response.send_message("Hello!")

    async def on_ready():
        # await tree.sync()
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

    client.run(TOKEN)

run_discord_bot()