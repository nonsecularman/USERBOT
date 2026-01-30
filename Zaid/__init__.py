import time
from datetime import datetime
from pyrogram import Client
from aiohttp import ClientSession

from config import (
    API_ID, API_HASH, BOT_TOKEN, OWNER_ID, SUDO_USERS,
    STRING_SESSION1, STRING_SESSION2, STRING_SESSION3, STRING_SESSION4,
    STRING_SESSION5, STRING_SESSION6, STRING_SESSION7, STRING_SESSION8,
    STRING_SESSION9, STRING_SESSION10,
)

# ── GLOBALS ─────────────────────────────
StartTime = time.time()
START_TIME = datetime.now()
CMD_HELP = {}
clients = []
ids = []

if OWNER_ID not in SUDO_USERS:
    SUDO_USERS.append(OWNER_ID)

# Backward compatibility
SUDO_USER = SUDO_USERS

# ── BOT CLIENT (BOT TOKEN ONLY) ─────────
app = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Zaid/modules/bot"),
)

# ── USER CLIENTS (STRING SESSIONS ONLY) ──
def add_client(name, session):
    clients.append(
        Client(
            name=name,
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=session,
            plugins=dict(root="Zaid/modules"),
        )
    )

if STRING_SESSION1: add_client("user1", STRING_SESSION1)
if STRING_SESSION2: add_client("user2", STRING_SESSION2)
if STRING_SESSION3: add_client("user3", STRING_SESSION3)
if STRING_SESSION4: add_client("user4", STRING_SESSION4)
if STRING_SESSION5: add_client("user5", STRING_SESSION5)
if STRING_SESSION6: add_client("user6", STRING_SESSION6)
if STRING_SESSION7: add_client("user7", STRING_SESSION7)
if STRING_SESSION8: add_client("user8", STRING_SESSION8)
if STRING_SESSION9: add_client("user9", STRING_SESSION9)
if STRING_SESSION10: add_client("user10", STRING_SESSION10)

# ── AIOHTTP SESSION (SAFE INIT) ─────────
aiosession: ClientSession | None = None

async def init_aiosession():
    global aiosession
    if aiosession is None or aiosession.closed:
        aiosession = ClientSession()

__all__ = [
    "app", "clients", "ids", "CMD_HELP",
    "StartTime", "START_TIME",
    "SUDO_USERS", "SUDO_USER",
    "aiosession", "init_aiosession",
]
