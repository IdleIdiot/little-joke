from typing import Dict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    project_name: str = "Joke"
    api_version: str = "v1"

    api_host: str = "0.0.0.0"
    api_port: int = 80

    debug_mode: bool = True

    database: Dict[str, Dict[str, str]] = {
        "mariadb": {
            "db": "joke",
            "host": "127.0.0.1",
            "port": "3306",
            "username": "root",
            "passwd": "Amazing0534",
        }
    }

    database_url: str = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
        database["mariadb"]["username"],
        database["mariadb"]["passwd"],
        database["mariadb"]["host"],
        database["mariadb"]["port"],
        database["mariadb"]["db"],
    )

    # class Config:
    #     env_file = ".env"


settings = Settings()
