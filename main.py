import discord
import os
import random
from keep_alive import keep_alive
from discord.ext import commands


client = commands.Bot(command_prefix="/")


magic8= [' it is likely', 'no shot bucko', 'lol', 'probably', '...', 'im a bot, how am i supposed to know', 'sure, whatever', 'why do *you* want to know?', 'TW/// NO', 'OFC! not', 'yeah sure', 'probably', 'i give it a 90% chance', 'my creator didnt code a response for this dumb fucking question', 'what a waste of a question', 'if you want', 'ok', 'ask Chloe', 'i just want to wear thigh highs' ]

@client.event
async def on_ready():
    print("IM TURNED ON")

@client.command()
async def maya(ctx):
  await ctx.send('my dumbfuck creator')

@client.command()
async def m8b(ctx):
  lucky_num = random.randint(0,len(magic8) - 1)
  await ctx.send(magic8[lucky_num])


@client.command()
async def gwenvara(ctx):
  await ctx.send('the most based mod!')
@client.command()
async def true(ctx):
  await ctx.send('so true!')
keep_alive()
client.run(os.getenv('TOKEN'))