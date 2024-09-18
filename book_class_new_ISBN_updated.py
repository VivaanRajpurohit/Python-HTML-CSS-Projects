class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        
    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}")

    def update_isbn(self, new_isbn):
        self.isbn = new_isbn

# Create a Book object
book = Book("Python 101", "Michael Driscoll", "000-0000000000")

# Display initial info
book.display_info()

# Update the ISBN
book.update_isbn("111-1111111111")

# Display updated info
book.display_info()
