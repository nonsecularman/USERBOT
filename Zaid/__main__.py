import asyncio
import importlib
from pyrogram import idle
from Zaid.helper import join
from Zaid.modules import ALL_MODULES
from Zaid import clients, app, ids

async def start_bot():
    await app.start()
    print("LOG: Founded Bot token Booting..")

    for module in ALL_MODULES:
        importlib.import_module(f"Zaid.modules.{module}")
        print(f"Successfully Imported {module} 💥")

    for cli in clients:
        try:
            await cli.start()
            ex = await cli.get_me()
            await join(cli)
            print(f"Started {ex.first_name} 🔥")
            ids.append(ex.id)
        except Exception as e:
            print(e)

    await idle()

if __name__ == "__main__":
    asyncio.run(start_bot())
