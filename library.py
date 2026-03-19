import mysql.connector
from datetime import date, timedelta

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Miru@11",
    database="library_db"
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
            "SELECT due_date FROM borrowed_books WHERE book_id=%s AND return_date IS NULL",
            (book_id,)
        )
        borrowed = cursor.fetchone()

        if borrowed is None:
            print("This book was not borrowed")
            return

        due_date = borrowed[0]
        today = date.today()

        if today > due_date:
            days_late = (today - due_date).days
            fine = days_late * 10
            print(f"Late return! Fine = Rs.{fine}")
        else:
            print("Returned on time (No fine)")

        cursor.execute(
            "UPDATE borrowed_books SET return_date=%s WHERE book_id=%s AND return_date IS NULL",
            (today, book_id)
        )

        cursor.execute(
            "UPDATE books SET available = TRUE WHERE book_id=%s",
            (book_id,)
        )

        db.commit()

        print("Book returned successfully")


lib = Library()

while True:
    print("\n===== Library Menu =====")
    print("1. Display all books")
    print("2. Display available books")
    print("3. Borrow a book")
    print("4. Return a book")
    print("5. Quit")

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
        print("Thank you..")
        break

    else:
        print("Invalid choice")

    