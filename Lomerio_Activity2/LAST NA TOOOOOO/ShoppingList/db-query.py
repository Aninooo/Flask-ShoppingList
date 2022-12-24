import sqlite3

db_locale = 'items.db'

con = sqlite3.connect(db_locale)
c = con.cursor()

c.execute("""
SELECT * FROM products
""")

items = c.fetchall()
for item in items:
    print(item)


con.commit()
con.close()