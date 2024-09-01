from flask import Flask, render_template, jsonify, request
import sqlite3
import random
from datetime import datetime, timedelta

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    product = conn.execute('SELECT * FROM products WHERE id = 1').fetchone()
    conn.close()
    return render_template('index.html', product=product)

@app.route('/api/product')
def product_data():
    conn = get_db_connection()
    product = conn.execute('SELECT * FROM products WHERE id = 1').fetchone()
    conn.close()
    return jsonify(dict(product))

@app.route('/api/nutritional_info')
def nutritional_info():
    conn = get_db_connection()
    nutritional_info = conn.execute('SELECT calories, protein, fat FROM products WHERE id = 1').fetchone()
    conn.close()
    return jsonify(dict(nutritional_info))

@app.route('/api/supplier_info')
def supplier_info():
    conn = get_db_connection()
    supplier_info = conn.execute('SELECT supplier_info FROM products WHERE id = 1').fetchone()
    conn.close()
    return jsonify(dict(supplier_info))

@app.route('/api/dietary_restrictions')
def dietary_restrictions():
    conn = get_db_connection()
    dietary_info = conn.execute('SELECT dietary_suitability, certifications FROM products WHERE id = 1').fetchone()
    conn.close()
    return jsonify(dict(dietary_info))

@app.route('/api/spoilage_status')
def spoilage_status():
    conn = get_db_connection()
    product = conn.execute('SELECT expiration_date, spoilage_indicator FROM products WHERE id = 1').fetchone()
    conn.close()

    expiration_date = datetime.strptime(product['expiration_date'], '%Y-%m-%d')
    current_date = datetime.now()

    status = "Edible" if current_date <= expiration_date else "Spoiled"
    result = {
        "status": status,
        "details": product['spoilage_indicator'] if status == "Spoiled" else "Product is fresh"
    }

    return jsonify(result)

@app.route('/api/update_spoilage', methods=['POST'])
def update_spoilage():
    new_status = request.json.get('new_status')
    
    conn = get_db_connection()
    conn.execute('UPDATE products SET spoilage_indicator = ? WHERE id = 1', (new_status,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Spoilage indicator updated successfully"})

@app.route('/api/traceability')
def traceability():
    conn = get_db_connection()
    traceability_info = conn.execute('SELECT origin_information, processing_history FROM products WHERE id = 1').fetchone()
    conn.close()
    return jsonify(dict(traceability_info))

@app.route('/api/countdown')
def countdown():
    target_date = datetime.now() + timedelta(days=10)
    time_left = target_date - datetime.now()

    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return jsonify({
        "days": days,
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds
    })

@app.route('/api/random_nutritional_fact')
def random_nutritional_fact():
    facts = [
        "High in protein, good for muscle building.",
        "Low in fat, suitable for weight loss.",
        "Rich in omega-3 fatty acids, great for heart health.",
        "High in vitamin D, beneficial for bone health."
    ]
    selected_fact = random.choice(facts)
    return jsonify({"fact": selected_fact})

@app.route('/api/verify_batch/<batch_number>')
def verify_batch(batch_number):
    conn = get_db_connection()
    product = conn.execute('SELECT * FROM products WHERE batch_number = ?', (batch_number,)).fetchone()
    conn.close()

    if product:
        return jsonify({"status": "valid", "product_name": product['name']})
    else:
        return jsonify({"status": "invalid", "message": "Batch number not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)