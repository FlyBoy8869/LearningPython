from pathlib import Path
from typing import TYPE_CHECKING

from tinydb import TinyDB, where

if TYPE_CHECKING:
    from tinydb.table import Table

_db_name: str = "assemblies_db.json"
_db_path: Path = Path(__file__).parent / _db_name

db = TinyDB(_db_path.resolve().as_posix(), indent=4)

assemblies_table: Table = db.table(name="assemblies")
sources_table: Table = db.table(name="sources")


def add_source(source: str) -> None:
    sources_table.insert({"source": source})


def source_exists(source: str) -> bool:
    return bool(sources_table.search(where("source") == source))


def close() -> None:
    db.close()
