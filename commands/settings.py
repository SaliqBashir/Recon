"""
/settings command for managing server settings (log channel, fun commands, etc.)
"""
import discord
from discord.ext import commands
from db import get_guild_settings_collection

COMMAND_NAME = "settings"
COMMAND_DESCRIPTION = "Bot settings for the server"
COMMAND_USAGE = "/settings [subcommand]"

class SettingsCog(discord.Cog):
    def __init__(self, bot):
        self.bot = bot

    settings = discord.SlashCommandGroup(
        name=COMMAND_NAME,
        description=COMMAND_DESCRIPTION
    )
    @settings.command(name="show", description="Show current settings")
    async def show(self, ctx: discord.ApplicationContext):
        """Show current server settings"""
        col = get_guild_settings_collection()
        doc = await col.find_one({"_id": ctx.guild.id})
        if not doc:
            doc = {"_id": ctx.guild.id, "log_channel_id": None, "fun_enabled": True, "modlog_enabled": True}
            await col.insert_one(doc)
        embed = discord.Embed(title=f"Settings for {ctx.guild.name}", color=discord.Color.blurple())
        embed.add_field(name="Log Channel", value=f'<#{doc.get("log_channel_id")}>' if doc.get("log_channel_id") else "Not set", inline=False)
        embed.add_field(name="Fun Commands", value="Enabled" if doc.get("fun_enabled", True) else "Disabled", inline=True)
        embed.add_field(name="Mod Logs", value="Enabled" if doc.get("modlog_enabled", True) else "Disabled", inline=True)
        await ctx.respond(embed=embed)

    @settings.command(name="setlog", description="Set the moderation log channel")
    async def setlog(self, ctx: discord.ApplicationContext, channel: discord.Option(discord.TextChannel, "Log channel")): # type: ignore
        col = get_guild_settings_collection()
        await col.update_one({"_id": ctx.guild.id}, {"$set": {"log_channel_id": channel.id}}, upsert=True)
        await ctx.respond(f"Log channel set to {channel.mention}")

    @settings.command(name="togglefun", description="Enable or disable fun commands")
    async def togglefun(self, ctx: discord.ApplicationContext, enabled: bool):
        col = get_guild_settings_collection()
        await col.update_one({"_id": ctx.guild.id}, {"$set": {"fun_enabled": enabled}}, upsert=True)
        await ctx.respond(f"Fun commands {'enabled' if enabled else 'disabled'}.")

    @settings.command(name="togglemodlog", description="Enable or disable moderation logs")
    async def togglemodlog(self, ctx: discord.ApplicationContext, enabled: bool):
        col = get_guild_settings_collection()
        await col.update_one({"_id": ctx.guild.id}, {"$set": {"modlog_enabled": enabled}}, upsert=True)
        await ctx.respond(f"Moderation logs {'enabled' if enabled else 'disabled'}.")

def setup(bot):
    bot.add_cog(SettingsCog(bot))
    print("🔧 Command 'settings' registered successfully")
