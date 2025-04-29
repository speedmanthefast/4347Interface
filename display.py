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
    self.display_heading("Process Transaction")
    self.display_item(display_process_transaction)
    self.display_weight_row(weight=2)
