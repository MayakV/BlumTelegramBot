import sqlite3
import os
from pathlib import Path
import datetime


def log_event(cursor,
              session_name: str,
              _type: str,
              status: str,
              message: str,
              data: str):
    cursor.execute(f'''
        INSERT INTO events (session_name, type, status, message, data, date_inserted
         VALUES {session_name}, {_type}, {status}, {message}, {data}, {datetime.datetime.now()}
    ''')


def add_user(cursor,
             session_name: str,
             blum_username: str = "",
             user_agent: str = ""):
    cursor.execute(f'''
            INSERT INTO users (session_name, blum_username, user_agent, last_login_date, date_inserted
             VALUES {session_name}, {blum_username}, {user_agent}, NULL, {datetime.datetime.now()}
        ''')


def update_user(cursor,
                session_name: str,
                blum_username: str = "",
                user_agent: str = "",
                next_login_date: datetime = None,
                last_login_date: datetime.datetime = None):
    updated_fields = []
    if blum_username:
        updated_fields.append(('blum_username', blum_username))
    if user_agent:
        updated_fields.append(('user_agent', user_agent))
    if last_login_date:
        updated_fields.append(('last_login_date', last_login_date))
    if next_login_date:
        updated_fields.append(('next_login_date', next_login_date))
    if updated_fields:
        update_clause = ', '.join([f"{x[0]} = {x[1]}" for x in updated_fields])
        cursor.execute(f'''
                UPDATE users SET {update_clause}
                 WHERE session_name = {session_name}
            ''')


def get_users(cursor,
              sessions: list[str] = None,
              due_to_login=True):
    cursor.execute(f'''
            SELECT session_name, blum_username, user_agent, last_login_date, date_inserted
            FROM users
            WHERE next_login_date < {1}
        ''')
