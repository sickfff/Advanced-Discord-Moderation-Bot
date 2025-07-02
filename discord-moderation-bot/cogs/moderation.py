import discord
from discord.ext import commands
from models.toxicity_model import ToxicityModel
import datetime
import os

class ModerationCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.toxicity_model = ToxicityModel()
        self.log_dir = "data/logs"
        os.makedirs(self.log_dir, exist_ok=True)
        self.toxicity_threshold = 0.7  # Adjust as needed

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user or message.author.bot:
            return
        
        # Run toxicity detection
        toxicity_score = await self.toxicity_model.predict(message.content)
        
        if toxicity_score > self.toxicity_threshold:
            await self.handle_toxic_message(message, toxicity_score)
        else:
            await self.bot.process_commands(message)

    async def handle_toxic_message(self, message, score):
        # Warn user and delete message
        try:
            await message.delete()
            warning_msg = f"⚠️ {message.author.mention}, your message was removed for toxic content (score: {score:.2f}). Please be respectful."
            await message.channel.send(warning_msg)
            await self.log_action(message.author, message.content, score)
        except Exception as e:
            print(f"Failed to moderate message: {e}")

    async def log_action(self, user, content, score):
        filename = f"{self.log_dir}/moderation_log.txt"
        timestamp = datetime.datetime.utcnow().isoformat()
        log_entry = f"{timestamp} | User: {user} | Toxicity Score: {score:.2f} | Message: {content}\n"
        with open(filename, "a", encoding="utf-8") as f:
            f.write(log_entry)

    @commands.command(name="purge")
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, limit: int):
        """Purge messages from channel."""
        deleted = await ctx.channel.purge(limit=limit)
        await ctx.send(f"Deleted {len(deleted)} messages.", delete_after=5)
