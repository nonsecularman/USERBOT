#!/usr/bin/env bash
python - << 'EOF'
import asyncio
from main import bot  # the bot instance

async def main():
    await bot.start()
    print("✅ BOT STARTED")
    await bot.run_until_disconnected()

asyncio.run(main())
EOF
