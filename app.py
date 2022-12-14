from gptbots import davinci_client
import os
import traceback
import nextcord
from nextcord.ext import commands

# from discord import app_commands
import logging


async def send_message(message, content, is_private):
    if is_private:
        reply = await message.author.send(content)
    else:
        reply = await message.channel.send(content)
    return reply

# Send messages
async def send_message(message, user_message, is_private):
    try:
        think = False
        if think:
            thinking_message = "Thinking. Give me a moment..."
            reply = await send_message(message, thinking_message, is_private)
            response = davinci_client.handle_response(user_message)
            await reply.edit(content=response)
        else:
            # await message.channel.trigger_typing()
            async with message.channel.typing():
                response = davinci_client.handle_response(user_message)
            
            await send_message(message, response, is_private)


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


    except Exception as e:
        print(traceback.format_exc())


intents = nextcord.Intents(messages=True)


def test_message():
    # msg = gpt_chat_client.handle_response("Are you working?")
    msg = davinci_client.handle_response("Are you alive?")
    
    print(msg)


def run_discord_bot():
    # Change your token here
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


test_message()

run_discord_bot()