from mysql.connector import connect

def dbconnect():
    return connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='bookmanagement'
    )

def add_book(isbn, title, author, copyright, edition, price, qty):
    total = price * qty
    connection = dbconnect()
    cursor = connection.cursor()
    query = """
        INSERT INTO books (isbn, title, author, copyright, edition, price, qty, total)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (isbn, title, author, copyright, edition, price, qty, total))
    connection.commit()
    cursor.close()
    connection.close()

def get_all_books():
    connection = dbconnect()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    cursor.close()
    connection.close()
    return books

def get_book_by_id(book_id):
    connection = dbconnect()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books WHERE id = %s", (book_id,))
    book = cursor.fetchone()
    cursor.close()
    connection.close()
    return book

def update_book(book_id, isbn, title, author, copyright, edition, price, qty):
    total = price * qty
    connection = dbconnect()
    cursor = connection.cursor()
    query = """
        UPDATE books SET isbn=%s, title=%s, author=%s, copyright=%s, 
        edition=%s, price=%s, qty=%s, total=%s WHERE id=%s
    """
    cursor.execute(query, (isbn, title, author, copyright, edition, price, qty, total, book_id))
    connection.commit()
    cursor.close()
    connection.close()

def delete_book(book_id):
    connection = dbconnect()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM books WHERE id = %s", (book_id,))
    connection.commit()
    cursor.close()
    connection.close()