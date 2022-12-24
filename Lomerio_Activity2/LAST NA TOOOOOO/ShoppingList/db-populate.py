import sqlite3

db_locale = 'items.db'

con = sqlite3.connect(db_locale)
c = con.cursor()

c.execute("""
INSERT INTO  products (item_name, item_quantity ) VALUES
('banane', '1'),
('cartofi', '3'),
('suc', '5')

""")

con.commit()
con.close()
