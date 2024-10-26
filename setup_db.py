import sqlite3
from os.path import join

DATABASE = join('instance', 'friends.db')

friends_data = [
        {
            'name': 'Name1',
            'role': 'Role1',
            'description': 'Description1',
            'gender': 'M'
        },
        {
            'name': 'Name2',
            'role': 'Role2',
            'description': 'Description2',
            'gender': 'F'
        },
        {
            'name': 'Name3',
            'role': 'Role3',
            'description': 'Description3',
            'gender': 'M'
        },
        {
            'name': 'Name4',
            'role': 'Role4',
            'description': 'Description4',
            'gender': 'M'
        },
        {
            'name': 'Name5',
            'role': 'Role5',
            'description': 'Description5',
            'gender': 'M'
        },
        {
            'name': 'Name6',
            'role': 'Role6',
            'description': 'Description6',
            'gender': 'F'
        },
        {
            'name': 'Name7',
            'role': 'Role7',
            'description': 'Description7',
            'gender': 'F'
        }
]

def create_db_and_table():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS friends (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        role TEXT NOT NULL,
        description TEXT NOT NULL,
        gender TEXT NOT NULL)
    """)

    connection.commit()
    connection.close()

def insert_sample_data():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    prepped_data = [
        (friend_data['name'], friend_data['role'], friend_data['description'], friend_data['gender']) 
        for friend_data in friends_data
    ]
    
    cursor.executemany("INSERT INTO friends (name, role, description, gender) VALUES (?, ?, ?,?)", prepped_data)
    
    connection.commit()
    connection.close()


if __name__ == '__main__':
    create_db_and_table()
    insert_sample_data()