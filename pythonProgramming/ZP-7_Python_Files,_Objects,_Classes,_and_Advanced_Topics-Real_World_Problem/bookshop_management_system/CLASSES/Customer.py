from CLASSES.Admin import Admin


class Customer():
    def __init__(self, customer_ID, customer_name, customer_phone_number=None, db_obj=None) -> None:
        self.customer_ID = customer_ID
        self.customer_name = customer_name
        if customer_phone_number is not None:
            self.customer_phone_number = customer_phone_number
        print("hello >> i am in 1")
        print("db_bj >>",type(db_obj))
        if db_obj:
            print("db_obj foubd")
            self.db_obj = db_obj
            admin_obj = Admin(db_obj=db_obj)
            self.search_book = admin_obj.search_book
    def test(self):
        print("i am in test")        


class MemberCustomer(Customer):
    #normal_discount = 0.10
    
    def __init__(self, customer_ID, customer_name, customer_phone_number, db_obj, memebership_type='regular') -> None:
        super().__init__(customer_ID, customer_name, customer_phone_number, db_obj)
        print("hello >> i am in 2")

        # Customer.__init__(customer_ID, customer_name, customer_phone_number, db_obj)
        self.memebership_type = memebership_type

    def get_book_discounted_price(self,book_ID):
        message = ""
        book_details = {}
        if book_ID:
            print("in ")
            discount = .10
            result = self.search_book(book_ID=book_ID)
            book_details = result[1]
            print(book_details["price"])
            book_details["price"] = book_details["price"]  - (book_details["price"]*discount)

        else:
            message = "please enter the book_ID"

        return message,book_details

    def complain(self):
        print("i am in complains  --->")
        pass

    def request_queries(self):
        pass


class GoldMember(MemberCustomer):
    discount  = .20
    def __init__(self, customer_ID, customer_name, customer_phone_number=None, db_obj=None, memebership_type='gold',points = 0):
        super().__init__(customer_ID , customer_name,
                         customer_phone_number, db_obj, memebership_type)
        self.points = points
        print("hello i am in 3")
    

    def get_book_discounted_price(self,book_ID):
        message = ""
        book_details = {}
        if book_ID:
            print("in ")
            discount = .20
            result = self.search_book(book_ID=book_ID)
            book_details = result[1]
            print(book_details["price"])
            book_details["price"] = book_details["price"] - (book_details["price"]*discount)
        else:
            message = "please enter the book_ID"

        return message,book_details    