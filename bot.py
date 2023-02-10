# bot.py
import os

import discord
from dotenv import load_dotenv
import random
from sentiment import get_sentiment_score

intents = discord.Intents.default()
intents.message_content = True

load_dotenv()
#TOKEN = os.getenv('DISCORD_TOKEN')
TOKEN = 'MTA3MzI4MzMyMzE3MTk4MzQ0MQ.G1Mkiz.mdT0tpLC22zO1cKaYH1AUvaRctjfdnXnb6XQew'


client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #msg_sent_score = get_sentiment_score(str(message.content))

    #if message.content.startswith('hello'):
    #    await message.channel.send('Hello!')

    try:
        dice = random.randint(0,100)
        if dice < 25:
            score = get_sentiment_score(message.content)
            if score < -0.4:
                await message.channel.send('venlafaxine, 225 mg 💊')
    except:
        print("Error interpreting user's message.")

client.run(TOKEN)
