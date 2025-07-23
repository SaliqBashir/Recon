"""
/kick and /ban commands with logging
"""
import discord
from discord.ext import commands
from db import get_mod_logs_collection, get_guild_settings_collection
from datetime import datetime

class KickBanCog(discord.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(
        name="kick",
        description="Kick a user and log it"
    )
    @discord.default_permissions(kick_members=True)
    async def kick(self, ctx: discord.ApplicationContext, user: discord.Member, reason: str):
        # Only allow mods (kick_members) to use this command
        if not ctx.author.guild_permissions.kick_members:
            embed = discord.Embed(title="Missing Permissions", description="You do not have permission to kick members.", color=discord.Color.red())
            await ctx.respond(embed=embed, ephemeral=True)
            return
        try:
            await user.kick(reason=reason)
            col = get_mod_logs_collection()
            log = {
                "guild_id": ctx.guild.id,
                "user_id": user.id,
                "action": "kick",
                "reason": reason,
                "moderator_id": ctx.author.id,
                "timestamp": datetime.utcnow()
            }
            await col.insert_one(log)
            embed = discord.Embed(title="User Kicked", color=discord.Color.red(), timestamp=datetime.utcnow())
            embed.add_field(name="User", value=user.mention)
            embed.add_field(name="Moderator", value=ctx.author.mention)
            embed.add_field(name="Reason", value=reason)
            await ctx.respond(embed=embed)
            settings = await get_guild_settings_collection().find_one({"_id": ctx.guild.id})
            if settings and settings.get("log_channel_id"):
                channel = ctx.guild.get_channel(settings["log_channel_id"])
                if channel:
                    await channel.send(embed=embed)
        except discord.Forbidden:
            embed = discord.Embed(title="Missing Permissions", description="I do not have permission to kick this user.", color=discord.Color.red())
            await ctx.respond(embed=embed, ephemeral=True)
        except Exception as e:
            embed = discord.Embed(title="Error", description=f"An error occurred: {e}", color=discord.Color.red())
            await ctx.respond(embed=embed, ephemeral=True)

    @discord.slash_command(
        name="ban",
        description="Ban a user and log it"
    )
    @discord.default_permissions(ban_members=True)
    async def ban(self, ctx: discord.ApplicationContext, user: discord.Member, reason: str):
        # Only allow mods (ban_members) to use this command
        if not ctx.author.guild_permissions.ban_members:
            embed = discord.Embed(title="Missing Permissions", description="You do not have permission to ban members.", color=discord.Color.red())
            await ctx.respond(embed=embed, ephemeral=True)
            return
        try:
            await user.ban(reason=reason)
            col = get_mod_logs_collection()
            log = {
                "guild_id": ctx.guild.id,
                "user_id": user.id,
                "action": "ban",
                "reason": reason,
                "moderator_id": ctx.author.id,
                "timestamp": datetime.utcnow()
            }
            await col.insert_one(log)
            embed = discord.Embed(title="User Banned", color=discord.Color.red(), timestamp=datetime.utcnow())
            embed.add_field(name="User", value=user.mention)
            embed.add_field(name="Moderator", value=ctx.author.mention)
            embed.add_field(name="Reason", value=reason)
            await ctx.respond(embed=embed)
            settings = await get_guild_settings_collection().find_one({"_id": ctx.guild.id})
            if settings and settings.get("log_channel_id"):
                channel = ctx.guild.get_channel(settings["log_channel_id"])
                if channel:
                    await channel.send(embed=embed)
        except discord.Forbidden:
            embed = discord.Embed(title="Missing Permissions", description="I do not have permission to ban this user.", color=discord.Color.red())
            await ctx.respond(embed=embed, ephemeral=True)
        except Exception as e:
            embed = discord.Embed(title="Error", description=f"An error occurred: {e}", color=discord.Color.red())
            await ctx.respond(embed=embed, ephemeral=True)

def setup(bot):
    bot.add_cog(KickBanCog(bot))
    print("🔧 Command 'kick' and 'ban' registered successfully")
