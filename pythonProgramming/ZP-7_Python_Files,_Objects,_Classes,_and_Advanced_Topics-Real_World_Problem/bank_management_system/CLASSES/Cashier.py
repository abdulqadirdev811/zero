from CLASSES.DB import DB

class Cashier():
    def __init__(self, file) -> None:
        self.db_obj = DB(file) 
        pass

    def __getattr__(self, name):
        return getattr(self.db_obj, name)
    
  