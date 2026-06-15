while True:
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    choice = input("Enter Choice:")
    
    if choice == "1":
        num1 = int(input("Enter number:"))
        num2 = int(input("Enter number:"))
        print("Result:",num1 + num2)
    
    elif choice == "2":
        num1 = int(input("Enter number:"))
        num2 = int(input("Enter number:"))
        print("Result:",num1 - num2)
    
    elif choice == "3":
        num1 = int(input("Enter number:"))
        num2 = int(input("Enter number:"))
        print("Result:",num1 * num2)
    
    elif choice == "4":
        num1 = int(input("Enter number:"))
        num2 = int(input("Enter number:"))
        print("Result:",num1 / num2)
    
    elif choice == "5":
        break
    
    else:
        print("Invalid choice")
    
