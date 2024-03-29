import discord
import requests
import json 
from weather import *

token = "xx" #for private concern; will not show the real token here
api_key = "yy" # for private concern; will not show the real api_key here
command_prefix = "Weather."
client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{command_prefix}[location]"))

@client.event
async def on_message(message):
    if message.author != client.user and message.content.startswith(command_prefix):
        location = message.content.replace(command_prefix, "").lower()
        if len(location) >= 1:
            # Get Weather data here
            url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=imperial"
            try:
                data = json.loads(requests.get(url).content)
                data = parse_data(data)
                await message.channel.send(embed=weather_message(data, location))
            except KeyError:
                await message.channel.send(embed=error_message(location))
client.run(token)
