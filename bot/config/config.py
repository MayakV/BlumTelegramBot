from pydantic_settings import BaseSettings, SettingsConfigDict
from datetime import time, timedelta


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int
    API_HASH: str

    PLAY_GAMES: bool = True
    POINTS: list[int] = [190, 230]

    USE_REF: bool = False
    REF_ID: str = ''

    USE_PROXY_FROM_FILE: bool = False

    BED_TIME: time = time(1)
    WAKE_UP_TIME: time = time(10)
    START_DELAY: timedelta = timedelta(hours=1)


settings = Settings()


