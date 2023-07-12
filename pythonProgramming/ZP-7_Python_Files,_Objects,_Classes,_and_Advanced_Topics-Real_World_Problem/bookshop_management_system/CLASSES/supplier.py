class Supplier:
    def __init__(self,supplier_ID=None,supplier_name = None, db_obj = None):
        pass
        self.supplier_name = supplier_name
        self.supplier_ID = supplier_ID
        self.db_obj = db_obj
        self.supplier_phone_number = ""

    def complete_order(self,order_obj= None) -> None:
       if order_obj.order_ID:
            requested_order =  [book for book in self.db_obj.order_request_que if book["order_ID"] == order_obj.order_ID]
            if len(requested_order) > 0:
                requested_order = requested_order[0]
                self.db_obj.order_request_que.remove(requested_order)
                self.db_obj.completed_order.append(order_obj.order_ID)
                self.db_obj.completed_order = list(set(self.db_obj.completed_order))
                print("order completed successfully >> ",requested_order)
            else:
                print(f"order does note exist against ID {order_obj.order_ID}")
            

    def reject_order(self,order_obj = None) -> None:
       #order_obj
       if order_obj.order_ID:
            requested_order =  [book for book in self.db_obj.order_request_que if book["order_ID"] == order_obj.order_ID]
            if len(requested_order) > 0:
                requested_order = requested_order[0]
                self.db_obj.order_request_que.remove(requested_order)
                
                self.db_obj.rejected_order.append(order_obj.order_ID)
                self.db_obj.rejected_order = list(set(self.db_obj.rejected_order))
                print("order rejected successfully --> ",requested_order)
            else:
                print(f"order does note exist against --> ID {order_obj.order_ID}")    
    

