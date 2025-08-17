import sqlalchemy.exc
from sqlmodel import SQLModel, Field, create_engine, Session


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None


sql_db_name = "database.db"
engine = create_engine(f"sqlite:///{sql_db_name}", echo=True)

SQLModel.metadata.create_all(engine)

spider_man = Hero(name="Spider-Man", secret_name="Peter Parker", age=16)
ant_man = Hero(name="Ant-Man", secret_name="Scott Lang", age=46)

session = Session(engine)
session.add(spider_man)
session.add(ant_man)

try:
    session.commit()
except sqlalchemy.exc.IntegrityError:
    print("ran into trouble; found a duplicate")
