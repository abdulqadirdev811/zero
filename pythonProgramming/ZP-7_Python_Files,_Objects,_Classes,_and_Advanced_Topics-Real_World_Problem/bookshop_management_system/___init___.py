from CLASSES.DB import DB
from CLASSES.Customer import Customer
from CLASSES.Book import Book
from CLASSES.supplier import Supplier
from CLASSES.order import Order
from CLASSES.Admin import Admin
customer_obj = Customer(customer_ID="ab-001",customer_name="abdul",customer_phone_number="0333-7398009")

db_obj = DB()

admin_obj = Admin(db_obj= db_obj)

admin_obj.add_customer(customer_obj=customer_obj)
admin_obj.add_customer(customer_obj=customer_obj)
admin_obj.delete_customer(customer_obj=customer_obj)
admin_obj.add_customer(customer_obj=customer_obj)

print("customer list -->",db_obj.customer_list)

book_obj = Book(book_name="Joe Story",book_ID= "BK-001",book_author="Qadir",quantity=20)
admin_obj.add_book(book_obj=book_obj)


print("db books record -->",db_obj.books_list)
admin_obj.delete_book_quantity(book_obj=book_obj,quantity= 19)
print("db books records -->",db_obj.books_list)

print("-----> before tracking records",db_obj.warning_stocks, db_obj.out_of_stock_books)
admin_obj.track_quantity_of_books()
print("-----> before tracking records",db_obj.warning_stocks, db_obj.out_of_stock_books)




supplier_obj = Supplier(supplier_ID="SP-001",supplier_name="Joe")

admin_obj.add_suplier(supplier_obj)

print("before supplier -----> ",db_obj.supplier_list)

admin_obj.delete_supplier(supplier_obj)
admin_obj.delete_supplier(supplier_obj)

print("after supplier -----> ",db_obj.supplier_list)

#order_ID and book_name and supplier_ID

print("before requesting the order ---------> order list",db_obj.order_request_que)
admin_obj.add_suplier(supplier_obj)


Order(order_ID="OR-001",book_name='JOE-2')
order_obj = Order(order_ID="OR-001",book_name='JOE-2',supplier_ID="SP-001")
admin_obj.request_order(order_obj)
print("after request ---------> order list",db_obj.order_request_que)

admin_obj.delete_order(order_obj)
print("deleted order list  ---> ",db_obj.deleted_order)


admin_obj.request_order(order_obj)
supplier_obj = Supplier(db_obj=db_obj)
supplier_obj.reject_order(order_obj)

print("rejected order ---> ",db_obj.rejected_order)


admin_obj.request_order(order_obj)
supplier_obj.complete_order(order_obj)
print("completed order -->",db_obj.completed_order)
