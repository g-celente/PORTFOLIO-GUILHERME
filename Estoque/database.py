import sqlite3

class Database():
    def __init__(self, name = "system.db"):
        self.name = name
    
    def connection (self):
        self.connection = sqlite3.connect(self.name)
    
    def close_connection (self):
        try:
            self.connection.close()
        except:
            pass
    
    def create_table_users(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users(
                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        user TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL,
                        acess TEXT NOT NULL
                    ); 
                    
            """)
        

if __name__=="__main__":
    db = Database()
    db.connection()
    db.create_table_users()