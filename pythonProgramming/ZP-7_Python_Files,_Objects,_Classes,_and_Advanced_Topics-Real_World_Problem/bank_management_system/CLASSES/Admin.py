from CLASSES.DB import DB
class Admin():
    def __init__(self, file):
        pass
        #print("constructor type(self.file) ---> ", type(self.file))
        self._db_obj = DB(file) 
        pass

    def __getattr__(self, name):
        return getattr(self._db_obj, name)

    def create_user(self, usr_account=None, usr_password=None, usr_balance=0, usr_phone=None):
        '''It will append the user into the json file if it already not exists'''
        try:
            msg = ""

            if usr_account and usr_password:
                account_exist = self.search_json_file(
                    key="usr_account", value=usr_account)[0]
                # print("user balance !!!!!!! >>>>>>>>", usr_balance)
                if not account_exist:
                    # print("dddddd")
                    json_obj = {
                        "usr_account": usr_account,
                        "usr_password": usr_password,
                        "usr_balance": usr_balance,
                        "usr_phone": usr_phone,
                    }
                    self.apend_the_json_file(json_obj)
                    msg = f"ACCOUNT : {usr_account} INSERTED SUCCESSFULLY!!"

                else:
                    msg = "account already exists!"
            else:
                msg = "USER ACCOUNT number or the user password is missing!"
        except Exception as e:
            print("error[!] in create_user ", e)
        return msg

    def delete_user(self, usr_account=None) -> str:
        try:
            msg = ""
            if usr_account:
                account_exist = self.search_json_file(
                    key="usr_account", value=usr_account)[0]
                if account_exist:
                    msg = self.delete_json(usr_account=usr_account)
                else:
                    msg = "account does not exists!!!"
            else:
                msg = "please enter the user account !!"
        except Exception as e:
            print("error[!] delete_usr ", e)
        return msg
    
    def update_user(self, usr_account=None, user_pass=None, user_phone_number=None, balance=None) -> str:
        msg = ""
        if usr_account and (user_pass or user_phone_number):
            account_exist = self.search_json_file(
                key="usr_account", value=usr_account)[0]
            print("account_exist >>> ", account_exist)
            if account_exist:
                msg = self.update_json(
                    usr_account=usr_account, user_pass=user_pass, user_phone_number=user_phone_number, balance=balance)
            else:
                msg = f"Acoount {usr_account} doest not !!!"
        else:
            msg = "add password or phone number to update!!"
        print("msg >> ", msg)

        return msg
