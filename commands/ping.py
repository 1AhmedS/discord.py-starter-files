import discord
from discord.ext import commands
from discord import app_commands

class PingCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping", description="ping pong!")
    async def ping(self, ctx):
        latency = round(self.bot.latency * 1000)  # Convert latency to milliseconds
        await ctx.send(f':ping_pong: pong! {latency}ms')

    @app_commands.command(name="ping", description="ping pong!")
    async def slash_ping(self, interaction: discord.Interaction):
        latency = round(self.bot.latency * 1000)  # Convert latency to milliseconds
        await interaction.response.send_message(f':ping_pong: pong! {latency}ms')

async def setup(bot):
    await bot.add_cog(PingCommand(bot))