from flask import Flask, render_template, request, redirect, url_for
from dbhelper import add_book, get_all_books, get_book_by_id, update_book, delete_book

app = Flask(__name__)

@app.route('/')
def index():
    books = get_all_books()
    return render_template('index.html', books=books)

@app.route('/add', methods=['GET', 'POST'])
def add_new_book():
    if request.method == 'POST':
        # Get form data
        isbn = request.form['isbn']
        title = request.form['title']
        author = request.form['author']
        copyright = request.form['copyright']
        edition = request.form['edition']
        price = float(request.form['price'])
        quantity = int(request.form['quantity'])
        
        add_book(isbn, title, author, copyright, edition, price, quantity)
        return redirect(url_for('index'))
    return render_template('add_book.html')

@app.route('/edit/<int:book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    book = get_book_by_id(book_id)
    if not book:
        return "Book not found", 404
    
    if request.method == 'POST':
        isbn = request.form['isbn']
        title = request.form['title']
        author = request.form['author']
        copyright = request.form['copyright']
        edition = request.form['edition']
        price = float(request.form['price'])
        quantity = int(request.form['quantity'])
        
        update_book(book_id, isbn, title, author, copyright, edition, price, quantity)
        return redirect(url_for('index'))    
    return render_template('edit_book.html', book=book)

@app.route('/delete/<int:book_id>', methods=['POST'])
def delete_book_route(book_id):
    delete_book(book_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
