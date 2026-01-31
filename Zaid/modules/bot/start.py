from Zaid import app
from pyrogram import filters

@app.on_message(filters.command("start"))
async def start_handler(client, message):
    await message.reply_text("✅ Bot zinda hai bhai 🔥")
