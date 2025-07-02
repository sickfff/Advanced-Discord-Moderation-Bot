"""
utils.py
========
Utility functions for the AI-powered Discord Moderation Bot.

Author: Gabriel Roriz Silva
License: MIT License
"""

import discord
from discord.ext import commands
import json
import logging
import os
from datetime import datetime

# Set up logger
logger = logging.getLogger("moderation_bot")
logger.setLevel(logging.INFO)

# File handler for logs
if not os.path.exists("logs"):
    os.makedirs("logs")
log_file = logging.FileHandler(filename="logs/moderation.log", encoding="utf-8", mode="a")
formatter = logging.Formatter('%(asctime)s:%(levelname)s: %(message)s')
log_file.setFormatter(formatter)
logger.addHandler(log_file)

# Load bot token from config file
def load_config(path="config.json"):
    try:
        with open(path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        logger.error("config.json not found.")
        return {}

# Format user mention and ID
def user_tag(user: discord.User | discord.Member) -> str:
    return f"{user.name}#{user.discriminator} ({user.id})"

# Log moderation actions to file and console
def log_action(action: str, user: discord.User | discord.Member, reason: str = "N/A"):
    message = f"[{action}] {user_tag(user)} | Reason: {reason}"
    logger.info(message)
    print(message)

# Check if user is a moderator
def is_moderator(member: discord.Member) -> bool:
    mod_roles = {"Admin", "Moderator", "Mod"}
    return any(role.name in mod_roles for role in member.roles)

# Get current timestamp
def timestamp() -> str:
    return datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

# Check bot permissions
def has_permissions(ctx: commands.Context, perms: list[str]) -> bool:
    missing = [perm for perm in perms if not getattr(ctx.channel.permissions_for(ctx.me), perm, False)]
    if missing:
        logger.warning(f"Missing permissions: {', '.join(missing)} in channel {ctx.channel}")
        return False
    return True
