
import mysql.connector
import os
from dotenv import load_dotenv
from datetime import date, timedelta

load_dotenv()

db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = db.cursor()

class Library:

    def display_all_books(self):
        cursor.execute("SELECT book_name FROM books")
        books = cursor.fetchall()

        if not books:
            print("No books found")
            return

        for book in books:
            print(book[0])

    def display_available_books(self):
        cursor.execute("SELECT book_name FROM books WHERE available = TRUE")
        books = cursor.fetchall()

        if not books:
            print("No available books")
            return

        for book in books:
            print(book[0])

    def borrow_book(self, name, book):

        cursor.execute(
            "SELECT book_id, available FROM books WHERE book_name=%s",
            (book,)
        )
        result = cursor.fetchone()

        if result is None:
            print("Book not found")
            return

        book_id, available = result

        if available == 0:
            print("Book already borrowed")
            return

        today = date.today()
        due_date = today + timedelta(days=7)

        cursor.execute(
            "INSERT INTO borrowed_books (book_id, username, borrow_date, due_date) VALUES (%s, %s, %s, %s)",
            (book_id, name, today, due_date)
        )

        cursor.execute(
            "UPDATE books SET available = FALSE WHERE book_id=%s",
            (book_id,)
        )

        db.commit()

        print("Book borrowed successfully")
        print(f"Due Date: {due_date}")

    def return_book(self, book):

        cursor.execute(
            "SELECT book_id FROM books WHERE book_name=%s",
            (book,)
        )
        result = cursor.fetchone()

        if result is None:
            print("Book not found")
            return

        book_id = result[0]

        cursor.execute(
            """SELECT borrow_id, due_date 
               FROM borrowed_books 
               WHERE book_id=%s AND return_date IS NULL 
               ORDER BY borrow_date DESC 
               LIMIT 1""",
            (book_id,)
        )
        borrowed = cursor.fetchone()

        if borrowed is None:
            print("This book was not borrowed")
            return

        borrow_id, due_date = borrowed
        today = date.today()

        if today > due_date:
            days_late = (today - due_date).days
            fine = days_late * 10
            print(f"Late return! Fine = Rs.{fine}")
        else:
            print("Returned on time (No fine)")

        cursor.execute(
            "UPDATE borrowed_books SET return_date=%s WHERE borrow_id=%s",
            (today, borrow_id)
        )

        cursor.execute(
            "UPDATE books SET available = TRUE WHERE book_id=%s",
            (book_id,)
        )

        db.commit()

        print("Book returned successfully")

    def analyze_data(self):

        print("\n===== DATA ANALYSIS =====")

        cursor.execute("""
            SELECT b.book_name, COUNT(*) AS borrow_count
            FROM borrowed_books bb
            JOIN books b ON bb.book_id = b.book_id
            GROUP BY b.book_name
            ORDER BY borrow_count DESC
            LIMIT 3
        """)
        print("\nTop 3 Most Borrowed Books:")
        for row in cursor.fetchall():
            print(f"{row[0]} - {row[1]} times")

        cursor.execute("""
            SELECT username, COUNT(*) AS total_books
            FROM borrowed_books
            GROUP BY username
            ORDER BY total_books DESC
        """)
        print("\nMost Active Users:")
        for row in cursor.fetchall():
            print(f"{row[0]} - {row[1]} books")

        cursor.execute("""
            SELECT COUNT(*) 
            FROM borrowed_books
            WHERE return_date IS NULL AND due_date < CURDATE()
        """)
        overdue = cursor.fetchone()[0]
        print(f"\nOverdue Books Count: {overdue}")

        cursor.execute("""
            SELECT AVG(DATEDIFF(return_date, borrow_date)) 
            FROM borrowed_books
            WHERE return_date IS NOT NULL
        """)
        avg_days = cursor.fetchone()[0]

        if avg_days is not None:
            print(f"\nAverage Borrow Duration: {avg_days:.2f} days")
        else:
            print("\nNo returned books to calculate average duration")


lib = Library()

while True:
    print("\n===== Library Menu =====")
    print("1. Display all books")
    print("2. Display available books")
    print("3. Borrow a book")
    print("4. Return a book")
    print("5. Data Analysis")
    print("6. Quit")

    try:
        choice = int(input("Enter choice: "))
    except:
        print("Enter a valid number")
        continue

    if choice == 1:
        lib.display_all_books()

    elif choice == 2:
        lib.display_available_books()

    elif choice == 3:
        name = input("Enter Username: ")
        book = input("Enter Book Name: ")
        lib.borrow_book(name, book)

    elif choice == 4:
        book = input("Enter Book Name: ")
        lib.return_book(book)

    elif choice == 5:
        lib.analyze_data()

    elif choice == 6:
        print("Thank you..")
        break

    else:
        print("Invalid choice")

    


    