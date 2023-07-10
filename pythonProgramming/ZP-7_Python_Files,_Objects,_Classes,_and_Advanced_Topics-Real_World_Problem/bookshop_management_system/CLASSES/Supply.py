class Supply:
    order_request_que = []
    completed_order = []
    rejected_order = []
    deleted_order = []

    due_pending = []



    def __init__(self):
        pass

    def complete_order(self,order_ID=None) -> None:
       if order_ID:
            requested_order =  [book for book in Supply.order_request_que if book["order_ID"] == order_ID]
            if len(requested_order) > 0:
                requested_order = requested_order[0]
                Supply.order_request_que.remove(requested_order)
                Supply.completed_order.append(order_ID)
                Supply.completed_order = list(set(Supply.completed_order))
                print("order completed successfully >> ",requested_order)
            else:
                print(f"order does note exist against ID {order_ID}")
            

    def reject_order(self,order_ID=None) -> None:
       if order_ID:
            requested_order =  [book for book in Supply.order_request_que if book["order_ID"] == order_ID]
            if len(requested_order) > 0:
                requested_order = requested_order[0]
                Supply.order_request_que.remove(requested_order)
                
                Supply.rejected_order.append(order_ID)
                Supply.rejected_order = list(set(Supply.rejected_order))
                print("order rejected successfully --> ",requested_order)
            else:
                print(f"order does note exist against --> ID {order_ID}")    
    
