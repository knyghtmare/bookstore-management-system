import psycopg2
import sys


def connect_to_database():
    try:
        conn = psycopg2.connect(
            host='localhost',
            database='bookstore',
            user='postgres',
            password='root',
            port=5432
        )
    except Exception as e:
        print(e)

    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            book_id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT,
            price INTEGER,
            isbn INTEGER)
        """
        )
    conn.commit()
    conn.close()


def insert_entry(book_id, title, author, price, isbn):
    try:
        conn = psycopg2.connect(
            host='localhost',
            database='bookstore',
            user='postgres',
            password='root',
            port=5432
        )
    except Exception as e:
        print(e)

    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO books VALUES (
            {},'{}','{}',{},{})
            '''.format(book_id, title, author, price, isbn)
        )
    conn.commit()
    conn.close()


def view_entries():
    try:
        conn = psycopg2.connect(
            host='localhost',
            database='bookstore',
            user='postgres',
            password='root',
            port=5432
        )
    except Exception as e:
        print(e)

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()
    conn.close()
    return rows


def search_entry(title="", author="", price="", isbn=""):
    try:
        conn = psycopg2.connect(
            host='localhost',
            database='bookstore',
            user='postgres',
            password='root',
            port=5432
        )
    except Exception as e:
        print(e)

    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM books WHERE title='{}' OR author='{}' OR price={} OR isbn={}
        '''.format(title, author, price, isbn)
        )
    rows = cursor.fetchall()
    conn.close()
    return rows


def delete_entry(book_id):
    try:
        conn = psycopg2.connect(
            host='localhost',
            database='bookstore',
            user='postgres',
            password='root',
            port=5432
        )
    except Exception as e:
        print(e)

    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM books WHERE book_id={}".format(book_id)
    )
    conn.commit()
    conn.close()


def update_entry(book_id, title, author, price, isbn):
    try:
        conn = psycopg2.connect(
            host='localhost',
            database='bookstore',
            user='postgres',
            password='root',
            port=5432
        )
    except Exception as e:
        print(e)

    cursor = conn.cursor()
    cursor.execute('''
        "UPDATE books SET title='{}', author='{}', price={}, isbn={} WHERE book_id={}
        '''.format(title, author, price, isbn, book_id)
    )
    conn.commit()
    conn.close()


# event that launches a connection
connect_to_database()
