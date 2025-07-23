import discord
import os
import importlib
import traceback
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

class DiscordBot(discord.Bot):
    def __init__(self):
        super().__init__(
            intents=discord.Intents.all(),
            debug_guilds=[int(os.getenv("DEVGUILD"))] if os.getenv("DEVGUILD") else None  # Instant slash command registration for your test server
        )
        self.loaded_commands = set()
        self.loaded_events = set()

    async def setup_hook(self):
        await self.load_commands()
        await self.load_events()
        await self.sync_commands()

    async def load_commands(self):
        """Automatically load all commands from the commands folder"""
        commands_path = Path("commands")
        if not commands_path.exists():
            print("Commands folder not found!")
            return

        print(f"Looking for commands in: {commands_path.absolute()}")
        command_files = list(commands_path.glob("*.py"))
        print(f"Found {len(command_files)} Python files")

        for file_path in command_files:
            print(f"Processing file: {file_path.name}")
            if file_path.name.startswith("_"):
                print(f"Skipping template file: {file_path.name}")
                continue  # Skip files starting with underscore

            module_name = f"commands.{file_path.stem}"
            print(f"Attempting to import: {module_name}")
            try:
                module = importlib.import_module(module_name)
                print(f"Successfully imported: {module_name}")
                if hasattr(module, 'setup'):
                    print(f"Found setup function in {module_name}")
                    module.setup(self)
                    self.loaded_commands.add(module_name)
                    print(f"Loaded command: {file_path.stem}")
                else:
                    print(f"⚠️  Command file {file_path.stem} missing setup() function")
            except Exception as e:
                print(f"❌ Failed to load command {file_path.stem}: {e}")
                traceback.print_exc()

    async def load_events(self):
        """Automatically load all events from the events folder"""
        events_path = Path("events")
        if not events_path.exists():
            print("Events folder not found!")
            return

        print(f"Looking for events in: {events_path.absolute()}")
        event_files = list(events_path.glob("*.py"))
        print(f"Found {len(event_files)} Python files")

        for file_path in event_files:
            print(f"Processing file: {file_path.name}")
            if file_path.name.startswith("_"):
                print(f"Skipping template file: {file_path.name}")
                continue  # Skip files starting with underscore

            module_name = f"events.{file_path.stem}"
            print(f"Attempting to import: {module_name}")
            try:
                module = importlib.import_module(module_name)
                print(f"Successfully imported: {module_name}")
                if hasattr(module, 'setup'):
                    print(f"Found setup function in {module_name}")
                    module.setup(self)
                    self.loaded_events.add(module_name)
                    print(f"Loaded event: {file_path.stem}")
                else:
                    print(f"⚠️  Event file {file_path.stem} missing setup() function")
            except Exception as e:
                print(f"❌ Failed to load event {file_path.stem}: {e}")
                traceback.print_exc()

    async def reload_commands(self):
        """Reload all commands (useful for development)"""
        for module_name in list(self.loaded_commands):
            try:
                module = importlib.reload(importlib.import_module(module_name))
                print(f"Reloaded command: {module_name}")
            except Exception as e:
                print(f"Failed to reload command {module_name}: {e}")

    async def reload_events(self):
        """Reload all events (useful for development)"""
        for module_name in list(self.loaded_events):
            try:
                module = importlib.reload(importlib.import_module(module_name))
                print(f"🔄 Reloaded event: {module_name}")
            except Exception as e:
                print(f"❌ Failed to reload event {module_name}: {e}")

# Initialize bot
bot = DiscordBot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")
    # Manually run setup logic if not already run
    if not bot.loaded_commands or not bot.loaded_events:
        print("[Manual] Running setup_hook, load_commands, and load_events...")
        try:
            await bot.setup_hook()
        except Exception as e:
            print(f"Error during setup: {e}")
    print(f"Loaded {len(bot.loaded_commands)} commands and {len(bot.loaded_events)} events")
    print("=" * 50)

# Run the bot
if __name__ == "__main__":
    try:
        token = os.getenv('TOKEN')
        if not token:
            print("ERROR: No TOKEN found in environment variables!")
            print("Please create a .env file with your Discord bot token.")
            exit(1)
        bot.run(token)
    except Exception as e:
        print(f"Failed to start bot: {e}")
