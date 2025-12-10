import asyncio
import time
from datetime import datetime
from aiohttp import ClientSession
from pyrogram import Client

from config import (
    API_ID,
    API_HASH,
    SUDO_USERS,
    OWNER_ID,
    BOT_TOKEN,
    STRING_SESSION1,
    STRING_SESSION2,
    STRING_SESSION3,
    STRING_SESSION4,
    STRING_SESSION5,
    STRING_SESSION6,
    STRING_SESSION7,
    STRING_SESSION8,
    STRING_SESSION9,
    STRING_SESSION10
)

# ───────────────────────────────────────────────
# SAFE ASYNC CLIENTSESSION CREATION
# ───────────────────────────────────────────────
aiosession = None

async def init_session():
    global aiosession
    aiosession = ClientSession()

asyncio.get_event_loop().create_task(init_session())

# ───────────────────────────────────────────────
# GLOBALS
# ───────────────────────────────────────────────
StartTime = time.time()
START_TIME = datetime.now()

CMD_HELP = {}
clients = []
ids = []

# Add owner to SUDO
SUDO_USERS.append(OWNER_ID)

# ───────────────────────────────────────────────
# API FAIL-SAFE
# ───────────────────────────────────────────────
if not API_ID:
    print("WARNING: API ID NOT FOUND USING DEFAULT ⚡")
    API_ID = 6435225

if not API_HASH:
    print("WARNING: API HASH NOT FOUND USING DEFAULT ⚡")
    API_HASH = "4e984ea35f854762dcde906dce426c2d"

if not BOT_TOKEN:
    print("WARNING: BOT TOKEN NOT FOUND ⚡")

# ───────────────────────────────────────────────
# MAIN BOT CLIENT
# ───────────────────────────────────────────────
app = Client(
    name="app",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Zaid/modules/bot"),
    in_memory=True,
)

# ───────────────────────────────────────────────
# USER CLIENTS LOADING
# ───────────────────────────────────────────────
def add_client(name, session):
    client = Client(
        name=name,
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=session,
        plugins=dict(root="Zaid/modules")
    )
    clients.append(client)

# 10 STRING SESSIONS
if STRING_SESSION1:
    print("Client1 Starting… 📳")
    add_client("one", STRING_SESSION1)

if STRING_SESSION2:
    print("Client2 Starting… 📳")
    add_client("two", STRING_SESSION2)

if STRING_SESSION3:
    print("Client3 Starting… 📳")
    add_client("three", STRING_SESSION3)

if STRING_SESSION4:
    print("Client4 Starting… 📳")
    add_client("four", STRING_SESSION4)

if STRING_SESSION5:
    print("Client5 Starting… 📳")
    add_client("five", STRING_SESSION5)

if STRING_SESSION6:
    print("Client6 Starting… 📳")
    add_client("six", STRING_SESSION6)

if STRING_SESSION7:
    print("Client7 Starting… 📳")
    add_client("seven", STRING_SESSION7)

if STRING_SESSION8:
    print("Client8 Starting… 📳")
    add_client("eight", STRING_SESSION8)

if STRING_SESSION9:
    print("Client9 Starting… 📳")
    add_client("nine", STRING_SESSION9)

if STRING_SESSION10:
    print("Client10 Starting… 📳")
    add_client("ten", STRING_SESSION10)
