import sqlite3

class Database:
    def __init__(self, db_file='invoices.db'):
        self.conn = sqlite3.connect(db_file)
        self.create_tables()

    def create_tables(self):
        c = self.conn.cursor()
        c.execute("""
          CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            email TEXT
          )
        """)
        c.execute("""
          CREATE TABLE IF NOT EXISTS invoices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            invoice_id TEXT UNIQUE NOT NULL,
            client TEXT NOT NULL,
            date TEXT NOT NULL,
            total REAL NOT NULL,
            status TEXT NOT NULL
          )
        """)
        self.conn.commit()

    def fetch_invoices(self):
        c = self.conn.cursor()
        c.execute("SELECT invoice_id, client, date, total, status FROM invoices")
        return c.fetchall()

    def insert_invoice(self, invoice_id, client, date, total, status):
        c = self.conn.cursor()
        c.execute("INSERT INTO invoices (invoice_id, client, date, total, status) VALUES (?, ?, ?, ?, ?)",
                  (invoice_id, client, date, total, status))
        self.conn.commit()

    # Add additional methods for update, delete, search...
