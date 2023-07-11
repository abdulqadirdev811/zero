import json
print("Hello!!")
class DB:
    def __init__(self,file) -> None:
        self.file = file

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
            print("error[!] in search_json_file ss ", e)
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

