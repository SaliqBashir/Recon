"""
Server Information Command
Shows detailed information about the Discord server
"""

import discord
from discord.ext import commands
from datetime import datetime

# Command configuration
COMMAND_NAME = "serverinfo"
COMMAND_DESCRIPTION = "Get detailed information about this server"
COMMAND_USAGE = "/serverinfo"

class ServerinfoCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(
        name=COMMAND_NAME,
        description=COMMAND_DESCRIPTION
    )
    async def serverinfo_command(self, ctx: discord.ApplicationContext):
        """Get detailed information about the server"""

        guild = ctx.guild

        # Create embed
        embed = discord.Embed(
            title=f"Server Information - {guild.name}",
            color=discord.Color.blue()
        )

        # Set server icon
        if guild.icon:
            embed.set_thumbnail(url=guild.icon.url)

        # Basic info
        embed.add_field(
            name="📊 Basic Info",
            value=f"**Name:** {guild.name}\n"
                  f"**ID:** {guild.id}\n"
                  f"**Owner:** {guild.owner.mention if guild.owner else 'Unknown'}\n"
                  f"**Created:** {discord.utils.format_dt(guild.created_at, 'F')}",
            inline=True
        )

        # Member counts
        total_members = guild.member_count
        humans = len([m for m in guild.members if not m.bot])
        bots = len([m for m in guild.members if m.bot])

        online_members = len([m for m in guild.members if m.status != discord.Status.offline])

        embed.add_field(
            name="👥 Members",
            value=f"**Total:** {total_members}\n"
                  f"**Humans:** {humans}\n"
                  f"**Bots:** {bots}\n"
                  f"**Online:** {online_members}",
            inline=True
        )

        # Channel counts
        text_channels = len(guild.text_channels)
        voice_channels = len(guild.voice_channels)
        categories = len(guild.categories)

        embed.add_field(
            name="📺 Channels",
            value=f"**Text:** {text_channels}\n"
                  f"**Voice:** {voice_channels}\n"
                  f"**Categories:** {categories}\n"
                  f"**Total:** {len(guild.channels)}",
            inline=True
        )

        # Server features
        features = []
        if "COMMUNITY" in guild.features:
            features.append("Community")
        if "PARTNERED" in guild.features:
            features.append("Partnered")
        if "VERIFIED" in guild.features:
            features.append("Verified")
        if "WELCOME_SCREEN_ENABLED" in guild.features:
            features.append("Welcome Screen")
        if "MEMBER_VERIFICATION_GATE_ENABLED" in guild.features:
            features.append("Membership Screening")
        if "THREADS_ENABLED" in guild.features:
            features.append("Threads")

        if features:
            embed.add_field(
                name="✨ Features",
                value=", ".join(features[:6]),
                inline=True
            )

        # Boost info
        boost_level = guild.premium_tier
        boost_count = guild.premium_subscription_count

        embed.add_field(
            name="🚀 Nitro Boosts",
            value=f"**Level:** {boost_level}\n"
                  f"**Boosts:** {boost_count}",
            inline=True
        )

        # Role count
        embed.add_field(
            name="🎭 Roles",
            value=f"**Total:** {len(guild.roles)}",
            inline=True
        )

        # Verification level
        verification_levels = {
            discord.VerificationLevel.none: "None",
            discord.VerificationLevel.low: "Low",
            discord.VerificationLevel.medium: "Medium",
            discord.VerificationLevel.high: "High",
            discord.VerificationLevel.highest: "Highest"
        }

        embed.add_field(
            name="🔒 Security",
            value=f"**Verification:** {verification_levels.get(guild.verification_level, 'Unknown')}\n"
                  f"**MFA Required:** {'Yes' if guild.mfa_level else 'No'}",
            inline=True
        )

        # Server banner
        if guild.banner:
            embed.set_image(url=guild.banner.url)

        embed.set_footer(text=f"Requested by {ctx.author.display_name}")
        embed.timestamp = datetime.utcnow()

        await ctx.respond(embed=embed)

def setup(bot):
    """Required setup function for automatic loading (py-cord)"""
    bot.add_cog(ServerinfoCommand(bot))
    print(f"Command '{COMMAND_NAME}' registered successfully")
