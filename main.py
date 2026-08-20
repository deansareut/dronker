import logging
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user} is online.")


@bot.event
async def on_member_join(member):
    await member.send(f"{member.name} has joined the server.")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "hi dronker" in message.content.lower():
        await message.channel.send("WHAT'S UP YO!")

    await bot.process_commands(message)


@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}!")


bot.run(token, log_handler=handler, log_level=logging.DEBUG)
