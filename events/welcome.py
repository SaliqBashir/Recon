"""
Event listeners for joining member
"""
import discord

# ====== EVENT CONFIGURATION ======
EVENT_NAME = "welcome"
EVENT_DESCRIPTION = "Sends a welcome message whenever a person joins."

class Welcome(discord.Cog):
    def __init__(self, bot):
        self.bot = bot

    # ====== MEMBER EVENTS ======
    @discord.Cog.listener()
    async def on_member_join(self, member):
        channel = discord.utils.get(member.guild.channels, name="welcome")
        if channel:
            await channel.send(f"Welcome {member.mention}, Hope you enjoy your stay here.")

def setup(bot):
    bot.add_cog(Welcome(bot))
    print("🔧 Events 'welcome' registered successfully") 
