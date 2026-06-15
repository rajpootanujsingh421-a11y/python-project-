real_username = "anuj"
real_password = "1234"

username = input("Enter Username:")
password = input("Enter Password:")

if username == real_username and password == real_password:
    print("Login Successfully!")
else:
    print("Login Unsuccessful!")