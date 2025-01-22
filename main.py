import discord
import os
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    await bot.change_presence(activity=discord.Playing(name='Playing-name', name='A99'))

bot.run('MTMxODg2NzkxNjUzNTM2NTY0Mw.GhJ7n3.SoUsEv2ZZrZgcUAY9YVx7wuPTPjfeO63G8cTeg')
