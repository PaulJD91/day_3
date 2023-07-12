class Book:

    def __init__(self, title):
        self.title = title
        self.current_page = 1
    
    def flip_page(self):
        self.current_page += 1
    
book = Book("Harry Potter")
print(book.title)
book.flip_page()
print(book.current_page)

