import discord
import random

client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user: #Stops the bot from checking it's own messages
        return

    if message.content.startswith("Q joke"): #Checks for joke command
        jokes = ["Joke 1", "Joke 2", "Joke 3"]

        await message.channel.send(random.choice(jokes))
client.run("ODQzOTU5NjUyOTAzNTUxMDE3.YKLcrQ.qpQYhHyOBGwPvQezOC774miQNXU")