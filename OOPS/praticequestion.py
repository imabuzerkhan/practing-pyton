class LibraryItem:
    def __init__(self, title):  
        self.title = title
        self.is_borrowed = False  

    def borrow(self):
        try:
            if self.is_borrowed:
                raise Exception(f"Error: '{self.title}' has already been borrowed.")  # Raising exception
            self.is_borrowed = True
            return f'"{self.title}" has been borrowed.'
        except Exception as e:
            return str(e)  # Returning error message

    def returnBook(self):  # Fixed spelling mistake
        if self.is_borrowed:
            self.is_borrowed = False  # Corrected logic
            return f'"{self.title}" has been returned.'
        else:
            return f"Error: '{self.title}' was not borrowed."

class Book(LibraryItem):  # Capitalized class name
    def __init__(self, title, author):
        super().__init__(title)
        self.author = author  

    def get_author(self):
        return f"'{self.title}' is written by '{self.author}'."
       
class Journal(LibraryItem):
    def __init__(self, title, issue_number):
        super().__init__(title)
        self.issue_number = issue_number  

    def get_book(self):  # Renamed to follow standard naming conventions
        return f"'{self.title}' issue number is {self.issue_number}."

# Creating instances
journal_instance = Journal("Nature", 40)
book1 = LibraryItem("Book1")  
book2 = LibraryItem("Book2")  
book_instance = Book("The Magic of Thinking Big", "David Schwartz")

# Function calls
borrowing1 = book2.borrow()  # First borrow attempt - should succeed
borrowing2 = book2.borrow()  # Second borrow attempt - should raise exception
returning = book2.returnBook()  
checkBook = book_instance.get_author()
GetBookIssued = journal_instance.get_book()

# Print outputs
print(checkBook)          # ✅ Expected: "'The Magic of Thinking Big' is written by 'David Schwartz'."
print(GetBookIssued)      # ✅ Expected: "'Nature' issue number is 40."
print(borrowing1)         # ✅ Expected: "'Book2' has been borrowed."
print(borrowing2)         # ✅ Expected: "Error: 'Book2' has already been borrowed."
print(returning)          # ✅ Expected: "'Book2' has been returned."
