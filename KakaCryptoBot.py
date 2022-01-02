#MODULE IMPORTS
import random
import json
import discord
import util

#INITIALIZATION
client = discord.Client()
jsonreader = open('config.json')
config = json.load(jsonreader)

#EVENT ACTIONS
@client.event
async def on_ready():
    print('ready to crunch some numbers! ', client)

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(message.author, message.content)

    if user_message.lower() == '!random':
        response = random.random()
        await message.channel.send(response)
        return

#RUN!!!!!!
client.run(util.__DISCORDKEY__)