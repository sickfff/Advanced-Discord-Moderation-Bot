"""
Advanced Discord Moderation Bot
Author: Gabriel Roriz Silva
"""

import discord
from discord.ext import commands
import json
from cogs.moderation import ModerationCog

intents = discord.Intents.default()
intents.message_content = True  # Required for message content access

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")

async def main():
    # Load config
    with open("config.json") as f:
        config = json.load(f)
    bot.config = config
    
    # Load Cogs
    await bot.add_cog(ModerationCog(bot))

    # Run bot
    await bot.start(config["token"])

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
