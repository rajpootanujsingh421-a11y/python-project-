import tkinter as tk
from tkinter import messagebox
import sqlite3
from tkinter import ttk

# Database connection function
def connect_db():
    conn = sqlite3.connect('blood_bank.db')
    return conn

# Function to add a donor
def add_donor():
    name = entry_name.get()
    blood_type = entry_blood_type.get()
    age = entry_age.get()
    contact = entry_contact.get()
    last_donated = entry_last_donated.get()

    if not name or not blood_type or not age or not contact or not last_donated:
        messagebox.showwarning("Input Error", "All fields must be filled.")
        return

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO donors (name, blood_type, age, contact, last_donated)
    VALUES (?, ?, ?, ?, ?)
    ''', (name, blood_type, age, contact, last_donated))

    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Donor added successfully!")
    clear_fields()

# Function to add a blood request
def add_blood_request():
    patient_name = entry_patient_name.get()
    blood_type = entry_blood_type_request.get()
    quantity = entry_quantity.get()

    if not patient_name or not blood_type or not quantity:
        messagebox.showwarning("Input Error", "All fields must be filled.")
        return

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO blood_requests (patient_name, blood_type, quantity, date_requested)
    VALUES (?, ?, ?, DATE('now'))
    ''', (patient_name, blood_type, quantity))

    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Blood request added successfully!")
    clear_fields_request()

# Function to view donor records
def view_donors():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM donors")
    rows = cursor.fetchall()

    display_table(rows, "Donors")
    conn.close()

# Function to view blood request records
def view_blood_requests():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM blood_requests")
    rows = cursor.fetchall()

    display_table(rows, "Blood Requests")
    conn.close()

# Function to display records in a new window
def display_table(rows, record_type):
    table_window = tk.Toplevel()
    table_window.title(f"{record_type} Records")

    tree = ttk.Treeview(table_window, columns=("ID", "Name/Blood Type", "Age/Quantity", "Contact/Date", "Last Donated/Patient"))
    tree.heading("#1", text="ID")
    tree.heading("#2", text="Name/Blood Type")
    tree.heading("#3", text="Age/Quantity")
    tree.heading("#4", text="Contact/Date")
    tree.heading("#5", text="Last Donated/Patient")

    tree.column("#1", width=50)
    tree.column("#2", width=150)
    tree.column("#3", width=100)
    tree.column("#4", width=150)
    tree.column("#5", width=150)

    for row in rows:
        tree.insert("", tk.END, values=row)

    tree.pack(expand=True, fill=tk.BOTH)

# Function to clear donor fields
def clear_fields():
    entry_name.delete(0, tk.END)
    entry_blood_type.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_contact.delete(0, tk.END)
    entry_last_donated.delete(0, tk.END)

# Function to clear blood request fields
def clear_fields_request():
    entry_patient_name.delete(0, tk.END)
    entry_blood_type_request.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)

# Tkinter GUI setup
root = tk.Tk()
root.title("Blood Bank Management System")

# Donor Information Section
frame_donor = tk.LabelFrame(root, text="Add Donor Information", padx=10, pady=10)
frame_donor.grid(row=0, column=0, padx=10, pady=10)

tk.Label(frame_donor, text="Name:").grid(row=0, column=0)
entry_name = tk.Entry(frame_donor)
entry_name.grid(row=0, column=1)

tk.Label(frame_donor, text="Blood Type:").grid(row=1, column=0)
entry_blood_type = tk.Entry(frame_donor)
entry_blood_type.grid(row=1, column=1)

tk.Label(frame_donor, text="Age:").grid(row=2, column=0)
entry_age = tk.Entry(frame_donor)
entry_age.grid(row=2, column=1)

tk.Label(frame_donor, text="Contact:").grid(row=3, column=0)
entry_contact = tk.Entry(frame_donor)
entry_contact.grid(row=3, column=1)

tk.Label(frame_donor, text="Last Donated (YYYY-MM-DD):").grid(row=4, column=0)
entry_last_donated = tk.Entry(frame_donor)
entry_last_donated.grid(row=4, column=1)

btn_add_donor = tk.Button(frame_donor, text="Add Donor", command=add_donor)
btn_add_donor.grid(row=5, columnspan=2)

# Blood Request Section
frame_request = tk.LabelFrame(root, text="Add Blood Request", padx=10, pady=10)
frame_request.grid(row=0, column=1, padx=10, pady=10)

tk.Label(frame_request, text="Patient Name:").grid(row=0, column=0)
entry_patient_name = tk.Entry(frame_request)
entry_patient_name.grid(row=0, column=1)

tk.Label(frame_request, text="Blood Type:").grid(row=1, column=0)
entry_blood_type_request = tk.Entry(frame_request)
entry_blood_type_request.grid(row=1, column=1)

tk.Label(frame_request, text="Quantity (Units):").grid(row=2, column=0)
entry_quantity = tk.Entry(frame_request)
entry_quantity.grid(row=2, column=1)

btn_add_request = tk.Button(frame_request, text="Add Blood Request", command=add_blood_request)
btn_add_request.grid(row=3, columnspan=2)

# Buttons to view records
btn_view_donors = tk.Button(root, text="View Donors", command=view_donors)
btn_view_donors.grid(row=1, column=0, padx=10, pady=10)

btn_view_requests = tk.Button(root, text="View Blood Requests", command=view_blood_requests)
btn_view_requests.grid(row=1, column=1, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
