import sqlite3
from book import Book


sqliteConnection  = sqlite3.connect('books.db')
cursor = sqliteConnection.cursor()
    
    
#Create the table 

cursor.execute('CREATE TABLE IF NOT EXISTS books (title TEXT,pages INTEGER)')
#cursor.connection.close()  


#add books
def add_books(book):   
    
    with cursor.connection:
        cursor.execute('INSERT INTO books values (?,?)',(book.title,book.pages))
    
    return cursor.lastrowid

def get_books():
    books = []
    with cursor.connection:
        for book in cursor.execute('SELECT * FROM books'):
            books.append(Book(book[0],book[1]))
            
        
    #return cursor.fetchall()
    return books

    
    