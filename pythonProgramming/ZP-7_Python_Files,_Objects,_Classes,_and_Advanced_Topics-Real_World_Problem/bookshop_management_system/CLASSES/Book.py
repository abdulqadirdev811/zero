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
        '''tells if the book exists in the records'''
        if [book_dict for book_dict in cls.books_list if book_dict["book_ID"] == book_ID]:
            return True
        else:
            False
    @classmethod
    def get_dictionary_from_list_of_dictionaries(cls,my_dict, book_ID) -> dict:
        '''returns dictionary fromt the given list of dictionary'''
        result = [book_dict for book_dict in my_dict if book_dict["book_ID"] == book_ID][0]
        return result

    

    def search_book(self, book_ID= None,book_name=None) -> dict:
        '''search and provide the details of the books from class varible book_list'''
        book = {}
        
        if Book.check_book_existance(book_ID):
            book = Book.get_dictionary_from_list_of_dictionaries(
                Book.books_list, book_ID)
            if int(book["quantity"]) == 0:
                message = "Warning Book Out Of Stock!!"
            else:
                message = "Book Found !!"
        return message, book
