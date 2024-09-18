class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        
    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}")

class TextBook(Book):
    def __init__(self, title, author, isbn, subject):
        super().__init__(title, author, isbn)
        self.subject = subject
    
    def display_subject(self):
        print(f"Subject: {self.subject}")
    
textbook = TextBook("Advanced Python", "John Smith", "222-3333333333", "Computer Science")
textbook.display_info()
textbook.display_subject()
