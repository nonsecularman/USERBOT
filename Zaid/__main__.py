import asyncio
import importlib
from pyrogram import idle
from Zaid import app, clients, ids
from Zaid.modules import ALL_MODULES
from Zaid.helper import join

async def start_bot():
    # 1) Start BOT
    await app.start()
    print("Bot started successfully 🤖")

    # 2) Load modules
    for module in ALL_MODULES:
        importlib.import_module(f"Zaid.modules.{module}")
        print(f"Loaded module: {module}")

    # 3) Start USER clients
    for cli in clients:
        try:
            await cli.start()
            me = await cli.get_me()
            await join(cli)
            ids.append(me.id)
            print(f"User {me.first_name} started 🔥")
        except Exception as e:
            print(f"User start error: {e}")

    await idle()

if __name__ == "__main__":
    asyncio.run(start_bot())
