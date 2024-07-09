import psycopg2


class Connection():
    def __init__(self):
        self.conn = psycopg2.connect(
            database = 'postgres',
            user = 'postgres',
            password = '2894',
            host = 'localhost', 
            port = '5432'
        )

    def close_database(self):
        self.conn.close()
    
    def get_connection(self):
        return self.conn

    def create_database (self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS coins(
                       id SERIAL PRIMARY KEY,
                       moeda TEXT NOT NULL,
                       cotação REAL NOT NULL,
                       ultima_att TIME NOT NULL,
                       data DATE NOT NULL
                       )
                        """)
        self.conn.commit()
        
    def insert_coin(self, moeda, cotacao, data,data2):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO coins (moeda, cotação, ultima_att,data) VALUES (%s,%s,%s,%s)
                        """, (moeda,cotacao,data,data2))
        self.conn.commit()
    

if __name__ == "__main__":
    db = Connection()
    db.create_database()
    db.close_database()