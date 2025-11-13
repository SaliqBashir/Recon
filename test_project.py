import pytest
import project

@pytest.fixture
def bot_instance():
    """Create an instance of the bot for testing."""
    return project.DiscordBot()

def test_bot_class_exists():
    """Ensure the DiscordBot class exists."""
    assert hasattr(project, "DiscordBot"), "DiscordBot class not found in project.py"

def test_bot_instance_type(bot_instance):
    """Check if bot_instance is a subclass of discord.Bot."""
    from discord import Bot
    assert isinstance(bot_instance, Bot), "bot_instance should be an instance of discord.Bot"

def test_load_commands_exists():
    """Ensure load_commands() method exists."""
    assert hasattr(project.DiscordBot, "load_commands"), "DiscordBot missing load_commands()"

def test_load_events_exists():
    """Ensure load_events() method exists."""
    assert hasattr(project.DiscordBot, "load_events"), "DiscordBot missing load_events()"

def test_reload_methods_exist():
    """Ensure reload methods exist."""
    assert hasattr(project.DiscordBot, "reload_commands")
    assert hasattr(project.DiscordBot, "reload_events")

def test_main_function_exists():
    """Ensure main() function exists."""
    assert hasattr(project, "main"), "main() function missing in project.py"

def test_bot_attributes(bot_instance):
    """Ensure bot has expected tracking sets."""
    assert hasattr(bot_instance, "loaded_commands")
    assert hasattr(bot_instance, "loaded_events")
    assert isinstance(bot_instance.loaded_commands, set)
    assert isinstance(bot_instance.loaded_events, set)
