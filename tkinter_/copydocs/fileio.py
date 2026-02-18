import json
import shutil
from json import JSONDecodeError
from pathlib import Path

BASE = Path(__file__).parent
assemblies_path = BASE / "assemblies"
document_locations = [
    BASE / "testDocs/Japanese Documents/101249_DCIT",
    BASE / "testDocs/Japanese Documents/cecil",
    BASE / "testDocs/Japanese Documents/documents",
    BASE / "testDocs/Korean Docs/documents",
    BASE / "testDocs/Korean Docs/Released Documents",
]


def load_assembly_files() -> dict:
    # TODO: Evaluate the use of dict instead of list
    assemblies = {}

    for assembly in assemblies_path.glob("*.json"):
        try:
            with open(assembly.as_posix(), mode="rb") as fp:
                data = json.load(fp)
            assemblies.update(data)
        except JSONDecodeError:
            print(f"error trying to load {assembly.as_posix()}")

    return assemblies


def get_document_paths(document):
    paths = []

    for p in _document_paths:
        if document.lower() in p.name.lower():
            paths.append(p)

    return paths


def load_paths():
    paths = []
    for p in document_locations:
        docs = p.glob("*.pdf")
        paths.extend(docs)

    return paths


_document_paths = load_paths()


def copy_files(paths, dest):
    for path in paths:
        if Path(dest, path.name).exists():
            print(f"file exists: {path}, skipping file")
            continue
        print(f"copying {path}")
        shutil.copy(path.as_posix(), dest)
