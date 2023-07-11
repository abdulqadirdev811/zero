from CLASSES.acoount_holder import AccountHolder
from CLASSES.admin import Admin
from CLASSES.cashier import Cashier
from CLASSES.DB import DB

PATH = r"C:\Users\DELL\Documents\internship\pythonProgramming\ZP-7_Python_Files,_Objects,_Classes,_and_Advanced_Topics-Real_World_Problem\bank_management_system\data\user_record.json"
file = open(PATH, mode='r+')

cashier_obj = Cashier(file=file)     
rslt = cashier_obj.search_json_file(key = "usr_account",value ="ab-0011" )
print(rslt)


'''(READ and APPEND)ar : You can't do that with a textfile. Either you want to read it or you want to write to it. 
The a or the r specifies a seek to a particular location in the file. 
Specifying both is asking open to point to two different locations in the file at the same time.'''

admin_obj = Admin(file=file)
rslt1 = admin_obj.search_json_file(key="usr_account", value="ab-0022")
print("search element  ----> ", rslt1)


# ADD USER
admin_obj.create_user(usr_account="ab-0011",
                      usr_password="qwerty321", usr_phone="032145553", usr_balance=1000)
admin_obj.create_user(usr_account="ab-0022", usr_password="qwerty321")
admin_obj.create_user(usr_account="ab-0077", usr_password="qwerty321")
admin_obj.create_user(usr_account="ab-1122", usr_password="qwerty321")
rslt = admin_obj.delete_user(usr_account="ab-0077")

#rslt = admin_obj.update_user(
#    usr_account="ab-0022", user_pass="bbbb", user_phone_number="03337398009", balance=2000)
#print(rslt)

rslt1 = admin_obj.search_json_file(key="usr_account", value="ab-0022")
print("search element  ----> ", rslt1)

cashier_obj = Cashier(file)
rslt2 = cashier_obj.search_json_file(key="usr_account", value="ab-0022")
print("rslt 2 >>> ", rslt2)

AccountHolder_obj = AccountHolder.check_account_details(
    usr_account = "ab-0022", usr_pass = "bbbb", file = file)

print("pass pass ", AccountHolder_obj.usr_pass)
AccountHolder_obj.transection(receiver_account="ab-0011", amount=500)
