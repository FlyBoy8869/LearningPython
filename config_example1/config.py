import tomllib
from pathlib import Path
from typing import NamedTuple

config_file_path = Path(__file__).parent / "config.toml"

with config_file_path.open(mode="rb") as infile:
    _config = tomllib.load(infile)


class _Defaults(NamedTuple):
    name: str
    age: int
    likes: list


class _Server(NamedTuple):
    port: int
    ip: str
    timeout: int


class _Config:
    def __init__(self):
        self.defaults = _Defaults(**_config["defaults"])
        self.server = _Server(**_config["server"])


config = _Config()
