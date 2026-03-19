class Library():
    def __init__(self,list):
        self.book_list = list
        self.avail_books = list[:]
        self.books_lent = {} #key-books value-uname
    def display_all_books(self):
        for book in self.book_list:
            print(book)
    def display_avail_books(self):
        for book in self.avail_books:
            print(book)
    def display_lend_books(self,name,book):
        if book not in self.book_list:
            print("Incorrect book name. Please check the book list")
            return
        if book in self.avail_books:
            self.books_lent.update({book:name})
            self.avail_books.remove(book)
            print("You can take the book..")
        else:
            print("The book is already taken by " +self.books_lent[book])
    def display_return(self,book):
        del self.books_lent[book]
        self.avail_books.append(book)

lib = Library(["The Life Divine","The Alchemist","Da Vinci Code","Head-First Python","Storytelling with Data"])
print("Welcome to Library. Please enter an option")
while True:
   print("1.Display all books")
   print("2.Display available books")
   print("3.Borrow a book")
   print("4.Return a book")
   print("5.Quit")
   choice = int(input())
   if choice==1:
        lib.display_all_books()
   elif choice==2:
        lib.display_avail_books()
   elif choice==3:
        name=input("Enter Username:")
        book=input("Enter bookname:")
        lib.display_lend_books(name,book)
   elif choice==4:
        book=input("Enter the name of the book: ")
        lib.display_return(book)
   elif choice==5:
        print("Thank you..")
   else:
        print("Invalid choice. Kindly enter the valid choice")










