import sqlite3
import os
from pathlib import Path
from app.models import Idea, IdeaRequest

SCHEMA = Path(__file__).parent / "schema.sql"

class IdeaStore:
    def __init__(self, db_path: str = None):
        if db_path is None:
            db_path = os.environ.get("DB_PATH", "ideas.db")
        self._db_path = db_path
        self._setup()

    def _connect(self):
        return sqlite3.connect(self._db_path)

    def _setup(self):
        sql = SCHEMA.read_text()
        with self._connect() as con:
            con.executescript(sql)

    def find_all(self) -> list[Idea]:
        with self._connect() as con:
            rows = con.execute("SELECT id, title, category FROM ideas").fetchall()
        return [Idea(id=row[0], title=row[1], category=row[2]) for row in rows]

    def add(self, request: IdeaRequest) -> Idea:
        with self._connect() as con:
            cur = con.execute(
                "INSERT INTO ideas (title, category) VALUES (?, ?)",
                (request.title, request.category),
            )
            con.commit()
        return Idea(id=cur.lastrowid, title=request.title, category=request.category)
