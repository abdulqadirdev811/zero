from Book import Book
class Customer(Book):
    customer_list = []

    def __init__(self, customer_ID=None, customer_name=None, customer_phone_number=None) -> None:
        self.customer_ID = customer_ID
        self.customer_name = customer_name
        self.customer_phone_number = customer_phone_number
