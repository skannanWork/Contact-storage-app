import sqlite3

# Connect to the database
conn = sqlite3.connect('contacts.db')

# Create a table to store the contacts
conn.execute('''CREATE TABLE contacts (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL)''')

# Function to add a new contact
def add_contact(name, email, phone):
    conn.execute('''INSERT INTO contacts (name, email, phone)
                    VALUES (?, ?, ?)''', (name, email, phone))
    conn.commit()

# Function to update an existing contact
def update_contact(id, name, email, phone):
    conn.execute('''UPDATE contacts
                    SET name = ?, email = ?, phone = ?
                    WHERE id = ?''', (name, email, phone, id))
    conn.commit()

# Function to delete a contact
def delete_contact(id):
    conn.execute('''DELETE FROM contacts WHERE id = ?''', (id,))
    conn.commit()

# Function to search for a contact
def search_contact(name):
    cursor = conn.execute('''SELECT * FROM contacts WHERE name LIKE ?''', (f'%{name}%',))
    return cursor.fetchall()

# User interface
while True:
    print('1. Add a contact')
    print('2. Update a contact')
    print('3. Delete a contact')
    print('4. Search for a contact')
    print('5. Quit')
    choice = input('Enter your choice: ')

