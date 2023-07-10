# https://www.slideshare.net/bharat1911/book-store-management-system-functional-requirements-2021

class Book:
    books_list = []
    '''
    {book_name
     book_category
      book_atuhor}
    '''

    def __init__(self, book_name=None, book_category=None, book_author=None, quantity=1) -> None:
        self.book_name = book_name
        self.book_category = book_category
        self.book_author = book_author

    @classmethod
    def check_book_existance(cls, book_ID) -> bool:
        '''check if the book exists in our '''
        if [book_dict for book_dict in cls.books_list if book_dict["book_ID"] == book_ID]:
            return True
        else:
            False

    @classmethod
    def get_dictionary_from_list_of_dictionaries(cls, my_dict, book_ID) -> dict:
        result = [
            book_dict for book_dict in my_dict if book_dict["book_ID"] == book_ID][0]
        return result

    def search_book(self, book_ID=None, book_name=None) -> dict:
        book = {}
        message = ""
        if Book.check_book_existance(book_ID):
            book = Book.get_dictionary_from_list_of_dictionaries(
                Book.books_list, book_ID)
            if int(book["quantity"]) == 0:
                message = "Book Out Of Stock!!"
            else:
                message = "Book Found !!"
        else:
            message = "Book Out Of Stock!!"

        return message, book


class Customer(Book):
    

    def __init__(self, customer_ID=None, customer_name=None, customer_phone_number=None) -> None:
        self.customer_ID = customer_ID
        self.customer_name = customer_name
        self.customer_phone_number = customer_phone_number


class Supply:
    order_request_que = []
    completed_order = []
    rejected_order = []
    deleted_order = []
    due_pending = []

    def __init__(self):
        pass

    def complete_order(self, order_ID=None) -> None:
        if order_ID:
            requested_order = [
                book for book in Supply.order_request_que if book["order_ID"] == order_ID]
            if len(requested_order) > 0:
                requested_order = requested_order[0]
                Supply.order_request_que.remove(requested_order)
                Supply.completed_order.append(order_ID)
                Supply.completed_order = list(set(Supply.completed_order))
                print("order completed successfully >> ", requested_order)
            else:
                print(f"order does note exist against ID {order_ID}")

    def reject_order(self, order_ID=None) -> None:
        if order_ID:
            requested_order = [
                book for book in Supply.order_request_que if book["order_ID"] == order_ID]
            if len(requested_order) > 0:
                requested_order = requested_order[0]
                Supply.order_request_que.remove(requested_order)

                Supply.rejected_order.append(order_ID)
                Supply.rejected_order = list(set(Supply.rejected_order))
                print("order rejected successfully --> ", requested_order)
            else:
                print(f"order does note exist against --> ID {order_ID}")


class Admin(Customer, Book, Supply):
    warning_stocks = []
    out_of_stock_books = []
    supplier_list = []
    customer_list = []

    def __init___(self, admin_id=None, admin_name=None) -> None:
        pass

    def track_quantity_of_books(self) -> None:
        """
        update  the warning_stocks and out_ofstocks_books
        """

        books = self.books_list
        for book in books:
            if (book["quantity"]) < 6:
                if book["quantity"] == 0:
                    if book not in Admin.out_of_stock_books:
                        Admin.out_of_stock_books.append(book)
                else:
                    if book not in Admin.warning_stocks:
                        Admin.warning_stocks.append(book)

    
    def order_request(self, order_ID=None,supplier_ID =None , book_name=None, book_author=None, quantity=1) -> None:
        
        print("------>  0")
        if order_ID and book_name and supplier_ID :
            #print("----> 1 supplier list  : >> ",Admin.supplier_list)
            find_supplier = [sup for sup in Admin.supplier_list if sup["supplier_ID"] == supplier_ID]
            print("1")
            if  len(find_supplier) > 0:
                book_dict = {
                    "order_ID": order_ID,
                    "supplier_ID": supplier_ID,
                    "book_name": book_name,
                    "book_author": book_author,
                    "quantity": quantity
                }
                # print("book_dict >> ", book_dict)
                print("2")
                find_order = [
                    order for order in Supply.order_request_que if order["order_ID"] == order_ID]
                if len(find_order) < 1 :
                    book_in_order_queue = [
                        book for book in Supply.order_request_que if book["order_ID"] == order_ID]
                    # print("book_in_order_queue >>> ",book_in_order_queue)
                    if len(book_in_order_queue) == 0:

                        Supply.order_request_que.append(book_dict)
                        #print(Supply.order_request_que)
                        print("Requested the order successfully !!")
                    else:
                        # print(book_dict["quantity"],"<<<>>>",book_in_order_queue["quantity"])
                        print("order already in order quueue >> ", book_in_order_queue)
                        '''book_dict["quantity"] = int(
                            book_dict["quantity"]) + int(book_in_order_queue[0]["quantity"])
                        Supply.order_request_que.remove(book_in_order_queue[0])
                        Supply.order_request_que.append(book_dict)'''
                else:
                    print(f"Order already exist {order_ID}")
            else:
                print(f"No Supplier against ID {supplier_ID}")
        else:
            print(f"invalid arguments!!  ")
    def delete_order(self, order_ID=None) -> None:
        '''
        cancel the order
        '''
        if order_ID:
            my_order = [
                order for order in Supply.order_request_que if order["order_ID"] == order_ID]
            if len(my_order) > 0:
                order_details = my_order[0]
                Supply.order_request_que.remove(order_details)
                Supply.deleted_order.append(order_details["order_ID"])
                Supply.deleted_order = list(set(Supply.deleted_order))
                print("order deleted successfully ---> ", order_details)

            else:
                print(f"order does note exist against ID ---> {order_ID}")

    def add_customer(self, customer_ID=None, customer_name=None, customer_phone_number=None) -> str:
        message = ""
        if customer_ID:
            find_customer = [
                customer for customer in Admin.customer_list if customer["customer_ID"] == customer_ID]
            if len(find_customer) > 0:
                message = f"Insertion Failed !!! User Already Exists {find_customer[0]}"
            else:
                user_dict = {
                    "customer_ID": customer_ID,
                    "customer_name": customer_name,
                    "customer_phone_number": customer_phone_number
                }
                Admin.customer_list.append(user_dict)
                message = f"record is inserted successfully {user_dict} !!!"
        print(message)
        return message
    


    def delete_customer(self, customer_ID=None) -> None:
        message = ""
        if customer_ID:
            find_customer = [
                customer for customer in Admin.customer_list if customer["customer_ID"] == customer_ID]
            if len(find_customer) > 0:
                Admin.customer_list.remove(find_customer[0])
                message = f"Deleted the data successfully  {find_customer[0]}"
            else:

                message = f"Deletion Failed No Record Is Found against {customer_ID} !!!"
        print(message)

    def add_book(self, book_ID=None, book_name=None, book_category=None, book_author=None, quantity=1) -> None:
        # print(Book.books_list)
        message = ""
        if book_ID:
            if not Book.check_book_existance(book_ID):
                if book_name not in Book.books_list:
                    book_dict = {
                        "book_ID": book_ID,
                        "book_name": book_name,
                        "book_category": book_category,
                        "book_author": book_author,
                        "quantity": quantity
                    }
                    Book.books_list.append(book_dict)
                    message = f"Added new Book {book_dict}"
                    # print(Book.books_list)
            else:

                book_dict = Book.get_dictionary_from_list_of_dictionaries(
                    Book.books_list, book_ID)
                Book.books_list.remove(book_dict)
                book_dict["quantity"] = int(book_dict["quantity"]) + quantity
                Book.books_list.append(book_dict)
                message = f'Add stock : {quantity} Against Book_ID {book_dict["book_ID"]}'

    def add_suplier(self, supplier_ID=None, supplier_name=None, supplier_phone_number=None) -> str:
        message = ""
        if supplier_ID and supplier_name:
            find_supplier = [
                supplier for supplier in Admin.supplier_list if supplier["supplier_ID"] == supplier_ID]
            if len(find_supplier) > 0:
                message = f"Insertion Failed !!! User Already Exists {find_supplier[0]}"
            else:
                user_dict = {
                    "supplier_ID": supplier_ID,
                    "supplier_name": supplier_name,
                    "supplier_phone_number": supplier_phone_number
                }
                Admin.supplier_list.append(user_dict)
                message = f"record is inserted successfully {user_dict} !!!"
        #print(message)
        return message   
    def delete_supplier(self, supplier_ID=None) -> None:
        message = ""
        if supplier_ID:
            find_supplier = [
                customer for customer in Admin.supplier_list if customer["supplier_ID"] == supplier_ID]
            if len(find_supplier) > 0:
                Admin.supplier_list.remove(find_supplier[0])
                message = f"Deleted the supplier successfully  {find_supplier[0]}"
            else:

                message = f"Deletion Failed No Record Is Found against {supplier_ID} !!!"
        print(message)     

    '''def search_book(self, book_ID= None,book_name=None) -> dict:
        book = {}
        message = "Book Found !!"
        if Book.check_book_existance(book_ID):
            book = Book.get_dictionary_from_list_of_dictionaries(
                Book.books_list, book_ID)
            if int(book["quantity"]) == 0:
                message = "Warning Book Out Of Stock!!"

        return message, book
    '''

    def delete_book(self, book_ID=None, quantity=1) -> None:
        message = ""
        if book_ID:
            if Book.check_book_existance(book_ID):
                book_dict = Book.get_dictionary_from_list_of_dictionaries(
                    Book.books_list, book_ID)
                if int(book_dict["quantity"]) == 0:
                    message = (
                        f"Message -->  No book in the record against the {book_ID}")

                elif int(book_dict["quantity"]) - quantity > -1:
                    Book.books_list.remove(book_dict)
                    book_dict["quantity"] = int(
                        book_dict["quantity"]) - quantity
                    Book.books_list.append(book_dict)
                    message = f"Message --> Delete  {quantity} book/s against book_ID {book_ID} successfully !!"
                else:
                    message = (
                        f"Message --> Delete operation failed!! \n the number of book against ID {book_ID} are  {book_dict['quantity'] }  and you want to remove {quantity}")
        print(message)


admin_obj = Admin()

print(Book.books_list)
admin_obj.add_book(book_ID='001', book_name="The Hobbit")
admin_obj.add_book(book_ID='001', book_name="The Hobbit",quantity=4)
# print(Book.books_list)

admin_obj.add_book(
    book_ID="002", book_name="lord of the rings chapter 1", quantity=20)
admin_obj.add_book(
    book_ID="003", book_name="lord of the rings chapter 2", quantity=4)
admin_obj.add_book(book_ID="004", book_name="lord of the rings chapter 3")
admin_obj.add_book(book_ID="004", book_name="lord of the rings chapter 3")
admin_obj.add_book(book_ID="004", book_name="lord of the rings chapter 3")

admin_obj.add_book(book_ID="005", book_name="lord of the rings chapter 4",quantity=5)


print("Book.books_list >> ", Book.books_list)

rslt = admin_obj.search_book(book_ID="001")
print("rslt1 >>", rslt)
admin_obj.delete_book(book_ID="001")
admin_obj.delete_book(book_ID="001", quantity=2)
# admin_obj.add_book(book_ID='001',book_name="The Hobbit")
admin_obj.delete_book(book_ID="001")
rslt = admin_obj.search_book(book_ID="001")
print("rslt2 >>", rslt)
cstmr_obj = Customer()
print("before customer seach ----->")
rslt = cstmr_obj.search_book(book_ID="005")
print("rslt >> ", rslt)
print("after customer seach ----->")
print("Book.books_list >> ", Book.books_list)

admin_obj.track_quantity_of_books()

(Admin.warning_stocks)
(Admin.out_of_stock_books)
print(admin_obj.add_suplier(supplier_ID="spl-001", supplier_name="writersdev minisota", supplier_phone_number=None))
print(admin_obj.add_suplier(supplier_ID="spl-002", supplier_name="writersdev newyork", supplier_phone_number=None))
(admin_obj.order_request(order_ID="000",supplier_ID="spl-002",book_name="The Hobbit"))
(admin_obj.order_request(order_ID="001",supplier_ID="spl-002",book_name="The Hobbit"))
(admin_obj.order_request(order_ID="001",supplier_ID="spl-003",book_name="The Hobbit"))

print("admin >>>> ",admin_obj.supplier_list)

(admin_obj.delete_order(order_ID="000"))
print(Supply.order_request_que)
print("-------->")
print("order_request_queue ---> ", Supply.order_request_que)
print("completed order ---> ", Supply.completed_order)
print("rejected order ---> ", Supply.rejected_order)
print("deleted order ---> ", Supply.deleted_order)


sply_obj = Supply()

sply_obj.complete_order(order_ID="003")
sply_obj.complete_order(order_ID="003")
sply_obj.reject_order(order_ID="002")
sply_obj.reject_order(order_ID="002")

(admin_obj.delete_order(order_ID="007"))


print("order_request_queue ---> ", Supply.order_request_que)
print("completed order ---> ", Supply.completed_order)
print("rejected order ---> ", Supply.rejected_order)
print("deleted order ---> ", Supply.deleted_order)


admin_obj.add_customer(customer_ID="cstmr01",
                       customer_name="Joe", customer_phone_number=None)
admin_obj.add_customer(customer_ID="cstmr01",
                       customer_name="Joe", customer_phone_number=None)
print("Customer lsit -->", admin_obj.customer_list)
admin_obj.delete_customer(customer_ID="cstmr01")
print("Customer lsit -->", admin_obj.customer_list)

print(admin_obj.add_suplier(supplier_ID="spl-001", supplier_name="writersdev", supplier_phone_number=None))
print(admin_obj.add_suplier(supplier_ID="spl-001", supplier_name="writersdev", supplier_phone_number=None))
print(admin_obj.supplier_list)
(admin_obj.delete_supplier(supplier_ID="spl-001"))
print(admin_obj.supplier_list)