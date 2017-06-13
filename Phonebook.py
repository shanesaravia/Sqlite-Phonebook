import sqlite3, sys

class Phonebook(object):
    def __init__(self):
        try:
            c.execute('CREATE TABLE entries(id INTEGER PRIMARY KEY, name TEXT, phone TEXT unique)')
        except:
            pass
        print('Welcome to the Phonebook')


    def add_entry():
        name = input('Please enter a name: ')
        number = input('Please enter a phone number: ')
        c.execute('INSERT INTO entries(name, phone) VALUES(?,?)', (name, number))

    def del_entry():
        name = input('Please enter a name to delete: ')
        c.execute('DELETE FROM entries WHERE name=?', (name,))

    def rollback():
        db.rollback()

    def query():
        c.execute('SELECT name, phone FROM entries')
        for items in c:
            print(items)

    def save():
        db.commit()

    def exit():
        sys.exit()

class MainMenu(Phonebook):
    def __init__(self):
        print('''
Main Menu
Please select an option:
    1. "add" - to add an entry.
    2. "delete" - to delete an entry.
    3. "rollback" - to undo your last change.
    4. "query" - to query an entry.
    5. "save" - to save changes.
    6. "exit" - to exit the program.
            ''')

        selection = input()
        if selection == 'add':
            try:
                Phonebook.add_entry()
            except IntegrityError:
                print('Phone Number already exists.')

        if selection == 'delete':
            Phonebook.del_entry()

        if selection == 'rollback':
            Phonebook.rollback()

        if selection == 'query':
            Phonebook.query()

        if selection == 'save':
            Phonebook.save()

        if selection == 'exit':
            Phonebook.exit()

db = sqlite3.connect('ENTER DIRECTORY AND FILENAME HERE. ex. c:/users/myaccount/myfirstDB.sqlite')
c = db.cursor()

Phonebook()
while True:
    MainMenu()

db.close()