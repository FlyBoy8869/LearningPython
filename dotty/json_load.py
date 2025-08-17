import json
from collections import namedtuple

CONFIG_FILE = "Korean Spring Motor.json"


def make_me_a_namespace(data): ...


with open(CONFIG_FILE, "r") as infile:
    assembly_data = json.load(infile)

Drawing = namedtuple("Drawing", sorted(assembly_data["drawings"][0]))
drawing = Drawing(**assembly_data["drawings"][0])

for drawing in assembly_data["drawings"]:
    info = Drawing(**drawing)
    print(f"{info.number=}")
