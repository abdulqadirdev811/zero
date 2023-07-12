class Order:
    def __init__(self,order_ID=None,book_name =None,supplier_ID = None,quantity =1 ) -> None:
        self.order_ID = order_ID
        self.book_name  = book_name
        self.quantity = quantity 
        self.supplier_ID = supplier_ID