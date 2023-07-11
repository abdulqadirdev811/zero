from CLASSES.json_operation import jsonOperation

class Cashier():
    def __init__(self, file) -> None:
        self.cashier_obj = jsonOperation(file) 
        pass

    def __getattr__(self, name):
        return getattr(self.cashier_obj, name)
    
  