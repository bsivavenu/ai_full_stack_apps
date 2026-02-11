# db.py
import sqlite3

conn = sqlite3.connect("invoices.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS invoices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_name TEXT,
    vendor TEXT,
    invoice_number TEXT,
    date TEXT,
    total_amount REAL
)
""")

conn.commit()
conn.close()
