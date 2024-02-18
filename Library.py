class Library:
    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        try:
            self.file = open(self.file_name, 'a+')
            self.file.seek(0)
            return self
        except IOError:
            print("Error: Unable to open file.")
            raise

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

    def list_books(self):
        try:
            self.file.seek(0)
            books = self.file.readlines()
            if not books:
                print("No books available.")
                return
            print("List of Books:")
            for book in books:
                book_info = book.strip().split(',')
                print(f"Title: {book_info[0]}, Author: {book_info[1]}")
        except IOError:
            print("Error: Unable to read from file.")

    def add_book(self):
        try:
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            release_year = input("Enter the release year of the book: ")
            num_pages = input("Enter the number of pages of the book: ")
            book_info = f"{title},{author},{release_year},{num_pages}\n"
            self.file.write(book_info)
            print("Book added successfully.")
        except IOError:
            print("Error: Unable to write to file.")

    def remove_book(self):
        try:
            title = input("Enter the title of the book to remove: ")
            self.file.seek(0)
            books = self.file.readlines()
            new_books = []
            removed = False
            for book in books:
                if title not in book:
                    new_books.append(book)
                else:
                    removed = True
            if not removed:
                print("Book not found.")
                return
            self.file.seek(0)
            self.file.truncate(0)
            self.file.writelines(new_books)
            print("Book removed successfully.")
        except IOError:
            print("Error: Unable to modify file.")




# Creating an object named “lib” with “Library” class
with Library("books.txt") as lib:
    while True:
        # Creating a menu
        print("*** MENU***")
        print("1) List Books")
        print("2) Add Book")
        print("3) Remove Book")
        print("4) Quit")
        
        # Asking user input for menu item
        choice = input("Enter your choice: ")

        if choice == '1':
            lib.list_books()
        elif choice == '2':
            lib.add_book()
        elif choice == '3':
            lib.remove_book()
        elif choice == '4':
            break
        else:
            print("Not a valid option. Please enter a valid option.")
