class book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    
    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Book Isbn: {self.isbn}")

book1 = book("Learning Python the hard way", "Zed Shaw", "987-1234567890")
book2 = book("automate with python", "Al Sweigart", "567-0987654321")
book3 = book("Fluent Python", "Luciano Ramalho", "345-1122334455")

book1.display_info()
book2.display_info()
book3.display_info()