import json
from pathlib import Path

from black import JSONDecodeError

assemblies_path = Path("/Users/charles/working/MY_CECIL/assemblies")


def load_assemblies() -> dict:
    assemblies = {}

    for assembly in assemblies_path.glob("*.json"):
        try:
            with open(assembly.as_posix(), mode="rb") as fp:
                data = json.load(fp)
            assemblies.update(data)
        except JSONDecodeError:
            print(f"error trying to load {assembly.as_posix()}")

    return assemblies


if __name__ == "__main__":
    from pprint import pprint as pp

    asses = load_assemblies()
    pp(asses)
    print(f"# of asses: {len(asses)}")
