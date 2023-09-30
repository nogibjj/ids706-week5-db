import csv
import sqlite3

# Load the iris dataset into the SQLite database
def load_iris(dataset="iris.csv"):
    conn = sqlite3.connect('iris.db')
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS iris')
    cursor.execute('''
    CREATE TABLE iris (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        SepalLengthCm DOUBLE
    )
    ''')
    with open(dataset, 'r', encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            cursor.execute('INSERT INTO iris (SepalLengthCm) VALUES (?)', (row["SepalLengthCm"],))
    conn.commit()
    conn.close()

# CRUD functions for the iris dataset
def create_iris_entry(sepal_length):
    with sqlite3.connect('iris.db') as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO iris (SepalLengthCm) VALUES (?)", (sepal_length,))
        conn.commit()

def read_all_iris_entries():
    with sqlite3.connect('iris.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM iris")
        return cursor.fetchall()

def read_iris_entry_by_id(entry_id):
    with sqlite3.connect('iris.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM iris WHERE id=?", (entry_id,))
        return cursor.fetchone()

def update_iris_entry(entry_id, sepal_length):
    with sqlite3.connect('iris.db') as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE iris SET SepalLengthCm=? WHERE id=?", (sepal_length, entry_id))
        conn.commit()


def delete_iris_entry(entry_id):
    with sqlite3.connect('iris.db') as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM iris WHERE id=?", (entry_id,))
        conn.commit()

def main():
    load_iris()
    create_iris_entry(5.5)
    print(read_all_iris_entries())
    update_iris_entry(1, 6.5)
    print(read_iris_entry_by_id(1))
    delete_iris_entry(1)
    print(read_all_iris_entries())

if __name__ == "__main__":
    main()
