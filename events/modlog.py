"""
Event listeners for kick/ban logging
"""
import discord
from db import get_mod_logs_collection, get_guild_settings_collection
from datetime import datetime

class ModLogEvents(discord.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.Cog.listener()
    async def on_member_ban(self, guild, user):
        col = get_mod_logs_collection()
        log = {
            "guild_id": guild.id,
            "user_id": user.id,
            "action": "ban",
            "reason": "(unknown)",
            "moderator_id": None,
            "timestamp": datetime.utcnow()
        }
        await col.insert_one(log)
        settings = await get_guild_settings_collection().find_one({"_id": guild.id})
        if settings and settings.get("log_channel_id"):
            channel = guild.get_channel(settings["log_channel_id"])
            if channel:
                embed = discord.Embed(title="User Banned", color=discord.Color.red(), timestamp=datetime.utcnow())
                embed.add_field(name="User", value=f"<@{user.id}>")
                await channel.send(embed=embed)

    @discord.Cog.listener()
    async def on_member_remove(self, member):
        # Could be a kick or leave, can't always tell
        # Optionally, log as a kick if you want
        pass

def setup(bot):
    bot.add_cog(ModLogEvents(bot))
    print("🔧 Events 'modlog' registered successfully")
