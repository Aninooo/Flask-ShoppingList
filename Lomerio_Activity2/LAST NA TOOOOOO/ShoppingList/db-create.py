import sqlite3

db_locale = 'items.db'

con = sqlite3.connect(db_locale)
c = con.cursor()

c.execute("""
CREATE TABLE products (id INTEGER PRIMARY KEY AUTOINCREMENT,
item_name TEXT,
item_quantity TEXT)
""")

con.commit()
con.close()
