import datetime
import random


def format_duration(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    return f"{hours} hours, {minutes} mins, {remaining_seconds} secs"


def format_date(seconds):
    return datetime.datetime.fromtimestamp(seconds)


def add_random_time(dt: datetime,
                    max_delta: datetime.timedelta):
    return dt + random.random() * max_delta
