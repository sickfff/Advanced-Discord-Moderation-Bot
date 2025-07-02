# 🤖 Advanced Discord Moderation Bot 🚨

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://python.org)  
[![Discord](https://img.shields.io/badge/Discord-Bot-purple.svg)](https://discord.com/developers/applications)

---

## Overview

Welcome to the **Advanced Discord Moderation Bot** — a powerful AI-powered moderation assistant designed to keep your Discord server safe and friendly.  
This bot uses state-of-the-art machine learning models to detect toxic messages in real time and helps moderators take action efficiently.

Powered by:  
- **Gabriel Roriz Silva** (Developer)  
- [Detoxify](https://github.com/unitaryai/detoxify) (AI Toxicity Model)  

---

## 🚀 Features

- 🛡️ **Real-time Toxicity Detection** with Detoxify  
- ⚙️ Automated deletion of toxic messages and user warnings  
- 🧹 Message purge command for quick cleanup  
- 📜 Detailed logs for all moderation actions with timestamps  
- 👮‍♂️ Role-based command permissions for moderators only  
- 🔧 Easy to install, configure, and customize  
- 📊 Adjustable toxicity threshold for fine-tuning sensitivity  

---

## 📥 Installation

1. **Clone the repository**  
```bash
git clone https://github.com/yourusername/discord-moderation-bot.git
cd discord-moderation-bot
```

2. **Install dependencies**  
```bash
pip install -r requirements.txt
```

3. **Create your Discord bot** via the [Discord Developer Portal](https://discord.com/developers/applications) and enable the **Message Content Intent**.

4. **Add your bot token** to a `config.json` file at the project root:  
```json
{
  "token": "YOUR_BOT_TOKEN_HERE"
}
```

5. **Run the bot**  
```bash
python bot.py
```

---

## ⚙️ Configuration

- **toxicity_threshold**: Adjust this value in `cogs/moderation.py` to set how sensitive the bot is to toxic content (default: `0.7`).
- Ensure your bot has the necessary permissions and intents enabled in the Discord Developer Portal.

---

## 🤝 Contribution & Credits

Created and maintained by **Gabriel Roriz Silva**.  
Thanks to the [Detoxify](https://github.com/unitaryai/detoxify) team for their powerful AI toxicity detection model.

Feel free to open issues, suggest features, or submit pull requests!

---

## 📜 License

This project is licensed under the MIT License © 2025 Gabriel Roriz Silva.

---

## 📬 Contact

Questions, feedback, or collaboration?  

[Github:](github.com/groriz11)

---

Thank you for supporting open source! Keep your Discord communities safe and positive. ❤️🎉
