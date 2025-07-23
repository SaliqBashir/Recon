"""
/warn command and warning log system
"""
import discord
from discord.ext import commands
from db import get_mod_logs_collection, get_guild_settings_collection
from datetime import datetime


class WarnCog(discord.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(
        name="warn",
        description="Warn a user and log it"
    )
    @discord.default_permissions(kick_members=True)
    async def warn(self, ctx: discord.ApplicationContext, user: discord.Member, reason: str):
        # Only allow mods (kick_members) to use this command
        if not ctx.author.guild_permissions.kick_members:
            embed = discord.Embed(title="Missing Permissions", description="You do not have permission to warn members.", color=discord.Color.red())
            await ctx.respond(embed=embed, ephemeral=True)
            return
        try:
            col = get_mod_logs_collection()
            log = {
                "guild_id": ctx.guild.id,
                "user_id": user.id,
                "action": "warn",
                "reason": reason,
                "moderator_id": ctx.author.id,
                "timestamp": datetime.utcnow()
            }
            await col.insert_one(log)
            embed = discord.Embed(title="User Warned", color=discord.Color.orange(), timestamp=datetime.utcnow())
            embed.add_field(name="User", value=user.mention)
            embed.add_field(name="Moderator", value=ctx.author.mention)
            embed.add_field(name="Reason", value=reason)
            await ctx.respond(embed=embed)
            # Log to channel if set
            settings = await get_guild_settings_collection().find_one({"_id": ctx.guild.id})
            if settings and settings.get("log_channel_id"):
                channel = ctx.guild.get_channel(settings["log_channel_id"])
                if channel:
                    await channel.send(embed=embed)
        except discord.Forbidden:
            embed = discord.Embed(title="Missing Permissions", description="I do not have permission to warn this user.", color=discord.Color.red())
            await ctx.respond(embed=embed, ephemeral=True)
        except Exception as e:
            embed = discord.Embed(title="Error", description=f"An error occurred: {e}", color=discord.Color.red())
            await ctx.respond(embed=embed, ephemeral=True)

def setup(bot):
    bot.add_cog(WarnCog(bot))
    print("🔧 Command 'warn' registered successfully")
