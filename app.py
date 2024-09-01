from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)

# Create a connection to the SQLite database
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Create a route for the homepage
@app.route('/')
def index():
    conn = get_db_connection()
    product = conn.execute('SELECT * FROM products WHERE id = 1').fetchone()
    conn.close()
    return render_template('index.html', product=product)

# Create a route to get JSON data
@app.route('/api/product')
def product_data():
    conn = get_db_connection()
    product = conn.execute('SELECT * FROM products WHERE id = 1').fetchone()
    conn.close()
    return jsonify(dict(product))

if __name__ == '__main__':
    app.run(debug=True)
