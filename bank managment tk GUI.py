import tkinter as tk
import sqlite3
from datetime import datetime
accounts = []
account_number = 100
conn = sqlite3.connect("c:/Users/LENOVO/OneDrive/文档 - Copy/文档/GitHub/python_project/bank.db") 
Admin_username = "arnav"
Admin_password = "1432"
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts(
    account_no INTEGER PRIMARY KEY,
    name TEXT,
    balance INTEGER
)
""" )

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    account_no INTEGER,
    type TEXT,
    amount INTEGER
)
""")
conn.commit()
try:
    cursor.execute(
        "ALTER TABLE transactions ADD COLUMN date TEXT"
    )
    conn.commit()
except:
    pass

def create_account():
    global account_number
    
    name = entry_name.get()
    balance = entry_balance.get()
    
    try:
        
        balance = int(balance)
        if balance > 0:
            account_number = get_account_number()
            cursor.execute(
                "INSERT INTO accounts VALUES(?,?,?)",
                (account_number,name,balance)
            )
    
            conn.commit()
            
            result_label.config(text="Account Created Successfully")
            entry_name.delete(0,tk.END)
            entry_balance.delete(0,tk.END)
        else:
            result_label.config(text="Balance should be positive")
    except Exception as e:
        print(e)
        result_label.config(text="Error")
    
def show_accounts():
    text_box.delete("1.0",tk.END)
    cursor.execute("SELECT * FROM accounts")
    rows = cursor.fetchall()
    
    for acc in rows:
        text_box.insert(
            tk.END,
            f"Acc No:{acc[0]} | Name: {acc[1]} | Balance: {acc[2]}\n"
        )
        
def deposit_money():
    try:
        acc_no = int(entry_acc.get())
        amount = int(entry_amount.get())
        
        if amount > 0:
            
            cursor.execute(
                "SELECT balance FROM accounts WHERE account_no=?",
                (acc_no,)
            )
            acc = cursor.fetchone()
            
            if acc:     
                new_balance = acc[0] + amount
                
                cursor.execute(
                    "UPDATE accounts SET balance = ? WHERE account_no=?",
                    (new_balance,acc_no)
                ) 
                cursor.execute(
                    "INSERT INTO transactions(account_no,type,amount,date)VALUES(?,?,?,?)",
                    (    
                        acc_no,
                        "DEPOSIT",
                        amount,
                        datetime.now().strftime("%d-%m-%Y %H:%M")
                    )
                )   
                conn.commit()   
                
                result_label.config(
                    text="Money Deposited Successfully"
                )
            else:
                result_label.config (
                    text="Account Not Found"
                )
            
        else:
            result_label.config(
                text="Amount should be positive"
            )
    
    except:
        result_label.config(
            text="Enter Valid Amount"
        )
    
def withdraw_money():
    try:
        acc_no = int(entry_withdraw_acc.get())
        amount = int(entry_withdraw_amount.get())
        
        if amount > 0:
            
            cursor.execute(
                "SELECT balance FROM accounts WHERE account_no=?",  
                (acc_no,)
            )
            acc = cursor.fetchone()
            
            if acc:
                if acc[0] >= amount:
                    new_balance = acc[0] - amount   
                    
                    cursor.execute( 
                        "UPDATE accounts SET balance = ? WHERE account_no=?",
                        (new_balance,acc_no)
                    )
                    cursor.execute(
                        "INSERT INTO transactions(account_no,type,amount,date)VALUES(?,?,?,?)",
                        (    
                            acc_no,
                            "Withdraw",
                            amount,
                            datetime.now().strftime("%d-%m-%Y %H:%M")
                        )
                    )   
                    
                    conn.commit()
                    
                    result_label.config(
                        text="Withdraw Successful"
                    )
                else:
                    result_label.config(
                        text="Insufficient Balance"
                    )
            else:
                result_label.config(
                    text="Account Not Found"    
                )
        else:
            result_label.config (
                text="Amount should be positive"
            )
    except:
        result_label.config(
            text="Enter Valid Amount"
        )
    
def search_account():
    try:
        acc_no = int(entry_search.get())
        
        cursor.execute( 
            "SELECT * FROM accounts WHERE account_no=?",
            (acc_no,)
        )
        acc = cursor.fetchone()
        
        if acc:
            text_box.delete("1.0",tk.END)
            
            text_box.insert(
                tk.END,
                f"Account Found\n\n"
                f"Acc No: {acc[0]}\n"
                f"Name: {acc[1]}\n "    
                f"Balance: {acc[2]}\n"
            )
        else:
            
            result_label.config(
                text="Account Not Found"
            )
        
    except:
        result_label.config(
            text="Enter Valid Account Number"
        )
        
def transaction_history():
    try:
        acc_no = int(entry_history.get())
        text_box.delete("1.0",tk.END)
        
        #account details
        cursor.execute(
            "SELECT * FROM accounts WHERE account_no=?",
            (acc_no,)
        )
        account = cursor.fetchone()
        
        if account: 
        
            text_box.insert(
                tk.END,
                f"Account Statement\n\n"
                f"Account No: {account[0]}\n"
                f"Name: {account[1]}\n"
                f"Current Balance: {account[2]}\n\n"
                f"Transactions:\n"
            )
            
            cursor.execute(
                "SELECT * FROM transactions WHERE account_no=?",
                (acc_no,)
            )
            rows = cursor.fetchall()
            
            for t in rows:
                text_box.insert(
                    tk.END,
                    f"\nDate: {t[4]}"
                    f"\nType: {t[2]}"
                    f"\nAmount: {t[3]}"
                )
                
                text_box.insert (
                    tk.END,
                    "------------------\n"    
                )
        else:
            result_label.config(
                text="Account Not Found "
            )
    except:
        result_label.config(
            text="Enter Valid Account Number"
        )
                
            
        
def get_account_number():
    cursor.execute(
        "SELECT MAX(account_no) FROM accounts"
    )
    
    result = cursor.fetchone()
    
    if result[0] is None:
        return 101
    else:
        return result[0] + 1
    
def delete_account():
    try:
        acc_no = int(entry_delete.get())
        
        cursor.execute(
            "DELETE FROM accounts WHERE account_no=?",
            (acc_no,)
        )
        
        conn.commit()
        
        if cursor.rowcount > 0:
            result_label.config(
                text="Account Deleted Successfully"
            )
        else:
            result_label.config(
                text="Account Not Found"
            )
    except:
        result_label.config(
            text="Enter Valid Account Number"
        )

def clear_fields():
    
    entry_name.delete(0,tk.END)
    entry_balance.delete(0,tk.END)
    
    entry_acc.delete(0,tk.END)
    entry_amount.delete(0,tk.END)
    
    entry_withdraw_acc.delete(0,tk.END)
    entry_withdraw_amount.delete(0,tk.END)
    
    entry_search.delete(0,tk.END)
    entry_delete.delete(0,tk.END)
    
    result_label.config(text="Fields Cleared")
    
def login():
    
    username = entry_username.get()
    password = entry_password.get()
    
    if username == Admin_username and password == Admin_password:
        login_window.destroy()
        
        root.deiconify()
        
    else:
        login_result.config(
            text="Invalid Username or Password"
        )
        
root =tk.Tk()
root.withdraw()
root.title("Bank Management System")
root.geometry("500x700")
root.config(bg="lightgray")

title = tk.Label(
        root,
        text = "🏦 Bank Management System",       
        font = ("Arial",20,"bold"),
        bg="lightgray",
        fg = "blue"     
)
title.pack(pady=10)

button_frame = tk.Frame(root,bg="lightgray")      
button_frame.pack(pady=10)

input_frame = tk.Frame(root,bg= "lightgray")
input_frame.pack(pady=10)

#name input
tk.Label(input_frame,text="Name").grid(row=0,column=0,padx=10,pady=5)

entry_name = tk.Entry(input_frame,width=25,font=("Arial",10))
entry_name.grid(row=0,column=1,padx=10,pady=5)

#Balance input
tk.Label(input_frame,text="Balance").grid(row=1,column=0,padx=10,pady=5)

entry_balance = tk.Entry(input_frame,width=25,font=("Arial",10))
entry_balance.grid(row=1,column=1,padx=10,pady=5)

#Button
tk.Button(
    button_frame,
    text="Create Account",
    width=15,
    font=("Arial",10,"bold"),
    bg = "green",
    fg = "white",
    command=create_account
).grid(row=0, column=0,padx=5,pady=5)

#Result
result_label = tk.Label(root,text="")
result_label.pack()

#text box
text_frame = tk.Frame(root,bg="lightgray")
text_frame.pack(pady=20)

text_box = tk.Text(text_frame,height=15,width=60)
text_box.pack()

#Account Number
tk.Label(input_frame,text= "Account Number").grid(row=2,column=0,padx=10,pady=5)

entry_acc = tk.Entry(input_frame,width=25,font=("Arial",10))
entry_acc.grid(row=2,column=1,padx=10,pady=5)

#Deposit Amount
tk.Label(input_frame,text="Deposit Amount").grid(row=3,column=0,padx=10,pady=5)

entry_amount = tk.Entry(input_frame,width=25,font=("Arial",10))
entry_amount.grid(row=3 ,column=1,padx=10,pady=5)

#Withdraw Acc. no.
tk.Label(input_frame,text="Withdraw Account Number").grid(row=4,column=0,padx=10,pady=5)

entry_withdraw_acc = tk.Entry(input_frame,width=25,font=("Arial",10))
entry_withdraw_acc.grid(row=4,column=1,padx=10,pady=5)

#Withdraw Amount
tk.Label(input_frame,text="Withdraw Amount").grid(row=5,column=0,padx=10,pady=5)

entry_withdraw_amount = tk.Entry(input_frame,width=25,font=("Arial",10))
entry_withdraw_amount.grid(row=5,column=1,padx=10,pady=5)

#Search 
tk.Label(input_frame,text="Search Account Number").grid(row=6,column=0,padx=10,pady=5)

entry_search = tk.Entry(input_frame,width=25,font=("Arial",10))
entry_search.grid(row=6,column=1,padx=10,pady=5)

#Transaction History
tk.Label(input_frame,text="Transaction Account Number").grid(row=8,column=0,padx=10,pady=5)

entry_history = tk.Entry(input_frame,width=25)
entry_history.grid(row=8,column=1,padx=10,pady=5)

#Delete Account
tk.Label(input_frame,text="Delete Account Number").grid(row=7,column=0,padx=10,pady=5)

entry_delete = tk.Entry(input_frame,width=25,font=("Arial",10))
entry_delete.grid(row=7,column=1,padx=10,pady=5)

#Deposit Button
tk.Button(
    button_frame,
    text="Deposit Money",
    width=20,
    bg = "blue",
    fg = "white",
    command = deposit_money
).grid(row=0,column=1,padx=5,pady=5)

#withdraw Button
tk.Button(
    button_frame,
    text="Withdraw Money",
    width=20,
    bg = "pink",
    fg = "white",
    command=withdraw_money
).grid(row=0,column=2,padx=5,pady=5)


#Search Button
tk.Button(
    button_frame,
    text = "Search Account",
    width=20,
    bg = "orange",
    fg = "black",
    command = search_account
).grid(row=1,column=0,padx=5,pady=5)

#Transaction History
tk.Button(
    button_frame,
    text="Transaction History",
    width = 20,
    bg = "brown",
    fg = "white",
    command=transaction_history
).grid(row=2,column=1,padx=5,pady=5)
#show button
tk.Button(
    button_frame,
    text="Show Accounts",
    width=20,
    bg = "purple",
    fg = "white",
    command=show_accounts
).grid(row=1,column=1,padx=5,pady=5)

#delete button  
tk.Button(
    button_frame,
    text="Delete Account",
    width = 20,
    bg="red",
    fg="white",
    command=delete_account 
).grid(row=2,column=0,padx=5,pady=5)

#clear Button
tk.Button(
    button_frame,
    text="Clear All Fields",
    width=20,
    bg = "gray",
    fg = "white",
    command=clear_fields
).grid(row=1,column=2,padx=5,pady=5)

login_window = tk.Toplevel()
login_window.title("Bank Management Login")
login_window.geometry("400x450")
login_window.config(bg="#1e3c72")

#main frame
login_frame = tk.Frame(
    login_window,
    bg="white",
    width=320,
    height=350
)

login_frame.place(
    relx=0.5,
    rely=0.5,
    anchor="center"
)

#Title
tk.Label(
    login_frame,
    text="username",
    font=("Arial",12),
    bg="white"
).pack()

entry_username = tk.Entry(
    login_frame,
    width=25,
    font=("Arial",12)
)

entry_username.pack(
    pady=8    
)

#Password
tk.Label(
    login_frame,
    text="Password",
    font=("Arial",12),
    bg="white"
).pack()

entry_password = tk.Entry(
    login_frame,
    width=25,
    font=("Arial",12),
    show="*"    
)

entry_password.pack(
    pady=8
)

#Result
login_result = tk.Label(
    login_frame,
    text="",
    bg="white",
    fg="red",
    font=("Arial",10)
)
login_result.pack(
    pady=10 
)

#Login Button   
tk.Button(
    login_frame,
    text="LOGIN",
    width=20,
    font=("Arial",12,"bold"),
    bg='#1e3c72',    
    fg="white",
    command=login
).pack(
    pady=15
)

#footer 
tk.Label(
    login_frame,
    text="Secure Banking System",
    bg="white",
    fg="gray",
    font=("Arial",9)
).pack( )



root.mainloop()