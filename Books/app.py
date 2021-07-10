from flask import Flask, render_template, request, redirect, url_for
from database import init_db, db_session
from models import Book

app = Flask(__name__)

@app.route('/')
def index():
    books = db_session.query(Book).all()
    return render_template('index.html', books=books)

@app.route('/new', methods=['GET','POST'])
def new_book():
    if request.method == 'POST':
        book = Book(title=request.form['title'], author=request.form['author'], genre=request.form['genre'])
        db_session.add(book)
        db_session.commit()
        return redirect(url_for('index'))
    else:
        return render_template('new_book.html')

@app.route('/<int:book_id>/edit/', methods=['GET','POST'])
def edit_book(book_id):
    edited_book = db_session.query(Book).filter_by(id=book_id).one()
    if request.method == 'POST':
        if request.form['title'] and request.form['author'] and request.form['genre']:
            edited_book.title = request.form['title']
            edited_book.author = request.form['author']
            edited_book.genre = request.form['genre']
            db_session.commit()
            return redirect(url_for('index'))
    else:
        return render_template('edit_book.html', book=edited_book)

@app.route('/<int:book_id>/delete/', methods=['GET','POST'])
def delete_book(book_id):
    book_to_delete = db_session.query(Book).filter_by(id=book_id).one()
    if request.method == 'POST':
        db_session.delete(book_to_delete)
        db_session.commit()
        return redirect(url_for('index'))
    else: 
        return render_template('delete_book.html', book=book_to_delete)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    init_db()
    app.run()