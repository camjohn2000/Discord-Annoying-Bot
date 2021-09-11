""""
First attempt at making a discord bot

Annoyingly sends non-stop dad jokes to test channel when someone types anything

Cameron Johnson
9-10-2021
""""

import discord
import os
import json
import requests
from discord.ext import commands, tasks

client = discord.Client()

@tasks.loop(seconds=2)
async def get_joke():
  #find the channel the user is in
  channel = client.get_channel('CHANNEL_ID_HERE')
 
 #dad joke from API icanhazdadjoke, sent every 2 seconds in text channel
  joke = requests.get('https://icanhazdadjoke.com', headers={"Accept": "text/plain"}).text
  await channel.send(joke)
  

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
  
  #stops the annoying loop
  elif msg.content.startswith("%chill"):
    get_joke.stop()
    await msg.channel.send("lmao ok")
  else:
    get_joke.start()

#token defined privately
client.run(os.environ['TOKEN'])


