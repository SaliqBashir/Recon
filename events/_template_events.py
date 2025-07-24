"""
Event Template - Copy this file to create new events
Rename the file and modify the configuration below
"""

import discord

# ====== EVENT CONFIGURATION ======
EVENT_NAME = "template_events"
EVENT_DESCRIPTION = "Template for various Discord events"

class TemplateEvents(discord.Cog):
    def __init__(self, bot):
        self.bot = bot

    # ====== MESSAGE EVENTS ======
    @discord.Cog.listener()
    async def on_message(self, message):
        """Triggered when any message is sent"""
        # Ignore messages from bots
        if message.author.bot:
            return

        # Example: React to messages containing certain words
        if "hello" in message.content.lower():
            await message.add_reaction("👋")

        # Log message (optional)
        print(f"📝 Message from {message.author}: {message.content[:50]}...")

    @discord.Cog.listener()
    async def on_message_delete(self, message):
        """Triggered when a message is deleted"""
        if message.author.bot:
            return

        print(f"🗑️ Message deleted by {message.author}: {message.content}")

    @discord.Cog.listener()
    async def on_message_edit(self, before, after):
        """Triggered when a message is edited"""
        if before.author.bot:
            return

        print(f"✏️ Message edited by {before.author}")
        print(f"   Before: {before.content}")
        print(f"   After: {after.content}")

    # ====== MEMBER EVENTS ======
    @discord.Cog.listener()
    async def on_member_join(self, member):
        """Triggered when a member joins the server"""
        print(f"👋 {member.name} joined {member.guild.name}")

        # Example: Send welcome message
        # channel = discord.utils.get(member.guild.channels, name="welcome")
        # if channel:
        #     await channel.send(f"Welcome {member.mention}!")

    @discord.Cog.listener()
    async def on_member_remove(self, member):
        """Triggered when a member leaves the server"""
        print(f"👋 {member.name} left {member.guild.name}")

    @discord.Cog.listener()
    async def on_member_update(self, before, after):
        """Triggered when a member's profile is updated"""
        # Check what changed
        if before.nick != after.nick:
            print(f"🏷️ {after.name} changed nickname: {before.nick} → {after.nick}")

        if before.roles != after.roles:
            added_roles = set(after.roles) - set(before.roles)
            removed_roles = set(before.roles) - set(after.roles)

            for role in added_roles:
                print(f"➕ {after.name} gained role: {role.name}")

            for role in removed_roles:
                print(f"➖ {after.name} lost role: {role.name}")

    # ====== REACTION EVENTS ======
    @discord.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        """Triggered when a reaction is added to a message"""
        if user.bot:
            return

        print(f"👍 {user.name} reacted with {reaction.emoji}")

        # Example: Role reactions
        # if reaction.emoji == "🎯" and reaction.message.id == ROLE_MESSAGE_ID:
        #     role = discord.utils.get(user.guild.roles, name="Target Role")
        #     if role:
        #         await user.add_roles(role)

    @discord.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        """Triggered when a reaction is removed from a message"""
        if user.bot:
            return

        print(f"👎 {user.name} removed reaction {reaction.emoji}")

    # ====== VOICE EVENTS ======
    @discord.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        """Triggered when a member's voice state changes"""
        if before.channel != after.channel:
            if before.channel is None:
                print(f"🔊 {member.name} joined voice channel: {after.channel.name}")
            elif after.channel is None:
                print(f"🔇 {member.name} left voice channel: {before.channel.name}")
            else:
                print(f"🔄 {member.name} moved from {before.channel.name} to {after.channel.name}")

    # ====== GUILD EVENTS ======
    @discord.Cog.listener()
    async def on_guild_join(self, guild):
        """Triggered when the bot joins a new server"""
        print(f"🎉 Bot joined new server: {guild.name} ({guild.member_count} members)")

    @discord.Cog.listener()
    async def on_guild_remove(self, guild):
        """Triggered when the bot leaves a server"""
        print(f"😢 Bot left server: {guild.name}")

    # ====== ERROR HANDLING ======
    @discord.Cog.listener()
    async def on_application_command_error(self, ctx, error):
        """Triggered when a slash command encounters an error"""
        print(f"Command error in {ctx.command}: {error}")

        if isinstance(error, commands.CommandOnCooldown):
            await ctx.respond(f"Command is on cooldown. Try again in {error.retry_after:.2f} seconds.", ephemeral=True)
        elif isinstance(error, commands.MissingPermissions):
            await ctx.respond("You don't have permission to use this command.", ephemeral=True)
        else:
            await ctx.respond("An error occurred while executing the command.", ephemeral=True)

async def setup(bot):
    """Required setup function for automatic loading"""
    await bot.add_cog(TemplateEvents(bot))
    print(f"🔧 Events '{EVENT_NAME}' registered successfully")

# ====== DEVELOPMENT NOTES ======
"""
To create a new event handler:
1. Copy this file to a new file in the events/ folder
2. Rename the file (e.g., 'moderation.py')
3. Update EVENT_NAME and EVENT_DESCRIPTION
4. Rename the class (e.g., 'ModerationEvents')
5. Remove events you don't need and implement the ones you do
6. The bot will automatically load it when you restart!

Available Discord events:
- on_ready: Bot is ready
- on_message: Message sent
- on_message_delete: Message deleted
- on_message_edit: Message edited
- on_reaction_add: Reaction added
- on_reaction_remove: Reaction removed
- on_member_join: Member joins server
- on_member_remove: Member leaves server
- on_member_update: Member profile updated
- on_user_update: User profile updated (global)
- on_voice_state_update: Voice state changed
- on_guild_join: Bot joins server
- on_guild_remove: Bot leaves server
- on_guild_update: Server settings updated
- on_guild_role_create: Role created
- on_guild_role_delete: Role deleted
- on_guild_role_update: Role updated
- on_guild_channel_create: Channel created
- on_guild_channel_delete: Channel deleted
- on_guild_channel_update: Channel updated
- on_application_command_error: Command error
- on_error: General error

Event listener decorator: @discord.Cog.listener()
All event methods must be async and match the exact event name.
"""
