import os
from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()
env_file = os.getenv("{{ cookiecutter.package_name|upper }}_ENV_FILE")


class Settings(BaseSettings):
    WORKDIR: Path = Path(__file__).parents[1]
    DATA_DIR: Path = Path(__file__).parents[1].joinpath("data", "mpc_nrr_data")
    DATABASE: Path = Path(__file__).parents[1].joinpath("database")

    model_config = SettingsConfigDict(
        env_prefix="{{ cookiecutter.package_name|upper }}_", env_file=env_file, extra="ignore"
    )
