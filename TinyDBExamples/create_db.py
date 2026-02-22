from csv import DictReader
from pathlib import Path

from tinydb import TinyDB

this_folder = Path(__file__).parent

with TinyDB(this_folder / "countries.json", indent=4) as countries_db:
    countries_table = countries_db.table(name="countries")

    countries_table.insert(
        {"location": "Vatican City", "population": 503},
    )

    countries_table.insert_multiple(
        [
            {"location": "India", "population": 1_417_492_000},
            {"location": "China", "population": 1_408_280_000},
        ],
    )

    with (this_folder / "countries_file.csv").open(mode="r", encoding="utf-8") as csv_source:
        reader = DictReader(csv_source)

        for row in reader:
            row["population"] = int(row["population"])
            countries_table.insert(row)
