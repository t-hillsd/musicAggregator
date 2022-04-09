import json
from pathlib import Path
from typing import List

from loguru import logger
from pydantic import BaseModel


class Config(BaseModel):
    __conf = None

    VERSION: str
    REDDIT_ID: str
    REDDIT_SECRET: str
    REDDIT_USER: str
    REDDIT_PASS: str
    MULTIREDDITS: List
    WANTED_URLS: List
    TARGET_SUBREDDIT: str
    INSTANCE_DIR: Path

    @property
    def USER_AGENT(self) -> str:
        return f"script:musicAggregator:v{self.VERSION} (by /u/thillsd)"

    @classmethod
    def config(cls):
        if cls.__conf is None:  # Read only once, lazy.
            dir = Path(__file__).resolve().absolute().parents[1] / "instance"
            dir.mkdir(exist_ok=True, mode=0o777)

            with (dir / "config.json").open() as f:
                cls.__conf = cls(**json.load(f), INSTANCE_DIR=dir)

            logger.debug(cls.__conf)
        return cls.__conf
