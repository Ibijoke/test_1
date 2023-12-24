### ibijoke_bodunrin_1st_sem_de_exam

1. Project description:
This task was designed to test my comprehension of Object Oriented Programming in Python. 
The first part involved creating a Class called Expense where I needed to first create the class and initialize it, then list all the attributes that each instance (object) of the class must possess. In tracking each expense, the object must have a unique ID which is auto-generated using UUID4(), an expenses title (what the money was spent on), cost of the item (amount), date and time of expense- this is also auto-generated using the datetime module. Two additional methods were required to be created- the update and to_dict methods. Update method (I presume) is to allow editing of an already existing expense, the time of the update was required to be recorded. The to_dict is to accept and return all the attributes details of each expense in a dictionary datatype with the attributes as the key and the expense details as the values.
The second part was to create a database for storing all the expenses. This required creation of another class called ExpenseDB. This will act as a collection and storage point for all the details of each expense using a list datatype. I was tasked to create five different methods, asides the initialization method, in this class- add_expense: to add an expense to the database, remove_expense: to remove an expense using the unique identifier, get_expense_by_id: retrieves an expense by using the expense ID, get_expense_by_title: this can be used to retrieved expenses by title, to_dict: returns a list of dictionaries representing expenses.
2.	How to clone this project
Open your terminal, change directory to the folder you want to clone the file to. Enter the git clone command followed by the url for the file (this can be gotten from the github page, navigate to the clone or download button and copy the url). This command will clone this project to your computer locally. 
3.	How to run the code

