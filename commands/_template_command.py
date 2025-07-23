"""
Command Template - Copy this file to create new commands
Rename the file and modify the configuration below
"""

import discord
from discord.ext import commands

# ====== COMMAND CONFIGURATION ======
COMMAND_NAME = "template"
COMMAND_DESCRIPTION = "This is a template command"
COMMAND_USAGE = "/template [option]"

class TemplateCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Simple slash command
    @discord.slash_command(
        name=COMMAND_NAME,
        description=COMMAND_DESCRIPTION
    )
    async def template_command(self, ctx: discord.ApplicationContext):
        """Basic template command"""
        await ctx.respond("This is a template command!")

    # Command with options/parameters
    @discord.slash_command(
        name=f"{COMMAND_NAME}_with_options",
        description="Template command with options"
    )
    async def template_with_options(
        self,
        ctx: discord.ApplicationContext,
        text: discord.Option(str, "Enter some text", required=True),
        number: discord.Option(int, "Enter a number", required=False, default=1),
        user: discord.Option(discord.Member, "Select a user", required=False)
    ):
        """Template command with various option types"""

        embed = discord.Embed(
            title="Template Command Result",
            color=discord.Color.blue()
        )
        embed.add_field(name="Text", value=text, inline=False)
        embed.add_field(name="Number", value=str(number), inline=True)

        if user:
            embed.add_field(name="Selected User", value=user.mention, inline=True)

        embed.set_footer(text=f"Executed by {ctx.author.display_name}")

        await ctx.respond(embed=embed)

    # Command with subcommands (command groups)
    template_group = discord.SlashCommandGroup(
        name=f"{COMMAND_NAME}_group",
        description="Template command group"
    )

    @template_group.command(name="subcommand1", description="First subcommand")
    async def subcommand1(self, ctx: discord.ApplicationContext):
        await ctx.respond("This is subcommand 1!")

    @template_group.command(name="subcommand2", description="Second subcommand")
    async def subcommand2(self, ctx: discord.ApplicationContext):
        await ctx.respond("This is subcommand 2!")

    # Context menu command (right-click on user)
    @discord.user_command(name="Template User Action")
    async def template_user_action(self, ctx: discord.ApplicationContext, user: discord.Member):
        await ctx.respond(f"You used the template action on {user.mention}!", ephemeral=True)

    # Message context menu (right-click on message)
    @discord.message_command(name="Template Message Action")
    async def template_message_action(self, ctx: discord.ApplicationContext, message: discord.Message):
        await ctx.respond(f"You used the template action on a message by {message.author.mention}!", ephemeral=True)

async def setup(bot):
    """Required setup function for automatic loading"""
    await bot.add_cog(TemplateCommand(bot))
    print(f"Command '{COMMAND_NAME}' registered successfully")

# ====== DEVELOPMENT NOTES ======
"""
To create a new command:
1. Copy this file to a new file in the commands/ folder
2. Rename the file (e.g., 'userinfo.py')
3. Update COMMAND_NAME, COMMAND_DESCRIPTION, and COMMAND_USAGE
4. Rename the class (e.g., 'UserinfoCommand')
5. Implement your command logic
6. The bot will automatically load it when you restart!

Available option types for commands:
- str: Text input
- int: Integer input
- float: Decimal number input
- bool: True/False input
- discord.Member: User selection
- discord.User: User selection (includes users not in the server)
- discord.Role: Role selection
- discord.TextChannel: Text channel selection
- discord.VoiceChannel: Voice channel selection
- discord.CategoryChannel: Category selection
- discord.Attachment: File upload

Command decorators:
- @discord.slash_command: Creates a slash command
- @discord.user_command: Creates a user context menu command
- @discord.message_command: Creates a message context menu command
- @commands.command: Creates a traditional prefix command (if you enable message content intent)
"""
