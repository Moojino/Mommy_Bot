import os
import discord
import time
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = commands.Bot(command_prefix = "!")
plist = ["ass", "asshole", "arse", "bastard", "bitch", "bullshit", "cunt", "crap", "dick", "dickhead", "dumbass", "fuck", "fucker", "fucking", "hell", "motherfucker", "motherfucking", "piss", "pissed", "prick", "pussy", "retard", "retarded", "shit", "shithead", "slut", "whore", "wanker", "damn", "damnit"]
quotes = [  "It’s been a bit… maybe go outside per chance.",
            "I’m pretty sure your diet has only been Doritos and Mountain Dew… I'll make you something healthy.",
            "For someone who's so thirsty, you haven't drank a lot of water.",
            "When’s the last time you saw the sun… you’re looking a little pale. Go outside and get some Vitamin D.",
            "I swear you’re addicted to that darn screen. Take a break.",
            "It’s getting kinda late sweetheart, go to bed. It’s a school night.",
            "I didn’t raise no vampire, take a walk.",
            "Honey, you’re burning your retinas playing all these games… eat some carrots, it’ll help.",
            "You’re doing great, sweetie.",
            "If you’re waiting, get a little exercise in.",
            "An apple a day keeps the doctor away.",
            "Don’t snack so often, leave your room for meals."]

user_dic = {}

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.content.lower() == "hi":
        await message.channel.send("Hello.")

    if message.content.lower() == "hi mom" or message.content.lower() == "hi mommy":
        await message.channel.send("Hi, sweetie.")

    if message.content.lower() == "mom where r u" or message.content.lower() == "mommy where r u" or message.content.lower() == "mommy where are you":
        await message.channel.send("I'm right here, sweetheart.")

    if message.content.lower() == "thanks mom" or message.content.lower() == "thanks mommy":
        await message.channel.send("No problem, sweetie.")

    if message.content.lower() in plist:
        await message.channel.send("https://imgur.com/gallery/St5r04n")

    if message.author not in user_dic:
        user_dic[message.author] = []
    user_dic[message.author].append('x')
    if(len(user_dic[message.author]) % 10 == 0):
        ran = random.choice(quotes)
        await message.channel.send(f'{message.author}! {ran}')

client.run(TOKEN)
