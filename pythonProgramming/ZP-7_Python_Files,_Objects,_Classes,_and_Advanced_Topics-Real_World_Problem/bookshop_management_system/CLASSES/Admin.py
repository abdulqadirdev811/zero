class Admin():
    
    def __init__(self, admin_id=None, admin_name=None, db_obj = None) -> None:
        self.db_obj = db_obj
        self.admin_id = admin_id
        self.admin_name = admin_name 

    def __getattr__(self, name):
        return getattr(self.db_obj,name)
    
    def track_quantity_of_books(self) -> None:
        """
        update  the warning_stocks and out_ofstocks_books
        """

        books = self.db_obj.books_list
        for book in books:
            if (book["quantity"]) < 6:
                if book["quantity"] == 0:
                    if book not in self.db_obj.out_of_stock_books:
                        self.db_obj.out_of_stock_books.append(book)
                else:
                    if book not in self.db_obj.warning_stocks:
                       self.db_obj.warning_stocks.append(book)

    def add_customer(self, customer_obj= None) -> str:
        message = ""
        if customer_obj.customer_ID:
            find_customer = [
                customer for customer in self.db_obj.customer_list if customer["customer_ID"] == customer_obj.customer_ID]
            if len(find_customer) > 0:
                message = f"Insertion Failed !!! User Already Exists {find_customer[0]}"
            else:
                user_dict = {
                    "customer_ID": customer_obj.customer_ID,
                    "customer_name": customer_obj.customer_name,
                    "customer_phone_number": customer_obj.customer_phone_number
                }
                self.db_obj.customer_list.append(user_dict)
                message = f"record is inserted successfully {user_dict} !!!"
        print(message)
        return message
    


    def delete_customer(self, customer_obj= None) -> None:
        message = ""
        if customer_obj.customer_ID:
            find_customer = [
                customer for customer in self.db_obj.customer_list if customer["customer_ID"] == customer_obj.customer_ID]
            if len(find_customer) > 0:
                self.db_obj.customer_list.remove(find_customer[0])
                message = f"Deleted the data successfully  {find_customer[0]}"
            else:

                message = f"Deletion Failed No Record Is Found against {customer_obj.customer_ID} !!!"
        print(message)

    def add_book(self, book_obj) -> None:
        # print(Book.books_list)
        message = ""
        if book_obj.book_ID:
            if not self.db_obj.check_book_existance(book_obj.book_ID):
                
                if book_obj.book_name not in self.db_obj.books_list:
                    book_dict = {
                        "book_ID": book_obj.book_ID,
                        "book_name": book_obj.book_name,
                        "book_category": book_obj.book_category,
                        "book_author": book_obj.book_author,
                        "quantity": book_obj.quantity
                    }
                    self.db_obj.books_list.append(book_dict)
                    message = f"Added new Book {book_dict}"
                    # print(Book.books_list)
            else:

                book_dict = self.db_obj.get_dictionary_from_list_of_dictionaries(
                    self.db_obj.books_list, book_obj.book_ID)
                self.db_obj.books_list.remove(book_dict)
                book_dict["quantity"] = int(book_dict["quantity"]) + book_obj.quantity
                self.db_obj.books_list.append(book_dict)
                message = f'Add stock : {book_obj.quantity} Against Book_ID {book_dict["book_ID"]}'

    def add_suplier(self,supplier_obj = None) -> str:
        message = ""
        
        if supplier_obj.supplier_ID and supplier_obj.supplier_name:
            find_supplier = [
                supplier for supplier in self.db_obj.supplier_list if supplier["supplier_ID"] == supplier_obj.supplier_ID]
            if len(find_supplier) > 0:
                message = f"Insertion Failed !!! User Already Exists {find_supplier[0]}"
            else:
                user_dict = {
                    "supplier_ID": supplier_obj.supplier_ID,
                    "supplier_name": supplier_obj.supplier_name,
                    "supplier_phone_number": supplier_obj.supplier_phone_number
                }
                self.db_obj.supplier_list.append(user_dict)
                message = f"record is inserted successfully {user_dict} !!!"
        #print(message)
        return message  


    def delete_supplier(self, supplier_obj=None) -> None:
        message = ""
        
        if supplier_obj.supplier_ID:
            find_supplier = [
                customer for customer in self.db_obj.supplier_list if customer["supplier_ID"] == supplier_obj.supplier_ID]
            if len(find_supplier) > 0:
                self.db_obj.supplier_list.remove(find_supplier[0])
                message = f"Deleted the supplier successfully  {find_supplier[0]}"
            else:

                message = f"Deletion Failed No Record Is Found against {supplier_obj.supplier_ID} !!!"
        print(message)     



    def delete_book_quantity(self, book_obj,quantity= 1) -> None:
        message = ""
        if book_obj.book_ID:
            if self.db_obj.check_book_existance(book_obj.book_ID):
                book_dict = self.db_obj.get_dictionary_from_list_of_dictionaries(
                    self.db_obj.books_list, book_obj.book_ID)
                if int(book_dict["quantity"]) == 0:
                    message = (
                        f"Message -->  No book in the record against the {book_obj.book_ID}")

                elif int(book_dict["quantity"]) - quantity > -1:
                    self.db_obj.books_list.remove(book_dict)
                    book_dict["quantity"] = int(
                        book_dict["quantity"]) - quantity
                    self.db_obj.books_list.append(book_dict)
                    message = f"Message --> Delete  {quantity} book/s against book_ID {book_obj.book_ID} successfully !!"
                else:
                    message = (
                        f"Message --> Delete operation failed!! \n the number of book against ID {book_obj.book_ID} are  {book_dict['quantity'] }  and you want to remove {quantity}")
        print(message)


    def request_order(self,order_obj) -> None:
        #print("------>  0")
        #order_obj.
        if order_obj.order_ID and order_obj.book_name and order_obj.supplier_ID :
            #print("----> 1 supplier list  : >> ",Admin.supplier_list)
            find_supplier = [sup for sup in self.db_obj.supplier_list if sup["supplier_ID"] == order_obj.supplier_ID]
            #print("1")
            if  len(find_supplier) > 0:
                book_dict = {
                    "order_ID": order_obj.order_ID,
                    "supplier_ID": order_obj.supplier_ID,
                    "book_name": order_obj.book_name,
                    "quantity": order_obj.quantity
                }
                
                find_order = [
                    order for order in self.db_obj.order_request_que if order["order_ID"] == order_obj.order_ID]
                if len(find_order) < 1 :
                    book_in_order_queue = [
                        book for book in self.db_obj.order_request_que if book["order_ID"] == order_obj.order_ID]
                    # print("book_in_order_queue >>> ",book_in_order_queue)
                    if len(book_in_order_queue) == 0:

                        self.db_obj.order_request_que.append(book_dict)
                        #print(Supply.order_request_que)
                        print("Requested the order successfully !!")
                    else:
                        # print(book_dict["quantity"],"<<<>>>",book_in_order_queue["quantity"])
                        print("order already in order quueue >> ", self.db_obj.book_in_order_queue)
                        '''book_dict["quantity"] = int(
                            book_dict["quantity"]) + int(book_in_order_queue[0]["quantity"])
                        Supply.order_request_que.remove(book_in_order_queue[0])
                        Supply.order_request_que.append(book_dict)'''
                else:
                    print(f"Order already exist {order_obj.order_ID}")
            else:
                print(f"No Supplier against ID {order_obj.supplier_ID}")
        else:
            print(f"invalid arguments!! ")
    def delete_order(self, order_obj) -> None:
        '''
        cancel the order
        '''
        if order_obj.order_ID:
            my_order = [
                order for order in self.db_obj.order_request_que if order["order_ID"] == order_obj.order_ID]
            if len(my_order) > 0:
                order_details = my_order[0]
                self.db_obj.order_request_que.remove(order_details)
                self.db_obj.deleted_order.append(order_details["order_ID"])
                self.db_obj.deleted_order = list(set(self.db_obj.deleted_order))
                print("order deleted successfully ---> ", order_details)

            else:
                print(f"order does note exist against ID ---> {order_obj.order_ID}")    

