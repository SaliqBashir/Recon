"""
/rapsheet command: show all moderation actions for a user
"""
import discord
from db import get_mod_logs_collection
from datetime import datetime

class RapSheetCog(discord.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(
        name="rapsheet",
        description="Show all moderation actions (warnings, kicks, bans) for a user."
    )
    @discord.default_permissions(kick_members=True)
    async def rapsheet(self, ctx: discord.ApplicationContext, user: discord.Member):
        # Only allow mods (kick_members) to use this command
        if not ctx.author.guild_permissions.kick_members:
            embed = discord.Embed(title="Missing Permissions", description="You do not have permission to view rapsheets.", color=discord.Color.red())
            await ctx.respond(embed=embed, ephemeral=True)
            return
        try:
            col = get_mod_logs_collection()
            logs = col.find({"guild_id": ctx.guild.id, "user_id": user.id})
            actions = [log async for log in logs]
            if not actions:
                embed = discord.Embed(
                    title=f"Rap Sheet for {user.display_name}",
                    description="No moderation actions found.",
                    color=discord.Color.green()
                )
                await ctx.respond(embed=embed, ephemeral=True)
                return
            # Sort by timestamp
            actions.sort(key=lambda x: x.get("timestamp", datetime.min))
            embed = discord.Embed(
                title=f"Rap Sheet for {user.display_name}",
                color=discord.Color.orange(),
                timestamp=datetime.utcnow()
            )
            for i, entry in enumerate(actions, 1):
                action = entry.get("action", "?").capitalize()
                reason = entry.get("reason", "No reason provided.")
                mod_id = entry.get("moderator_id")
                mod = ctx.guild.get_member(mod_id)
                mod_str = mod.mention if mod else (f"<@{mod_id}>" if mod_id else "Unknown")
                time = entry.get("timestamp")
                if isinstance(time, datetime):
                    time_str = time.strftime('%Y-%m-%d %H:%M UTC')
                else:
                    time_str = str(time)
                embed.add_field(
                    name=f"{i}. {action}",
                    value=f"By: {mod_str}\nReason: {reason}\nAt: {time_str}",
                    inline=False
                )
            await ctx.respond(embed=embed, ephemeral=True)
        except discord.errors.Forbidden:
            await ctx.respond(embed=discord.Embed(
                title="Missing Permissions",
                description="I do not have permission to view members or send embeds.",
                color=discord.Color.red()
            ), ephemeral=True)
        except Exception as e:
            embed = discord.Embed(
                title="Error",
                description=f"An error occurred: {e}",
                color=discord.Color.red()
            )
            await ctx.respond(embed=embed, ephemeral=True)

def setup(bot):
    bot.add_cog(RapSheetCog(bot))
    print("🔧 Command 'rapsheet' registered successfully")
