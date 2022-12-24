from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import time

app = Flask(__name__)
db_local = 'items.db'

@app.route("/home")
def home():
    products_data = query_products()
    return render_template('home.html', products_data=products_data)


def query_products():
    con = sqlite3.connect(db_local)
    c = con.cursor()
    c.execute("""
    SELECT * FROM products
    """)
    products_data = c.fetchall()
    return products_data


@app.route('/add', methods=['GET', 'POST'])
def add_items():
    if request.method == 'GET':
        return render_template('add.html')
    else:
        item_details = (
            request.form['item_name'],
            request.form['item_quantity']
        )
        insert_item(item_details)
        return render_template('add_success.html')



def insert_item(item_details):
    con = sqlite3.connect(db_local)
    c = con.cursor()
    sql_execute_string = 'INSERT INTO products (item_name, item_quantity) VALUES(?, ?)'
    c.execute(sql_execute_string, item_details)
    con.commit()
    con.close()


@app.route('/delete/<id>')
def delete(id):
    con = sqlite3.connect(db_local)
    c = con.cursor()
    c.execute("DELETE FROM products WHERE ID = '{}'".format(id))
    c.execute("UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='products';")
    con.commit()
    con.close()
    return redirect(url_for('home'))



@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'Topi' or request.form['password'] != 'goodboy':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
