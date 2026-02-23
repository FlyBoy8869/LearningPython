from pathlib import Path
from pprint import pprint
from typing import NamedTuple

from tinydb import Query, TinyDB

db_name = "assemblies_db.json"
db_table = "assemblies"

db_path: Path = Path(__file__).parent / db_name
db = TinyDB(db_path.resolve().as_posix())

table = db.table(name="assemblies")
assemblies = Query()


class Assembly(NamedTuple):
    nomenclature: str
    partnumber: str
    documents: list


# documents = table.search(assemblies.partnumber == "1012490210")
# assembly = Assembly(**documents[0])

# print(f"Assembly: {assembly.nomenclature}")
# print(f"Part Number: {assembly.partnumber}")
# pprint(assembly.documents)
# pprint(list(assembly.documents))

# pprint(table.all())

# for assembly in table:
#     print(assembly)

partnumbers = [doc["partnumber"] for doc in table.all()]
pprint(partnumbers)
