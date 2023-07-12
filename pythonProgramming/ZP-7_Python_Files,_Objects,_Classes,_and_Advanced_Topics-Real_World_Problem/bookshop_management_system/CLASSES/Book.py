class Book:
    def __init__(self,book_ID = None ,book_name=None, book_category=None, book_author=None, quantity=0) -> None:
        self.book_ID = book_ID
        self.book_name = book_name
        self.book_category = book_category
        self.book_author = book_author
        self.quantity = quantity
