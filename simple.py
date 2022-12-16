import os
from dotenv import load_dotenv
from nextcord.ext import commands

def main():
    client = commands.bot(command_prefix="?")

    load_dotenv()

    @client.event
    async def on_ready():
        print(f"{client.user.name} is ready")

    # load cogs
    client.run(os.getenv("DISCORD_BOT_TOKEN"))