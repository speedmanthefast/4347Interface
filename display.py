import tkinter as tk
import mysql.connector
from tkinter import messagebox

def display_CRUD_add(self, row, col):

    add_label = tk.Label(self.root, text="Select Table:").grid(row=row, column=col, sticky="e")

    self.cursor.execute("SHOW TABLES")
    tables = self.cursor.fetchall()
    tables_f = [table[0] for table in tables]

    # Tkinter variable to store the selected value
    variable = tk.StringVar()
    variable.set(tables_f[0])  # Set the default option

    # Create the drop-down menu
    dropdown = tk.OptionMenu(self.root, variable, *tables_f)
    dropdown.grid(row=row, column=col+1, sticky="w")

    # Add tuple button
    tk.Button(self.root, text="Add Tuple", command=lambda: self.add_tuple(variable.get())).grid(row=row, column=col+2, sticky="w")

def display_CRUD_update(self, row, col):

    add_label = tk.Label(self.root, text="Select Table:").grid(row=row, column=col, sticky="e")

    self.cursor.execute("SHOW TABLES")
    tables = self.cursor.fetchall()
    tables_f = [table[0] for table in tables]

    # Tkinter variable to store the selected value
    variable = tk.StringVar()
    variable.set(tables_f[0])  # Set the default option

    # Create the drop-down menu
    dropdown = tk.OptionMenu(self.root, variable, *tables_f)
    dropdown.grid(row=row, column=col+1, sticky="w")

    # Add tuple button
    tk.Button(self.root, text="Update Tuple", command=lambda: self.update_tuple(variable.get())).grid(row=row, column=col+2, sticky="w")

def display_CRUD_delete(self, row, col):
    add_label = tk.Label(self.root, text="Select Table:").grid(row=row, column=col, sticky="e")

    self.cursor.execute("SHOW TABLES")
    tables = self.cursor.fetchall()
    tables_f = [table[0] for table in tables]

    # Tkinter variable to store the selected value
    variable = tk.StringVar()
    variable.set(tables_f[0])  # Set the default option

    # Create the drop-down menu
    dropdown = tk.OptionMenu(self.root, variable, *tables_f)
    dropdown.grid(row=row, column=col+1, sticky="w")

    # Add tuple button
    tk.Button(self.root, text="Delete Tuple", command=lambda: self.delete_tuple(variable.get())).grid(row=row, column=col+2, sticky="w")

def display_CRUD_viewtable(self, row, col):
    add_label = tk.Label(self.root, text="Select Table:").grid(row=row, column=col, sticky="e")

    self.cursor.execute("SHOW TABLES")
    tables = self.cursor.fetchall()
    tables_f = [table[0] for table in tables]

    # Tkinter variable to store the selected value
    variable = tk.StringVar()
    variable.set(tables_f[0])  # Set the default option

    # Create the drop-down menu
    dropdown = tk.OptionMenu(self.root, variable, *tables_f)
    dropdown.grid(row=row, column=col+1, sticky="w")

    # Add tuple button
    tk.Button(self.root, text="View Table", command=lambda: self.view_table(variable.get())).grid(row=row, column=col+2, sticky="w")

def display_customer_lookup(self, row, col):
    phone_label = tk.Label(self.root, text="Phone Number:").grid(row=row, column=col)
    phone_entry = tk.Entry(self.root)
    phone_entry.grid(row=row, column=col+1)
    tk.Button(self.root, text="Search", command=lambda: self.lookup_customer(phone_entry)).grid(row=row, column=col+2)

def display_process_transaction(self, row, col):
    tk.Button(self.root, text="Begin", command=lambda: self.process_transaction()).grid(row=row, column=col, columnspan=3)

def display_seat_customer(self, row, col):
    phone_label = tk.Label(self.root, text="Phone Number:").grid(row=row, column=col)
    phone_entry = tk.Entry(self.root)
    phone_entry.grid(row=row, column=col+1)
    def submit():
        phone = phone_entry.get()
        query = "SELECT * FROM Customer WHERE Phone_number = %s"
        self.cursor.execute(query, (phone,))
        result = self.cursor.fetchone()
        if result:
            self.seat_customer(phone)
        else:
            messagebox.showinfo("Customer Not Found")

    tk.Button(self.root, text="Search", command=submit).grid(row=row, column=col+2)

def display_cook_food(self, row, col):
    phone_label = tk.Label(self.root, text="Phone Number:").grid(row=row, column=col)
    phone_entry = tk.Entry(self.root)
    phone_entry.grid(row=row, column=col+1)
    tk.Button(self.root, text="Search", command=lambda: self.cook_food(phone_entry.get())).grid(row=row, column=col+2)

def display_serve_order(self, row, col):
    phone_label = tk.Label(self.root, text="Phone Number:").grid(row=row, column=col)
    phone_entry = tk.Entry(self.root)
    phone_entry.grid(row=row, column=col+1)
    tk.Button(self.root, text="Search", command=lambda: self.serve_order(phone_entry.get())).grid(row=row, column=col+2)

def display_unseat_customer(self, row, col):
    phone_label = tk.Label(self.root, text="Phone Number:").grid(row=row, column=col)
    phone_entry = tk.Entry(self.root)
    phone_entry.grid(row=row, column=col+1)
    tk.Button(self.root, text="Search", command=lambda: self.unseat_customer(phone_entry.get())).grid(row=row, column=col+2)

def display_main_screen(self):
    self.display_weight_col(0)
    self.display_weight_col(5)
    self.display_pad_row()
    self.display_heading("CRUD Functions")
    self.display_item(display_CRUD_add)
    self.display_item(display_CRUD_update)
    self.display_item(display_CRUD_delete)
    self.display_item(display_CRUD_viewtable)
    self.display_pad_row()
    self.display_heading("Customer Lookup")
    self.display_item(display_customer_lookup)
    self.display_pad_row()
    self.display_heading("Seat Customer")
    self.display_item(display_seat_customer)
    self.display_pad_row()
    self.display_heading("Cook Food")
    self.display_item(display_cook_food)
    self.display_pad_row()
    self.display_heading("Serve Customer")
    self.display_item(display_serve_order)
    self.display_pad_row()
    self.display_heading("Clean Table")
    self.display_item(display_unseat_customer)
    self.display_pad_row()
    self.display_heading("Process Transaction")
    self.display_item(display_process_transaction)
    self.display_weight_row(weight=2)
