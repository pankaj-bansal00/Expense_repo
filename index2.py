"""This is the expense tracker Task"""

print("Welcome to the Expense Tracker")

expenses = []

def add_expense( amount, category, date):
    expense = {
        'amount': amount,
        'category': category,
        'date': date
    }
    expenses.append(expense)
    print("Print Expense successfully")
 

def get_veiw():
    print(expenses)
  

def total_expense():
    total = sum(expenses['amount'])
    print(total)
print(total_expense)

while True:
    print("""Enter your task
        1. add_expense
        2. veiw
        3. total_expense
        4. Exit""")
        
    choice = int(input("enter the 1-4: "))
    
    if choice == '1':
        expenses['date'] = input("Enter the date: dd/mm/yyyy:  ")
        expenses['amount'] = float(input("Enter your amount:  "))
        expenses['category'] = input("Enter the description about your expense: ")
        add_expense('amount','category','date')

    elif choice == '2':
        get_veiw

    elif choice == '3':
        total_expense

    else:
        print("Thank you for Using Expense Tracker")
           