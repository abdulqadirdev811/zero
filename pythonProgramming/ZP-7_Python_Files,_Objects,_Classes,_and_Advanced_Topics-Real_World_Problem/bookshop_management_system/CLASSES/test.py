from  CLASSES.Book import Book
#from book_module import B
from CLASSES.Supply import Supply
from CLASSES.Customer import Customer
from CLASSES.Admin import Admin


admin_obj = Admin()

print(Book.books_list)
admin_obj.add_book(book_ID='001',book_name="The Hobbit")
admin_obj.add_book(book_ID='001',book_name="The Hobbit")
# print(Book.books_list)

admin_obj.add_book(book_ID="002",book_name="lord of the rings chapter 1", quantity=20)


admin_obj.add_book(book_ID="003",book_name="lord of the rings chapter 2", quantity=4)
admin_obj.add_book(book_ID="004",book_name="lord of the rings chapter 3")
admin_obj.add_book(book_ID="004",book_name="lord of the rings chapter 3")
admin_obj.add_book(book_ID="004",book_name="lord of the rings chapter 3")

admin_obj.add_book(book_ID="005",book_name="lord of the rings chapter 4")
admin_obj.add_book(book_ID="005",book_name="lord of the rings chapter 4")
admin_obj.add_book(book_ID="005",book_name="lord of the rings chapter 4")
admin_obj.add_book(book_ID="005",book_name="lord of the rings chapter 4")
admin_obj.add_book(book_ID="005",book_name="lord of the rings chapter 4")


print("Book.books_list >> ",Book.books_list)

rslt = admin_obj.search_book(book_ID="001")
print("rslt1 >>", rslt)
admin_obj.delete_book(book_ID="001")
admin_obj.delete_book(book_ID="001",quantity=2)
#admin_obj.add_book(book_ID='001',book_name="The Hobbit")
admin_obj.delete_book(book_ID="001")
rslt = admin_obj.search_book(book_ID="001")
print("rslt2 >>", rslt)
print("Book.books_list >> ",Book.books_list)

admin_obj.track_quantity_of_books()

(Admin.warning_stocks)
(Admin.out_of_stock_books)
(admin_obj.order_request(order_ID="000",book_name="The Hobbit"))
(admin_obj.order_request(order_ID="000",book_name="The Hobbit",quantity=99))
(admin_obj.delete_order(order_ID="000"))
print(">>>>>>>>>>>>>>>>>>>>>>")
(admin_obj.order_request(order_ID="001",book_name="The Hobbit"))
(admin_obj.order_request(order_ID="002",book_name="The Hobbit"))
(admin_obj.order_request(order_ID="003",book_name="The Hobbit", quantity=100))

(admin_obj.order_request(order_ID="005",book_name="lord of the rings chapter 1"))
(admin_obj.order_request(order_ID="006",book_name="lord of the rings chapter 2"))
(admin_obj.order_request(order_ID="007",book_name="The Hobbit", quantity=100))


print("order_request_queue ---> ",Supply.order_request_que)
print("completed order ---> ",Supply.completed_order)
print("rejected order ---> ",Supply.rejected_order)
print("deleted order ---> ",Supply.deleted_order)


sply_obj = Supply()
sply_obj.complete_order(order_ID="003")
sply_obj.complete_order(order_ID="003")
sply_obj.reject_order(order_ID="002")
sply_obj.reject_order(order_ID="002")

(admin_obj.delete_order(order_ID="007"))


print("order_request_queue ---> ",Supply.order_request_que)
print("completed order ---> ",Supply.completed_order)
print("rejected order ---> ",Supply.rejected_order)
print("deleted order ---> ",Supply.deleted_order)
