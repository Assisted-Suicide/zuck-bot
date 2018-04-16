import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client ()
client = commands.Bot (command_prefix = "!")

@client.event
async def on_ready ():
    print ("Zucc is connected to Discord")

@client.event
async def on_message (message):
    if message.content.upper().startswith ('!PING'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID) )


client.run ("NDM1NDg0MDc4Mjc2NDc2OTQ2.DbZrzw.ynhbnB_WK0eI2Jvbq2wUpGokGsA")
