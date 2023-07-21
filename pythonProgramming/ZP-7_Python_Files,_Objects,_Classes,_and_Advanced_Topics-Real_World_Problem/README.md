# OOP Real World Example



## LEARNING
  * Implemented an OOP based system.
  * Implemented the class inheritance.
  * Handled the class based varibales in child classes.
  * Enhanced the understanding  of the class methods,class variables and static method usage.
  * Resovled error related to MRO (Method Reolution order).



### BOOKSHOP MANAGEMENT SYSTEM

A book store management system manages the data regarding to the customer, supplier and Admin.  
In this project the concepts of oops e.g constructor, inheritance and MRO were implemented.
How to handle the class varible and the usage of the class functions  are also covered in it.


### 1. **USERS**
Here are the details of the users and thier usage regarding to our bookshop management system. 
* **Customer**
  * A user can search a book
* **Member Customer**
  * A member customer can search a book and see the discouted price.
* **Gold Member**
  * A A gold member can can search a book and see the discouted price(more discounted price than a normal user).
 
* **Admin**
  * An admin can check and maintain the stocks
  * Add books into the records.
  * Delelte Book Records
  * Can order books.
  * Can cancel the order
* **Supplier**
  * Can complete the order
  * Can reject the order. 


### 2. USED CLASSES.  
*  **Book** 
*  **Customer**
*  **Supply**
*  **Admin**
*  **MemeberCustomer**
*  **GoldMemeber**

### 3. CLASSES INHERITANCE GRAPHS.
* **GoldMember**
```mermaid
  graph TD;
      Customer -->MemberCustomer;
      MemberCustomer-->GoldMember

      
```


  

### BANK ACCOUNT HOLDER MANAGEMENT 

It is helper account holder management system that allow admin to create delte and update the account, enables
the account holder to do transection and assits the cashier to watch  the existing bank account details.
### 1. **USERS**
Here are the details of the users and thier usage regarding to our bookshop management system. 
* **Account Holder**
  * Perform transection.
* **Admin**
  * Create the account. 
  * Update the account
  * Delelte the account.
  * Seacrch the account details.
  * **Cashier**
  * Search the account details.



### 2. USED CLASSES.  
*  **jsonOperation** 
*  **Admin**
*  **Cashier**
*  **accountHolder**


### 3. CLASSES INHERITANCE GRAPHS.
* **Admin Class**
```mermaid
  graph TD;
      jsonOperation -->Admin;      
```
* **accountHolder Class**
  ```mermaid
  graph TD;
  jsonOperation-->accountHolder;
  ```


* **Cashier Class**
  ```mermaid
  graph TD;
      jsonOperation -->Cashier;
  ```

## USEFUL MATERIAL LINKS
[TypeError: Cannot create a consistent method resolution order (MRO) [duplicate]](https://stackoverflow.com/questions/29214888/typeerror-cannot-create-a-consistent-method-resolution-order-mro)