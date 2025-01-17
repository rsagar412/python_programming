# library class with no of books and books as two instance variables. Write a program to create the library class and show how you can print all books, add a book and get number of books using different methods. Show that your program doesn't persist the books after the program is stopped. 


class Library:
    def __init__(self, books):
        self.books = []
        self.no_of_books = 0

    def addBook(self, book):
        self.books.append(book)
        self.no_of_books = len(self.books)
    
    def showinfo(self):
        print("Books: ", self.books)
        print("No of books: ", self.no_of_books)

l1 = Library([])
l1.addBook("Python")
l1.addBook("Javascript")
l1.addBook("MERN STACK")
l1.showinfo()


