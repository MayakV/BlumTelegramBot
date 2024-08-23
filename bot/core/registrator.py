from pyrogram import Client
import json

from bot.config import settings
import bot.utils.console_logger as logger
import bot.core.user_data as ud


async def register_sessions() -> None:
    API_ID = settings.API_ID
    API_HASH = settings.API_HASH

    if not API_ID or not API_HASH:
        raise ValueError("API_ID and API_HASH not found in the .env file.")

    session_name = input('\nEnter the session name (press Enter to exit): ')
    blum_username = input('Enter the Blum username (press Enter if not registered in Blum): ')
    proxy = input("Enter proxy (format: type://ip:port@user:pass): ")

    if not session_name:
        return None

    if blum_username:
        await ud.save_blum_username(session_name, blum_username)

    if proxy:
        await ud.save_proxy(session_name, proxy)

    session = Client(
        name=session_name,
        api_id=API_ID,
        api_hash=API_HASH,
        workdir="sessions/"
    )

    async with session:
        user_data = await session.get_me()

    logger.success("MASTER",
                   f'Session added successfully @{user_data.username} | {user_data.first_name} {user_data.last_name}')
