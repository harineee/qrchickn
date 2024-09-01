import faker
import random
import sqlite3

fake = faker.Faker()

def insert_fake_data(num_records=10):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    for _ in range(num_records):
        name = fake.word().capitalize() + " " + fake.word().capitalize()
        packaging_date = fake.date_between(start_date='-2y', end_date='today')
        expiration_date = fake.date_between(start_date=packaging_date, end_date='+30d')
        batch_number = fake.bothify(text='??-#####X#')
        supplier_info = f"{fake.company()}, {fake.address()}"
        calories = random.randint(100, 300)
        protein = random.uniform(10.0, 40.0)
        fat = random.uniform(1.0, 20.0)
        ingredients = fake.words(nb=3, ext_word_list=None, unique=False)
        ingredients = ', '.join([ingredient.capitalize() for ingredient in ingredients])
        allergens = fake.word().capitalize() if random.choice([True, False]) else 'None'
        dietary_suitability = random.choice(['Halal', 'Kosher', 'Vegan', 'Vegetarian', 'Pescatarian'])
        certifications = random.choice(['Halal Certified', 'Kosher Certified', 'Organic Certified'])
        spoilage_indicator = random.choice(['Fresh', 'Slightly Spoiled', 'Severely Spoiled'])
        storage_instructions = f"Keep refrigerated at or below {random.randint(0, 4)}°C"
        origin_information = f"Farm Location: {fake.city()}, {fake.state()}, {fake.country()}"
        processing_history = f"Cut and packed on-site at {fake.company()}"

        cursor.execute('''
            INSERT INTO products (name, packaging_date, expiration_date, batch_number, supplier_info, 
            calories, protein, fat, ingredients, allergens, dietary_suitability, certifications, 
            spoilage_indicator, storage_instructions, origin_information, processing_history)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            name, packaging_date, expiration_date, batch_number, supplier_info, 
            calories, protein, fat, ingredients, allergens, dietary_suitability, certifications, 
            spoilage_indicator, storage_instructions, origin_information, processing_history
        ))

    conn.commit()
    conn.close()
    print(f"Inserted {num_records} fake records into the database.")

insert_fake_data(10) # Set Param for how many records to add