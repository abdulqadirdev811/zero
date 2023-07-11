from CLASSES.DB import DB
class AccountHolder():
    def __init__(self, usr_account, usr_pass, file) -> None:
        self.usr_account = usr_account
        self.usr_pass = usr_pass
        self._db_obj = DB(file) 
        pass

    def __getattr__(self, name):
        return getattr(self._db_obj, name)
    
    def transection(self, receiver_account=None, amount=None):

        if receiver_account and amount:
            rslt = self.search_json_file(
                key="usr_account", value=receiver_account)
            check_receiver_account = rslt[0]
            print("rslt1 >>", rslt[2])
            receiver_account_details = rslt[2]
            receiver_amount = rslt[2]["usr_balance"]

            #print("check_receiver_account >> ", check_receiver_account)
            if check_receiver_account:
                sender_details = self.search_json_file(
                    key="usr_account", value = self.usr_account)
                sender_acount_detail = sender_details[2]
                #print("amount >>>>>>>>>>>.",sender_acount_detail["usr_balance"] )
                sender_remain_balance = (
                    sender_acount_detail["usr_balance"] - amount)
                print("remaining account  >>>",sender_remain_balance)
                if sender_remain_balance >= 0:
                    #print(sender_remain_balance)
                    # sender_acount_detail["usr_balance"] = sender_remain_balance
                    # receiver_account_details["usr_balance"] = receiver_amount +amount
                    
                    print("sender >> ",self.update_json(usr_account = self.usr_account,
                          balance=sender_remain_balance))
                    print("receiveer >> ",self.update_json(usr_account=receiver_account,
                          balance=receiver_account_details["usr_balance"] + amount))
                    print(
                        f"amount {amount} transfered to {receiver_account} !!")

        else:
            print("Missing arguments !!")

    @classmethod
    def check_account_details(cls, usr_account, usr_pass, file):
        account_verfied = DB.verify_account(
            usr_account=usr_account, usr_pass=usr_pass, file=file)[0]
        print(account_verfied)
        if account_verfied:
            return AccountHolder(usr_account, usr_pass, file)

