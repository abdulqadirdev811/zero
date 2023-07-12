class Customer():
    def __init__(self, customer_ID=None, customer_name=None, customer_phone_number=None, search_func=None) -> None:
        self.customer_ID = customer_ID
        self.customer_name = customer_name
        self.customer_phone_number = customer_phone_number
        self.seach_book = search_func
