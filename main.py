import discord
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv
import asyncio
import datetime

load_dotenv()

intents = discord.Intents.default()
intents.guilds = True
intents.voice_states = True
intents.messages = True
intents.message_reactions = True

bot = commands.Bot(command_prefix='!', intents=intents)
line = '─' * 50
line2 = '─' * 22
line3 = '─' * 20

@bot.event
async def on_ready():
    print(line)
    print(f'🌐 {bot.user} is now online!')
    print(line)
    print(f'🤖 Bot Username  : {bot.user.name}')
    print(f'🆔 Bot ID        : {bot.user.id}')
    print(f'⏲ Launched On   : {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    print(line)
    print(f'📊 Connected to  : {len(bot.guilds)} Server(s)')
    print(f'👥 Total Users   : {len(bot.users)}')
    print(line2+'📞 Contact'+line2)
    print('© 2025 AhmedSamir - All Rights Reserved.')
    print(f'➕ Invite link: {discord.utils.oauth_url(bot.user.id)}')
    print('🔗 GitHub: https://github.com/1AhmedS')
    print('🕊 Twitter: https://x.com/nsl2j')
    print('💬 Discord: https://discord.gg/hTkzz2ZzJA')
    print(line)
    print('✅ Bot is fully operational and ready to serve!')
    print(line3+'📜 Commands'+line3)
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} command(s)'+f'\n{line}')
        for command in synced:
            print(f'✅ {command.name}')
            print(f'📝 {command.description}'f'\n{line}')
            
    except Exception as e:
        print(f'Failed to sync commands: {e}')

async def load_extensions():
    for filename in os.listdir('./commands'):
        if filename.endswith('.py'):
            await bot.load_extension(f'commands.{filename[:-3]}')

async def main():
    await load_extensions()
    await bot.start(os.getenv('TOKEN'))

asyncio.run(main())