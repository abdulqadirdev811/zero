import json
PATH = r"C:\Users\DELL\Documents\internship\pythonProgramming\ZP-7_Python_Files,_Objects,_Classes,_and_Advanced_Topics-Real_World_Problem\bank_management_system\data\user_record.json"


class jsonOperation:
    def __init__(self) -> None:
        pass

    @classmethod
    def verify_account(cls, usr_account=None, usr_pass=None, file=None) -> tuple:
        ''' It will search the value in json file  against the key value
            and returns tuple(flag,msg,searched element)
            flag = is the element found 
            msg = the message tells if element is fount or not
            value = searched vlaue (returns {} if no record is found)
        '''
        if file and usr_account and usr_pass:
            flag = False
            msg = "account not verfied"
            # msg = f"{key} : {value} RECORD NOT FOUND!!!"
            rslt = {}  # weired error replace rslt with usr
            try:
                jsoned_file = json.load(file)

                for usr in jsoned_file:
                    if usr["usr_account"] == usr_account and usr["usr_password"] == usr_pass:
                        flag = True
                        msg = f"acount_verfied"
                        rslt = usr
                        break
            except Exception as e:
                print("error[!] in acount ", e)
            finally:
                file.seek(0)
            # print(msg)
        return (flag, msg, rslt)

    def search_json_file(self, key=None, value=None) -> tuple:
        ''' It will search the value in json file  against the key value
            and returns tuple(flag,msg,searched element)
            flag = is the element found 
            msg = the message tells if element is fount or not
            value = searched vlaue (returns {} if no record is found)
        '''
        flag = False
        msg = f"{key} : {value} RECORD NOT FOUND!!!"
        rslt = {}  # weired error replace rslt with usr
        try:
            jsoned_file = json.load(self.file)

            for usr in jsoned_file:
                if usr[key] == value:
                    flag = True
                    msg = f"Record Found against account : {usr[key]}"
                    rslt = usr
                    break
        except Exception as e:
            print("error[!] in search_json_file ", e)
        finally:
            self.file.seek(0)
        # print(msg)
        return (flag, msg, rslt)

    def update_json(self, usr_account=None, user_pass=None, user_phone_number=None, balance=None) -> str:
        print("blance >>>",balance )
        if True:
            try:
                msg =""
                # json.loads(str to json ) json.load TextIOWrapper to json
                jason_data = json.load(self.file)

                for index, record in enumerate(jason_data):
                    if record["usr_account"] == usr_account:
                        #print("update >> ", record)
                        if user_phone_number:
                            jason_data[index]["usr_phone"] = user_phone_number
                        if user_pass:
                            jason_data[index]["usr_password"] = user_pass
                        if usr_account:
                            jason_data[index]["usr_account"] = usr_account
                        if balance > -1 :
                            jason_data[index]["usr_balance"] = balance
                        #print("records >>> ",record)
                        msg = f"updated data for account {jason_data[index]} !!!"
                        # print("msg>>>>>>>>>>>>",msg)
                self.file.seek(0)
                self.file.truncate(0)
                print(jason_data)
                self.file.writelines(json.dumps(jason_data, indent=4))
            except Exception as e:
                print("error[!] in update_json ", e)
            finally:
                self.file.seek(0)

            return msg

    def apend_the_json_file(self, json_obj) -> str:
        '''It will take an json format obj and append it at the end of the json file  '''
        try:
            msg = f"{json_obj['usr_account']} : INSERTION FAILED !!!"

            file_data = json.load(self.file)
            file_data.append(json_obj)
            self.file.seek(0)
            json.dump(file_data, self.file, indent=4)
            msg = f"{json_obj['usr_account']} SUCCESSFULLY INSERTED  :)"
        except Exception as e:
            print("erorr[!] in append_json_file ", e)
        finally:
            self.file.seek(0)
        print(msg)
        return msg

    def delete_json(self, usr_account):

        try:
            self.file.seek(0, 0)
            jsoned_file = json.load(self.file)
            msg = ""
            for index, user in enumerate(jsoned_file):
                if user["usr_account"] == usr_account:
                    jsoned_file.pop(index)
                    # msg = f"USER ACCOUNT : {usr_account} Deleted SUCCESSFULLY !!"
                    break
            self.file.seek(0)
            self.file.truncate(0)
            self.file.writelines(json.dumps(jsoned_file, indent=4))
        except Exception as e:
            print("error in delete_json ", e)
        finally:
            self.file.seek(0, 0)
        return msg


class Cashier(jsonOperation):
    def __init__(self, file) -> None:
        self.file = file
        pass
     

class Admin(jsonOperation):
    def __init__(self, file_obj):
        pass
        self.file = file_obj
        print("constructor type(self.file) ---> ", type(self.file))

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


'''(READ and APPEND)ar : You can't do that with a textfile. Either you want to read it or you want to write to it. 
The a or the r specifies a seek to a particular location in the file. 
Specifying both is asking open to point to two different locations in the file at the same time.'''
file = open(PATH, mode='r+')
admin_obj = Admin(file)
rslt1 = admin_obj.search_json_file(key="usr_account", value="ab005")
print("search element  ----> ", rslt1)


# ADD USER
admin_obj.create_user(usr_account="ab-0011",
                      usr_password="qwerty321", usr_phone="032145553", usr_balance=1000)
admin_obj.create_user(usr_account="ab-0022", usr_password="qwerty321")
admin_obj.create_user(usr_account="ab-0077", usr_password="qwerty321")
rslt = admin_obj.delete_user(usr_account="ab-0077")

#rslt = admin_obj.update_user(
#    usr_account="ab-0022", user_pass="bbbb", user_phone_number="03337398009", balance=2000)
#print(rslt)

rslt1 = admin_obj.search_json_file(key="usr_account", value="ab-0022")
print("search element  ----> ", rslt1)

cashier_obj = Cashier(file)
rslt2 = cashier_obj.search_json_file(key="usr_account", value="ab-0022")
print("rslt 2 >>> ", rslt2)


class accountHolder(jsonOperation):
    def __init__(self, usr_account, usr_pass, file) -> None:
        self.usr_account = usr_account
        self.usr_pass = usr_pass
        self.file = file
        pass

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
        account_verfied = jsonOperation.verify_account(
            usr_account=usr_account, usr_pass=usr_pass, file=file)[0]
        print(account_verfied)
        if account_verfied:
            return accountHolder(usr_account, usr_pass, file)


accountHolder_obj = accountHolder.check_account_details(
    usr_account = "ab-0022", usr_pass = "bbbb", file = file)

print("pass pass ", accountHolder_obj.usr_pass)
accountHolder_obj.transection(receiver_account="ab-0011", amount=500)
