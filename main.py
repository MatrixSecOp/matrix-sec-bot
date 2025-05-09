from dotenv import load_dotenv
import os
import discord
from keep_alive import keep_alive

load_dotenv()  # Load .env variables

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$menu'):
        await message.channel.send('''choose any option from below:
1. Latest Tech News
2. Cybersecurity News
3. Hacker & Threat Intel Feed
4. Search by Topic
5. News by Date
6. Vulnerability & CVE Tracker
7. Save or Bookmark Articles
8. Preferences / Settings''')


keep_alive()  # Starts a webserver to be pinged.
client.run(os.getenv('TOKEN'))
