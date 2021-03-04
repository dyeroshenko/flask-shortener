import sqlite3

class Database:
    def __init__(self, db: str):
        self.db = db

    def __enter__(self):
        self.connector = sqlite3.connect(self.db)
        self.cursor = self.connector.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_trace):
        self.connector.commit()
        self.connector.close()
