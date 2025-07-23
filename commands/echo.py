import discord
from discord.ext import commands

# ====== COMMAND CONFIGURATION ======
COMMAND_NAME = "echo"
COMMAND_DESCRIPTION = "Repeats what users says."
COMMAND_USAGE = "/echo [text]"

class Echo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Command with options/parameters
    @discord.slash_command(
        name=f"{COMMAND_NAME}",
        description="Template command with options"
    )
    async def echo(
        self,
        ctx: discord.ApplicationContext,
        user: discord.Option(discord.Member, "Select a Nigger", required=True)
    ):
        await ctx.respond(f"{user} is a Nigger.")
        
def setup(bot):
    """Required setup function for automatic loading"""
    bot.add_cog(Echo(bot))
    print(f"Command '{COMMAND_NAME}' registered successfully")
