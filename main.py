import misc
import handlers
import asyncio
import logging


async def main():
    await misc.bot.delete_webhook(drop_pending_updates=True)
    await misc.dp.start_polling(misc.bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())