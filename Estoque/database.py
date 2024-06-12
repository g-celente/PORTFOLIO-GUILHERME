import sqlite3
import pandas as pd

class Database():
    def __init__(self, name="system.db"):
        self.name = name
        self.conn = None

    def connect(self):
        self.conn = sqlite3.connect(self.name)

    def close_connection(self):
        if self.conn:
            try:
                self.conn.close()
            except:
                pass

    def create_table_users(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                user TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                access TEXT NOT NULL
            );
        """)

    def insert_user(self, name, user, password, access):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO users (name, user, password, access) VALUES (?, ?, ?, ?);
        """, (name, user, password, access))
        self.conn.commit()

    def check_user(self, user, password):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT * FROM users;
        """)
        for linha in cursor.fetchall():
            if linha[2].upper() == user.upper() and linha[3] == password and linha[4] == 'Administrador':
                return "Administrador"
            elif linha[2].upper() == user.upper() and linha[3] == password and linha[4] == 'Usuário':
                return "Usuário"
            else:
                continue
        return "Sem Acesso"


db = Database()
db.connect()
db.create_table_users()
