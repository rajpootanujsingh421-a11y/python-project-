real_username = "anuj"
real_password = "1234"
attempt = 3
logged_in = False
while attempt >0 :
    username = input("Enter Username:")
    password = input("Enter Password:")
    if username==real_username and password==real_password:
        print("login Successfully!")
        logged_in = True
        break
    
    else:
        attempt = attempt-1
        print("Wrong Credentials!")
        print("Attempts Left:",attempt)
        
if not logged_in:
    print("Account locked!")