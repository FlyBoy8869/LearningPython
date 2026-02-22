from pathlib import Path

from tinydb import TinyDB, where

_db_path: Path = Path(__file__).parent / "assemblies_db.json"
db = TinyDB(_db_path.resolve().as_posix(), indent=4)
sources_table = db.table(name="sources")

_source_dict: dict[str, str] = {
    "source": "",
}


def add_source(source: str) -> None:
    d: dict[str, str] = _source_dict.copy()
    d["source"] = source
    sources_table.insert(d)


def source_exists(source: str) -> bool:
    return bool(sources_table.search(where("source") == source))


def close() -> None:
    db.close()
