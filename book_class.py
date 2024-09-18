class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.__isbn = isbn

    def get_isbn(self):
        return self.__isbn   

    def set_isbn(self, new_isbn):
        if self.validate_isbn(new_isbn):
            self.__isbn = new_isbn
        else:
            print("Invalid ISBN")

    def validate_isbn(self, isbn):
        # Add your ISBN validation logic here; for now, let's just check it's a string with 13 characters
        return isinstance(isbn, str) and len(isbn) == 13

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Book ISBN: {self.__isbn}")

my_book = Book("Python Programming", "Jane Doe", "123-4567890123")
my_book.display_info()
