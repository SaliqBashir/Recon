"""
User Information Command
Shows detailed information about a Discord user
"""

import discord
from discord.ext import commands
from datetime import datetime

# Command configuration
COMMAND_NAME = "userinfo"
COMMAND_DESCRIPTION = "Get detailed information about a user"
COMMAND_USAGE = "/userinfo [user]"

class UserinfoCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(
        name=COMMAND_NAME,
        description=COMMAND_DESCRIPTION
    )
    async def userinfo_command(
        self,
        ctx: discord.ApplicationContext,
        user: discord.Option(discord.Member, "The user to get info about", required=False)
    ):
        """Get detailed information about a user"""

        # If no user specified, use the command author
        target_user = user or ctx.author

        # Create embed
        embed = discord.Embed(
            title=f"User Information - {target_user.display_name}",
            color=target_user.color if target_user.color != discord.Color.default() else discord.Color.blue()
        )

        # Set user avatar
        embed.set_thumbnail(url=target_user.avatar.url if target_user.avatar else target_user.default_avatar.url)

        # Basic info
        embed.add_field(
            name="👤 Basic Info",
            value=f"**Username:** {target_user.name}\n"
                  f"**Display Name:** {target_user.display_name}\n"
                  f"**ID:** {target_user.id}\n"
                  f"**Bot:** {'Yes' if target_user.bot else 'No'}",
            inline=True
        )

        # Account dates
        account_created = target_user.created_at
        joined_server = target_user.joined_at if hasattr(target_user, 'joined_at') else None

        date_info = f"**Account Created:** {discord.utils.format_dt(account_created, 'F')}\n"
        date_info += f"**Account Age:** {discord.utils.format_dt(account_created, 'R')}\n"

        if joined_server:
            date_info += f"**Joined Server:** {discord.utils.format_dt(joined_server, 'F')}\n"
            date_info += f"**Server Member For:** {discord.utils.format_dt(joined_server, 'R')}"

        embed.add_field(
            name="📅 Dates",
            value=date_info,
            inline=True
        )

        # Roles (if it's a guild member)
        if hasattr(target_user, 'roles') and len(target_user.roles) > 1:
            roles = [role.mention for role in target_user.roles[1:]]  # Skip @everyone
            roles_text = ", ".join(roles[:10])  # Limit to first 10 roles
            if len(target_user.roles) > 11:
                roles_text += f" and {len(target_user.roles) - 11} more..."

            embed.add_field(
                name=f"🎭 Roles ({len(target_user.roles) - 1})",
                value=roles_text,
                inline=False
            )

        # Status and activity
        if hasattr(target_user, 'status'):
            status_emoji = {
                discord.Status.online: "🟢",
                discord.Status.idle: "🟡",
                discord.Status.dnd: "🔴",
                discord.Status.offline: "⚫"
            }

            status_text = f"{status_emoji.get(target_user.status, '❓')} {target_user.status.name.title()}"

            if target_user.activity:
                activity = target_user.activity
                if activity.type == discord.ActivityType.playing:
                    status_text += f"\n🎮 Playing **{activity.name}**"
                elif activity.type == discord.ActivityType.streaming:
                    status_text += f"\n📺 Streaming **{activity.name}**"
                elif activity.type == discord.ActivityType.listening:
                    status_text += f"\n🎵 Listening to **{activity.name}**"
                elif activity.type == discord.ActivityType.watching:
                    status_text += f"\n👀 Watching **{activity.name}**"
                elif activity.type == discord.ActivityType.custom:
                    status_text += f"\n💭 {activity.name}"

            embed.add_field(
                name="💬 Status",
                value=status_text,
                inline=True
            )

        # Permissions (if it's a guild member)
        if hasattr(target_user, 'guild_permissions'):
            key_perms = []
            perms = target_user.guild_permissions

            if perms.administrator:
                key_perms.append("Administrator")
            if perms.manage_guild:
                key_perms.append("Manage Server")
            if perms.manage_channels:
                key_perms.append("Manage Channels")
            if perms.manage_roles:
                key_perms.append("Manage Roles")
            if perms.kick_members:
                key_perms.append("Kick Members")
            if perms.ban_members:
                key_perms.append("Ban Members")
            if perms.moderate_members:
                key_perms.append("Timeout Members")

            if key_perms:
                embed.add_field(
                    name="🔑 Key Permissions",
                    value=", ".join(key_perms[:5]),
                    inline=True
                )

        embed.set_footer(text=f"Requested by {ctx.author.display_name}")
        embed.timestamp = datetime.utcnow()

        await ctx.respond(embed=embed)

def setup(bot):
    """Required setup function for automatic loading (py-cord)"""
    bot.add_cog(UserinfoCommand(bot))
    print(f"Command '{COMMAND_NAME}' registered successfully")
