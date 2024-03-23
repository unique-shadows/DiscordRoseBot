import discord
from os import environ

intents = discord.Intents.all()

client = discord.Client(
    intents=intents
)

@client.event
async def on_ready():
    print("Bot is running!")

@client.event
async def on_message(message: discord.Interaction):
    if message.author == client.user:
        return

    await message.channel.send('Hello!\nI am Rose bot')


if __name__ == "__main__":
    client.run(token = environ.get("token"))