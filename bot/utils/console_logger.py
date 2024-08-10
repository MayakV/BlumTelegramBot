import sys
from loguru import logger


logger.remove()
logger.add(sink=sys.stdout, format="<white>{time:YYYY-MM-DD HH:mm:ss}</white>"
                                   " | <level>{level}</level>"
                                   " | <white><b>{message}</b></white>")
logger = logger.opt(colors=True)


def info(session_name, text, data=""):
    return logger.info(f"<light-yellow>{session_name}</light-yellow> | " + text + f" | {data}")


def debug(session_name, text, data=""):
    return logger.debug(f"<light-yellow>{session_name}</light-yellow> | " + text + f" | {data}")


def warning(session_name, text, data=""):
    return logger.warning(f"<light-yellow>{session_name}</light-yellow> | " + text + f" | {data}")


def error(session_name, text, data=""):
    return logger.error(f"<light-yellow>{session_name}</light-yellow> | " + text + f" | {data}")


def critical(session_name, text, data=""):
    return logger.critical(f"<light-yellow>{session_name}</light-yellow> | " + text + f" | {data}")


def success(session_name, text, data=""):
    return logger.success(f"<light-yellow>{session_name}</light-yellow> | " + text + f" | {data}")

