from Zaid import app, API_ID, API_HASH
from config import OWNER_ID, ALIVE_PIC
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

PHONE_NUMBER_TEXT = (
    "✘ Heya My Master👋!\n\n"
    "✘ I'm Your Assistant\n\n"
    "‣ I can help you to host Your Left Clients.\n\n"
    "‣ Repo: github.com/Itz-Zaid/Zaid-Userbot\n\n"
    "‣ Now use /clone <Pyrogram Session String>"
)

# ==============================
# START COMMAND (PUBLIC)
# ==============================
@app.on_message(filters.command("start"))
async def start_handler(client, message: Message):
    buttons = [
        [InlineKeyboardButton("✘ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ", url="https://t.me/TheUpdatesChannel")],
        [InlineKeyboardButton("✘ ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ", url="https://t.me/TheSupportChat")]
    ]

    await message.reply_photo(
        photo=ALIVE_PIC,
        caption=PHONE_NUMBER_TEXT,
        reply_markup=InlineKeyboardMarkup(buttons)
    )

# ==============================
# CLONE COMMAND (OWNER ONLY)
# ==============================
@app.on_message(filters.command("clone") & filters.user(OWNER_ID))
async def clone_handler(client, message: Message):
    if len(message.command) < 2:
        return await message.reply(
            "❌ **Usage:**\n\n`/clone <pyrogram_session_string>`"
        )

    session_string = message.command[1]
    status = await message.reply("⚙️ Booting your client...")

    try:
        user_client = Client(
            name="ClonedUser",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=session_string,
            plugins=dict(root="Zaid/modules")
        )

        await user_client.start()
        me = await user_client.get_me()

        await status.edit(
            f"✅ **Client started successfully!**\n\n"
            f"👤 **User:** {me.first_name}\n"
            f"🆔 **ID:** `{me.id}`"
        )

    except Exception as e:
        await status.edit(f"❌ **ERROR:** `{e}`")

# ==============================
# BLOCK NON-OWNER FROM /clone
# ==============================
@app.on_message(filters.command("clone"))
async def clone_blocker(_, message: Message):
    await message.reply("🚫 This command is **OWNER only**.")
