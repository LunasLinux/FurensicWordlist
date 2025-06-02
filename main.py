import discord
import os
from dotenv import load_dotenv
from utils.guild_scanner import load_hitlist

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
hitlist = load_hitlist()

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Furensic bot is online as {client.user}')

@client.event
async def on_member_join(member):
    guild_id = str(member.guild.id)
    if guild_id in hitlist:
        print(f"[FLAG] {member} joined flagged guild: {member.guild.name}")

client.run(TOKEN)
