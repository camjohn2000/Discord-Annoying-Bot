import discord
import os
import json
import requests

client = discord.Client()

def get_joke():
  pass

#console logging that bot is logged in and online
@client.event
async def on_ready():
  print("Logged in as {0.user}".format(client))


@client.event
async def on_message(msg):
  
  #ignores it's own messages
  if msg.author == client.user:
    return
  
  #bot replies when it reads command in text channel
  if msg.content.startswith("%hey bot"):
    await msg.channel.send("HIIIIIIII")

#token defined privately
client.run(os.environ['TOKEN'])


