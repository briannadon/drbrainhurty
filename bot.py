# bot.py
import os
import discord
from dotenv import load_dotenv
import random
from sentiment import get_sentiment_score
import re

intents = discord.Intents.default()
intents.message_content = True
load_dotenv()

client = discord.Client(intents=intents)
TOKEN = os.getenv('DISCORD_TOKEN')

rx_path = os.path.dirname(os.path.realpath(__file__)) + "/prescriptions.txt"
prescriptions = []
with open(rx_path) as f:
    for line in f:
        line = line.strip()
        prescriptions.append(line)

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

    if re.search(r'(W|w)hy.*\?',message.content):
        dice = random.randint(0,100)
        if dice < 5:
            await message.reply("special message")
        return

    try:
        dice = random.randint(0,100)
        if dice < 25:
            score = get_sentiment_score(message.content)
            if score <= -0.5:
                p = random.choice(prescriptions)
                await message.reply(p)
        return
    except:
        print("Error interpreting user's message.")
        return

client.run(TOKEN)
