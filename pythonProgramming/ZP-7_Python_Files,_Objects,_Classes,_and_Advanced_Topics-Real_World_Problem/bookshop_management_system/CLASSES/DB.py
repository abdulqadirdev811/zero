class DB:

    def __init__(self, warning_stocks=[], out_of_stock_books=[], supplier_list=[], customer_list=[], order_request_que=[], completed_order=[], rejected_order=[], deleted_order=[],books_list =[]) -> None:
        self.warning_stocks = warning_stocks
        self.out_of_stock_books = out_of_stock_books
        self.supplier_list = supplier_list
        self.customer_list = customer_list
        self.order_request_que = order_request_que
        self.completed_order = completed_order
        self.rejected_order = rejected_order
        self.deleted_order = deleted_order
        self.books_list = books_list


    def get_dictionary_from_list_of_dictionaries(self, my_dict, book_ID) -> dict:
        '''returns dictionary from the given list of dictionary'''
        result = [
            book_dict for book_dict in my_dict if book_dict["book_ID"] == book_ID][0]
        return result
    
    def check_book_existance(self, book_ID) -> bool:
        '''check if the book exists in our '''
        result = False
        try:
            if [book_dict for book_dict in self.books_list if book_dict["book_ID"] == book_ID]:
                result =  True
            
        except Exception as e:
            pass    
        return result