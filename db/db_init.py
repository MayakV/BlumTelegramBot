import sqlite3
import os
from pathlib import Path


def create_table_if_not_exists(name: str,
                               fields: dict):
    cursor.execute(f'''
        SELECT name FROM sqlite_master WHERE type='table' AND name='{name}';
    ''')
    result = cursor.fetchone()
    if not result:
        # Keep in mind bot uses indexes to access data fields, so any order change will break the bot
        cursor.execute(f'''
            CREATE TABLE {name}({", ".join([f"{k} {v}" for k, v in fields.items()])});
        ''')
        print(f"Table {name} created.")
    else:
        print(f"Table {name} already exist.")


db_path = Path(os.getenv("DB_PATH")) / os.getenv("DB_NAME")
# db_path = Path(os.getcwd() + "/log.db")
print(db_path)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
create_table_if_not_exists("events", {'id': 'INTEGER PRIMARY KEY',
                                      'session_name': 'TEXT',
                                      'type': 'TEXT',
                                      'status': 'TEXT',
                                      'message': 'TEXT',
                                      'data': 'TEXT',
                                      'date_inserted': 'DATETIME'})
create_table_if_not_exists("users", {'user_id': 'INTEGER PRIMARY KEY',
                                     'session_name': 'TEXT',
                                     'blum_username': 'TEXT',
                                     'user_agent': 'TEXT',
                                     'last_login_date': 'DATETIME',
                                     'date_inserted': 'DATETIME'})
create_table_if_not_exists("proxies", {'id': 'INTEGER PRIMARY KEY',
                                     'proxy_text': 'TEXT',
                                     'date_inserted': 'DATETIME'})
conn.commit()
conn.close()
