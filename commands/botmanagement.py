"""
Bot Management Command
Commands for managing the bot (reload, status, etc.)
"""

import discord
from discord.ext import commands
import importlib
import sys
import traceback
from datetime import datetime, timedelta

# Command configuration
COMMAND_NAME = "bot"
COMMAND_DESCRIPTION = "Bot management commands"
COMMAND_USAGE = "/bot [subcommand]"

class BotManagementCommand(discord.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = datetime.utcnow()

    group = discord.SlashCommandGroup(
        name=COMMAND_NAME,
        description=COMMAND_DESCRIPTION
    )

    @group.command(name="status", description="Show bot status and statistics")
    async def status(self, ctx: discord.ApplicationContext):
        uptime = datetime.utcnow() - self.start_time
        uptime_str = str(uptime).split('.')[0]
        total_guilds = len(self.bot.guilds)
        total_users = len(set(self.bot.get_all_members()))
        total_commands = len(self.bot.loaded_commands)
        total_events = len(self.bot.loaded_events)
        embed = discord.Embed(
            title="🤖 Bot Status",
            color=discord.Color.green()
        )
        embed.add_field(
            name="📊 Statistics",
            value=f"**Servers:** {total_guilds}\n"
                  f"**Users:** {total_users}\n"
                  f"**Commands:** {total_commands}\n"
                  f"**Events:** {total_events}",
            inline=True
        )
        embed.add_field(
            name="⏱️ Performance",
            value=f"**Latency:** {round(self.bot.latency * 1000)}ms\n"
                  f"**Uptime:** {uptime_str}",
            inline=True
        )
        embed.set_footer(text=f"Bot started at {self.start_time.strftime('%Y-%m-%d %H:%M:%S UTC')}")
        await ctx.respond(embed=embed)

    @group.command(name="reload", description="Reload bot commands and events")
    async def reload(self, ctx: discord.ApplicationContext):
        if not ctx.author.guild_permissions.administrator:
            await ctx.respond("❌ You need Administrator permissions to use this command.", ephemeral=True)
            return
        await ctx.defer()
        try:
            await self.bot.reload_commands()
            await self.bot.reload_events()
            await ctx.respond("✅ Reloaded all commands and events!")
        except Exception as e:
            await ctx.respond(f"❌ Reload failed: {e}")

    @group.command(name="info", description="Show detailed bot information")
    async def info(self, ctx: discord.ApplicationContext):
        embed = discord.Embed(
            title="ℹ️ Bot Information",
            description="Professional Discord Bot with automatic command/event loading",
            color=discord.Color.blue()
        )
        embed.set_footer(text="Created with ❤️ for professional Discord bot development")
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(BotManagementCommand(bot))
    print(f"Command '{COMMAND_NAME}' registered successfully")
