import csv
import sqlite3

# Load the iris dataset into the SQLite database
def load_iris(dataset="iris.csv"):
    print("-" * 50)
    print("Loading data from", dataset)
    conn = sqlite3.connect('iris.db')
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS iris')
    cursor.execute('''
    CREATE TABLE iris (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        SepalLengthCm DOUBLE
    )
    ''')
    with open(dataset, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            cursor.execute('INSERT INTO iris (SepalLengthCm) VALUES (?)', (row["SepalLengthCm"],))
    conn.commit()
    conn.close()
    print("Data loaded successfully!")
    print("-" * 50)

# CRUD functions for the iris dataset
def create_iris_entry(sepal_length):
    print("Creating new entry with SepalLengthCm =", sepal_length)
    with sqlite3.connect('iris.db') as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO iris (SepalLengthCm) VALUES (?)", (sepal_length,))
        conn.commit()
    print("Entry created successfully!")
    print("-" * 50)

def read_all_iris_entries():
    print("Reading all entries...")
    with sqlite3.connect('iris.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM iris")
        entries = cursor.fetchall()
    print("Entries:", entries)
    print("-" * 50)
    return entries

def read_iris_entry_by_id(entry_id):
    print("Reading entry with ID =", entry_id)
    with sqlite3.connect('iris.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM iris WHERE id=?", (entry_id,))
        entry = cursor.fetchone()
    print("Entry:", entry)
    print("-" * 50)
    return entry

def update_iris_entry(id, sepal_length):
    print(f"Updating entry with ID = {id} to SepalLengthCm = {sepal_length}")
    with sqlite3.connect('iris.db') as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE iris SET SepalLengthCm=? WHERE id=?", (sepal_length, id))
        conn.commit()
    print("Entry updated successfully!")
    print("-" * 50)

def delete_iris_entry(id):
    print(f"Deleting entry with ID = {id}")
    with sqlite3.connect('iris.db') as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM iris WHERE id=?", (id,))
        conn.commit()
    print("Entry deleted successfully!")
    print("-" * 50)

def main():
    load_iris()
    create_iris_entry(5.5)
    read_all_iris_entries()
    update_iris_entry(1, 6.5)
    read_iris_entry_by_id(1)
    delete_iris_entry(1)
    read_all_iris_entries()

if __name__ == "__main__":
    main()