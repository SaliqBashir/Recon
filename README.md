# 🤖 Recon - Advanced Discord Bot Framework

> A feature-rich, modular Discord bot built with Python for server management, automation, and user engagement.

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://python.org)
[![Discord.py](https://img.shields.io/badge/discord.py-2.0+-5865F2.svg)](https://discordpy.readthedocs.io)
[![Async](https://img.shields.io/badge/Async-Enabled-green.svg)](https://docs.python.org/3/library/asyncio.html)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🚀 Overview

Recon is a comprehensive Discord bot framework designed for modern server management and automation. Built with Python 3.12 and discord.py, it features a modular command structure, event handling system, and extensive server management capabilities. The bot is optimized for performance, scalability, and ease of customization.

## ✨ Key Features

- **🎮 Modular Command System**: Organized command structure with easy extensibility
- **📊 Server Management**: Bot management, user tracking, and server information tools
- **🔔 Event Handling**: Custom event system for real-time server monitoring
- **⚙️ Configuration Management**: Centralized settings and environment configuration
- **🎯 User Interaction**: Ping, echo, and user info utilities
- **📝 Template System**: Pre-built command and event templates for rapid development
- **🎨 Rich Embeds**: Professional message formatting with Discord embeds
- **📈 Kickban System**: Advanced moderation and user management
- **🗂️ Database Integration**: Persistent data storage with SQLite/PostgreSQL support
- **🔒 Security**: Environment variable management and secure configuration

## 🛠️ Technical Stack

### Core Technologies
- **Language**: Python 3.12+
- **Framework**: discord.py 2.0+ (Async/Await)
- **Database**: SQLite (upgradeable to PostgreSQL)
- **Configuration**: python-dotenv for environment management
- **Virtual Environment**: venv for dependency isolation

### Key Libraries & Dependencies
- `discord.py` - Discord API wrapper
- `python-dotenv` - Environment variable management
- `asyncio` - Asynchronous I/O operations
- `aiohttp` - Async HTTP client/server
- Additional dependencies in `requirements.txt`

### Architecture
- **Pattern**: Command-Event driven architecture
- **Structure**: Modular cog-based design
- **Scalability**: Horizontal scaling ready
- **Performance**: Async operations for non-blocking execution

## 📋 System Requirements

- Python 3.12+
- pip (Python package manager)
- Discord Bot Token
- 512MB+ RAM recommended
- Linux/Windows/macOS compatible

## 🏗️ Project Structure

```
Recon/
├── commands/                 # Command modules (Cogs)
│   ├── botmanagement.py     # Bot control and management
│   ├── echo.py              # Message echo functionality
│   ├── kickban.py           # Moderation commands
│   ├── ping.py              # Latency checking
│   ├── rapsheet.py          # User history tracking
│   ├── serverinfo.py        # Server information display
│   ├── settings.py          # Bot configuration commands
│   ├── userinfo.py          # User profile information
│   ├── warn.py              # Warning system
│   └── template_command.py  # Command template for new features
│
├── events/                   # Event handlers
│   ├── modlog.py            # Moderation logging
│   ├── welcome.py           # Member welcome messages
│   └── _template_events.py  # Event template
│
├── app.py                    # Main bot application
├── db.py                     # Database operations and models
├── pyenv.cfg                 # Python environment configuration
├── requirements.txt          # Python dependencies
├── .env.example             # Environment variables template
└── README.md                # Project documentation
```

## 🔧 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/SaliqBashir/Recon.git
cd Recon
```

### 2. Set Up Virtual Environment
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On Linux/Mac:
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
```bash
# Copy example environment file
cp .env.example .env

# Edit .env with your credentials
# Required: DISCORD_TOKEN, DATABASE_URL (optional)
```

### 5. Initialize Database
```bash
python db.py
```

### 6. Run the Bot
```bash
python app.py
```

## 📚 Command Modules

### Bot Management
- Bot status control
- Restart and shutdown commands
- System information

### Moderation
- `/kick` - Remove members from server
- `/ban` - Ban users with reason logging
- `/warn` - Issue warnings to users
- `/rapsheet` - View user moderation history

### Information
- `/ping` - Check bot latency
- `/serverinfo` - Display server statistics
- `/userinfo` - Show user profile details

### Utility
- `/echo` - Repeat messages
- `/settings` - Configure bot behavior

## 🎯 Event Handlers

- **Welcome System**: Automated member greeting
- **Moderation Logging**: Track all moderation actions
- **Custom Events**: Extensible event system

## 🔐 Security Features

- **Environment Variables**: Secure token and API key storage
- **Permission Checks**: Role-based command access
- **Input Validation**: Sanitized user inputs
- **Rate Limiting**: Prevent command spam
- **Audit Logging**: Complete action history

## 📊 Database Schema

### Core Tables
- **Users**: Member profiles and statistics
- **Moderation**: Warnings, kicks, and bans
- **Settings**: Server-specific configurations
- **Logs**: Action and event history

## 🚀 Extending the Bot

### Adding New Commands
1. Use `template_command.py` as a starting point
2. Create new file in `commands/` directory
3. Implement command logic with decorators
4. Load cog in `app.py`

### Adding New Events
1. Use `_template_events.py` as reference
2. Create new file in `events/` directory
3. Implement event listeners
4. Register events in main application

## 💡 Technical Highlights for Recruiters

- **Asynchronous Programming**: Expert use of Python async/await patterns
- **API Integration**: Discord API implementation with discord.py
- **Database Management**: ORM patterns and efficient query design
- **Modular Architecture**: Scalable, maintainable cog-based structure
- **Event-Driven Design**: Real-time event handling and processing
- **Error Handling**: Comprehensive exception management
- **Code Organization**: Clean separation of concerns
- **Version Control**: Git workflow and best practices
- **Documentation**: Well-commented code and clear structure
- **DevOps Ready**: Environment-based configuration

## 🎨 Bot Features

- **Slash Commands**: Modern Discord interaction support
- **Embed Messages**: Rich, formatted responses
- **Button Interactions**: Interactive UI components
- **Modal Forms**: Advanced user input collection
- **Auto-complete**: Smart command suggestions
- **Cooldowns**: Rate limiting and spam prevention

## 📈 Performance Optimization

- **Async Operations**: Non-blocking I/O for maximum efficiency
- **Connection Pooling**: Optimized database connections
- **Caching**: Reduced API calls with intelligent caching
- **Lazy Loading**: Commands loaded on-demand
- **Memory Management**: Efficient resource utilization

## 🔄 Future Enhancements

- [ ] Dashboard web interface
- [ ] Advanced analytics and statistics
- [ ] Multi-language support
- [ ] Custom command creation (no-code)
- [ ] Integration with external APIs
- [ ] Music playback functionality
- [ ] Ticket system for support
- [ ] Economy and leveling system
- [ ] Automated moderation with AI
- [ ] Docker containerization

## 🛠️ Development Tools

- **Linting**: PEP 8 compliant code
- **Type Hints**: Enhanced code clarity
- **Virtual Environment**: Isolated dependencies
- **Git**: Version control and collaboration

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Contact

For any questions or suggestions, please reach out through GitHub issues or connect with me on LinkedIn.

---