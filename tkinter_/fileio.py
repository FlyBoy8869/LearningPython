import json
import shutil
from pathlib import Path

from black import JSONDecodeError

assemblies_path = Path("./assemblies")
document_locations = [
    r"/Users/charles/working/MY_CECIL/test docs/Japanese Documents/101249_DCIT",
    r"/Users/charles/working/MY_CECIL/test docs/Japanese Documents/cecil",
    r"/Users/charles/working/MY_CECIL/test docs/Japanese Documents/documents",
    r"/Users/charles/working/MY_CECIL/test docs/Korean Docs/documents",
    r"/Users/charles/working/MY_CECIL/test docs/Korean Docs/Released Documents",
]


def load_assembly_files() -> dict:
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
        if document in p.name:
            paths.append(p)

    return paths


def load_paths():
    paths = []
    for p in document_locations:
        path = Path(p)
        docs = path.glob("*.pdf")
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
