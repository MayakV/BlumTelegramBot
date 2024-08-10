import sys
from loguru import logger
from pathlib import Path
import os
import db.db_api as db

#
# logger.remove()
# logger.add(sink=sys.stdout, format="<white>{time:YYYY-MM-DD HH:mm:ss}</white>"
#                                    " | <level>{level}</level>"
#                                    " | <white><b>{message}</b></white>")
# logger = logger.opt(colors=True)

import sqlite3

conn = sqlite3.connect(Path(os.getenv("DB_PATH")) / os.getenv("DB_NAME"))
cursor = conn.cursor()


def info(session_name, text, data):
    db.log_event(cursor, session_name, 'Info', "", text, data)


def debug(session_name, text, data):
    db.log_event(cursor, session_name, 'Debug', "", text, data)


def warning(session_name, text, data):
    db.log_event(cursor, session_name, 'Warning', "", text, data)


def error(session_name, text, data):
    db.log_event(cursor, session_name, 'Error', "Failed", text, data)


def critical(session_name, text, data):
    db.log_event(cursor, session_name, 'Critical Error', "Failed", text, data)


def success(session_name, text, data):
    db.log_event(cursor, session_name, 'Critical Error', "Failed", text, data)
# def info(text):
#     return logger.info(text)
#
#
# def debug(text):
#     return logger.debug(text)
#
#
# def warning(text):
#     return logger.warning(text)
#
#
# def error(text):
#     return logger.error(text)
#

# def critical(text):
#     return logger.critical(text)
#
#
# def success(text):
#     return logger.success(text)
