import os
import motor.motor_asyncio

MONGO_URI = os.getenv("MONGO_URI") or "mongodb://localhost:27017"
DB_NAME = os.getenv("MONGO_DB") or "discordbot"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]

def get_guild_settings_collection():
    return db.guild_settings

def get_mod_logs_collection():
    return db.mod_logs
