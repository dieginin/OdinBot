import asyncio
import os

import discord
from discord.ext import commands

from config import DS_KEY

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())


@bot.event
async def on_ready() -> None:
    print(f"BOT {bot.user} connected to Discord!")
    print(f"CMD {len(await bot.tree.sync())} synced")


async def load() -> None:
    for folder in ["commands"]:
        for filename in os.listdir(f"./{folder}"):
            if filename.endswith(".py"):
                try:
                    await bot.load_extension(f"{folder}.{filename[:-3]}")
                except commands.ExtensionError as e:
                    print(f"Error loading extension {filename}: {str(e)}")


async def main() -> None:
    async with bot:
        await load()
        await bot.start(f"{DS_KEY}")


asyncio.run(main())
