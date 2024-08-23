import json

import bot.utils.console_logger as logger


def load_user_data(session_name = "MASTER"):
    user_data_file_name = "blum_user_data.json"
    try:
        with open(user_data_file_name, 'r') as user_data:
            session_data = json.load(user_data)
            if isinstance(session_data, list):
                return session_data

    except FileNotFoundError:
        logger.warning(session_name, "Blum user data file not found, creating...")

    except json.JSONDecodeError:
        logger.warning(session_name, "Blum user data file is empty or corrupted.")

    return []


async def save_blum_username(session_name, username):
    user_agents_file_name = "blum_user_data.json"
    blum_user_data = load_user_data()

    if not any(session['session_name'] == session_name for session in blum_user_data):
        blum_user_data.append({"session_name": session_name, "blum_username": username})
        # raise ValueError(f"No Blum data found for session {self.session_name}")
    else:
        def update_username(user_data, session_name, new_username):
            if user_data["session_name"] == session_name:
                user_data["blum_username"] = new_username
            return user_data

        blum_user_data = [update_username(x, session_name, username) for x in blum_user_data]

    with open(user_agents_file_name, 'w') as user_data:
        json.dump(blum_user_data, user_data, indent=4)

        logger.success(session_name, "Blum user data saved successfully")


async def save_proxy(session_name, proxy):
    user_agents_file_name = "blum_user_data.json"
    blum_user_data = load_user_data()

    if not any(session['session_name'] == session_name for session in blum_user_data):
        blum_user_data.append({"session_name": session_name, "proxy": proxy})
        # raise ValueError(f"No Blum data found for session {self.session_name}")
    else:
        def update_username(user_data, session_name, new_proxy):
            if user_data["session_name"] == session_name:
                user_data["proxy"] = new_proxy
            return user_data

        blum_user_data = [update_username(x, session_name, proxy) for x in blum_user_data]

    with open(user_agents_file_name, 'w') as user_data:
        json.dump(blum_user_data, user_data, indent=4)

        # logger.success(session_name, "Blum user data saved successfully")

