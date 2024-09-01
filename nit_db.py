import sqlite3

# Connect to SQLite database
connection = sqlite3.connect('database.db')

# Create a cursor object
cursor = connection.cursor()

# Create a table for products
cursor.execute('''
    CREATE TABLE products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        packaging_date TEXT NOT NULL,
        expiration_date TEXT NOT NULL,
        batch_number TEXT NOT NULL,
        supplier_info TEXT NOT NULL,
        calories INTEGER NOT NULL,
        protein INTEGER NOT NULL,
        fat INTEGER NOT NULL,
        ingredients TEXT NOT NULL,
        allergens TEXT NOT NULL,
        dietary_suitability TEXT NOT NULL,
        certifications TEXT NOT NULL,
        spoilage_indicator TEXT NOT NULL,
        storage_instructions TEXT NOT NULL,
        origin_information TEXT NOT NULL,
        processing_history TEXT NOT NULL
    )
''')

# Insert fake data into the products table
cursor.execute('''
    INSERT INTO products (name, packaging_date, expiration_date, batch_number, supplier_info, 
    calories, protein, fat, ingredients, allergens, dietary_suitability, certifications, spoilage_indicator, 
    storage_instructions, origin_information, processing_history)
    VALUES 
    ('Chicken Breast', '2024-08-01', '2024-08-08', 'CB-2043X7', 'Fresh Farms Poultry, 123 Market St, Springfield, IL', 
    165, 31, 3.6, '100% Chicken Breast', 'None', 'Suitable for Halal diet', 'Halal Certified', 'Severely Spoiled', 
    'Originally recommended to keep refrigerated at or below 4°C', 
    'Farm Location: Green Valley Farms, Kentucky, USA', 'Cut and packed on-site at Green Valley Farms')
''')

# Commit the changes and close the connection
connection.commit()
connection.close()