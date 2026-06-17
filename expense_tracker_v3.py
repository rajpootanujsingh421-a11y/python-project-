expenses = []
while True:
    print("1. Add Expense")
    print("2. Show Expense")
    print("3. Total Expense")
    print("4. Delete Expense")
    print("5. Edit Expense")
    print("6. Exit")
    choice = int(input("Enter your choice:"))

    if choice == 1:
        print("You selected Add Expense")
        category = input("Enter category:")
        amount = float(input("Enter amount:"))
        expense = {
            "category": category,
            "amount" : amount
        }
        expenses.append(expense)
        print("Expense Added Successfully..!")
    
    elif choice == 2:
        if len(expenses)==0:
            print("No Expenses found!")
            
        else:
            count = 1
            print("-----Expenses-------")
            print("You selected show Expense..")
            for expense in expenses:
                print(count,expense["category"],expense["amount"])
                count = count + 1
            
    elif choice == 3:
        if len(expenses)==0:
            print("No Expenses found!")
            
        else:
            total = 0
            for expense in expenses:
                total = total + expense["amount"]
    
            print("Total Expense =",total)
        
    elif choice == 4:
        if len(expenses)==0:
            print("No Expenses found!")
            
        else:
            count = 1
            for expense in expenses:
                print(count,expense["category"],expense["amount"])
                count = count + 1
            delete_index = int(input("Enter expense number to delete: "))
            expenses.pop(delete_index - 1)
            print("Expense Deleted Successfully..!")
            
    elif choice == 5:
        if len(expenses)==0:
            print("No Expenses found!")
            
        else:
            count = 1
            for expense in expenses:
                print(count,expense["category"],expense["amount"])
                count = count + 1
            edit_index = int(input("Enter expense number to edit: "))
            new_category = input("Enter new category: ")
            new_amount = float(input("Enter new amount: "))
            expenses[edit_index - 1]["category"] = new_category
            expenses[edit_index - 1]["amount"] = new_amount
            print("Expense Updated Successfully..!")
    
    elif choice == 6:
        print("Good Bye")
        break
        