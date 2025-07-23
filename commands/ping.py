"""
Ping command - Template for Discord bot commands
This command responds with the bot's latency
"""

import discord
from discord.ext import commands

# Command configuration
COMMAND_NAME = "ping"
COMMAND_DESCRIPTION = "Check the bot's latency"
COMMAND_USAGE = "/ping"

class PingCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(
        name=COMMAND_NAME,
        description=COMMAND_DESCRIPTION
    )
    async def ping_command(self, ctx: discord.ApplicationContext):
        """Ping command to check bot latency"""
        latency = round(self.bot.latency * 1000)

        embed = discord.Embed(
            title="🏓 Pong!",
            description=f"Bot latency: `{latency}ms`",
            color=discord.Color.green()
        )
        embed.set_footer(text=f"Requested by {ctx.author.display_name}")

        await ctx.respond(embed=embed)

def setup(bot):
    """Required setup function for automatic loading (py-cord)"""
    bot.add_cog(PingCommand(bot))
    print(f"Command '{COMMAND_NAME}' registered successfully")
