import uuid
from datetime import datetime, timezone


# TASK 1: We were tasked with creating an Expense Class to demonstrate our level of comprehension of OOP in python
class Expense:
    def __init__(self, title, amount):          # Attributes initialisation
        self.id = str(uuid.uuid4())             # UUID4() to generate a unique identifier for each expense
        self.title = title                      # A string representing the title of the expense.
        self.amount = amount                    # A float representing the amount of the expense.
        self.created_at = datetime.utcnow()     # A timestamp indicating when the expense was created (UTC).
        self.updated_at = self.created_at       # New expense should be updated at creation time of the expense

    def update(self, title=None, amount=None):  # Instruction says title=None, amount=None, I feel the update should ...
        if title:                               # have a new title and a new amount
            self.title = title
        if amount:
            self.amount = amount
        self.updated_at = datetime.utcnow()

    """
        def update(self, new_title=None, new_amount=None):
            if new_title:
                self.title = new_title
            if new_amount:
                self.amount = new_amount
            self.updated_at = datetime.utcnow()
            
"""

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "amount": self.amount,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S UTC"),
            "updated_at": self.updated_at.strftime("%Y-%m-%d %H:%M:%S UTC")
        }

expense1 = Expense("Ice-cream and Popsicle", 25.0)
expense2 = Expense("Toys", 55.0)
expense3 = Expense("Clothes", 100.0)

print(expense1.to_dict())
print(expense2.to_dict())
print(expense3.to_dict())


# TASK 2: We were tasked with creating an Expense Database to demonstrate our level of comprehension of OOP in python
class ExpenseDB:                    # To act as database for all expenses
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):             # To add an expense to the DB
        self.expenses.append(expense)

    def remove_expense(self, expense_id):       # To remove an expense by id from the DB
        for expense in self.expenses:
            if expense.id == expense_id:
                self.expenses.remove(expense)
                break

    def get_expense_by_id(self, expense_id):    # To get an expense by id from the DB
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense
        return None

    def get_expense_by_title(self, title):      # To get an expense by title from the DB
        return [expense for expense in self.expenses if expense.title == title]

    def to_dict(self):      # returns all expenses in a list
        return [expense.to_dict() for expense in self.expenses]


# Creating an ExpenseDB instance
expense_db = ExpenseDB()

# Adding expenses to the database
expense1 = Expense("Electricity", 125.0)
expense2 = Expense("Water and Waste Bill", 160.0)
expense3 = Expense("Rent", 850.0)
expense4 = Expense("Security Dues", 180.0)

expense_db.add_expense(expense1)
expense_db.add_expense(expense2)
expense_db.add_expense(expense3)
expense_db.add_expense(expense4)

print("All expenses in the database:", expense_db.to_dict())

# Getting an expense by ID
retrieved_expense = expense_db.get_expense_by_id(expense1.id)
if retrieved_expense:
    print("Retrieved expense by ID:", retrieved_expense.to_dict())

# Removing an expense
expense_db.remove_expense(expense2.id)

# Displaying all expenses after removing expense2
print("The remaining expenses in the database:", expense_db.to_dict())

# Getting expenses by title
expenses_by_title = expense_db.get_expense_by_title("Rent")
if expenses_by_title:
    print("Expenses retrieved by title:")
    for expense in expenses_by_title:
        print(expense.to_dict())

