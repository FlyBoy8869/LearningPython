from pathlib import Path
from pprint import pprint
from typing import NamedTuple

from tinydb import Query, TinyDB
from tinydb.queries import where


class Document(NamedTuple):
    nomenclature: str
    partNumber: str  # noqa: N815
    documents: list


def contains_string(value, search_term) -> bool:
    return search_term in value


db_path: Path = Path(__file__).parent / "cecil_assemblies.json"
print(str(db_path))

db = TinyDB(str(db_path))
query = Query()
assemblies= db.table(name="assemblies")

# pprint(assemblies.all())

# for document in assemblies.all():
#     doc = Document(**document)
#     print(f"{doc.nomenclature} uses the following documents:")
#     for key in doc.documents:
#         print(f"{key}")

# document = assemblies.search(query.nomenclature.test(contains_string, "Japanese Control Area Interface Unit"))
result = assemblies.search(where("nomenclature").search("Japanese Control Area Interface Unit"))
# result = assemblies.get(where("nomenclature") == "Japanese Control Area Interface Unit")
document = Document(**result[0])
print(document.partNumber)

db.close()
