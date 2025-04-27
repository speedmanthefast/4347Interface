import tkinter as tk
import mysql.connector
from tkinter import messagebox

def display_CRUD_add(self, row):

    add_label = tk.Label(self.root, text="Select Table:").grid(row=row, column=1, sticky="e")

    self.cursor.execute("SHOW TABLES")
    tables = self.cursor.fetchall()
    tables_f = [table[0] for table in tables]

    # Tkinter variable to store the selected value
    variable = tk.StringVar()
    variable.set(tables_f[0])  # Set the default option

    # Create the drop-down menu
    dropdown = tk.OptionMenu(self.root, variable, *tables_f)
    dropdown.grid(row=row, column=2, sticky="w")

    # Add tuple button
    tk.Button(self.root, text="Add Tuple", command=lambda: self.add_tuple(variable.get())).grid(row=row, column=3, sticky="w")

def display_CRUD_update(self, row):

    add_label = tk.Label(self.root, text="Select Table:").grid(row=row, column=1, sticky="e")

    self.cursor.execute("SHOW TABLES")
    tables = self.cursor.fetchall()
    tables_f = [table[0] for table in tables]

    # Tkinter variable to store the selected value
    variable = tk.StringVar()
    variable.set(tables_f[0])  # Set the default option

    # Create the drop-down menu
    dropdown = tk.OptionMenu(self.root, variable, *tables_f)
    dropdown.grid(row=row, column=2, sticky="w")

    # Add tuple button
    tk.Button(self.root, text="Update Tuple", command=lambda: self.update_tuple(variable.get())).grid(row=row, column=3, sticky="w")

def display_CRUD_delete(self, row):
    add_label = tk.Label(self.root, text="Select Table:").grid(row=row, column=1, sticky="e")

    self.cursor.execute("SHOW TABLES")
    tables = self.cursor.fetchall()
    tables_f = [table[0] for table in tables]

    # Tkinter variable to store the selected value
    variable = tk.StringVar()
    variable.set(tables_f[0])  # Set the default option

    # Create the drop-down menu
    dropdown = tk.OptionMenu(self.root, variable, *tables_f)
    dropdown.grid(row=row, column=2, sticky="w")

    # Add tuple button
    tk.Button(self.root, text="Delete Tuple", command=lambda: self.delete_tuple(variable.get())).grid(row=row, column=3, sticky="w")

def display_CRUD_viewtable(self, row):
    add_label = tk.Label(self.root, text="Select Table:").grid(row=row, column=1, sticky="e")

    self.cursor.execute("SHOW TABLES")
    tables = self.cursor.fetchall()
    tables_f = [table[0] for table in tables]

    # Tkinter variable to store the selected value
    variable = tk.StringVar()
    variable.set(tables_f[0])  # Set the default option

    # Create the drop-down menu
    dropdown = tk.OptionMenu(self.root, variable, *tables_f)
    dropdown.grid(row=row, column=2, sticky="w")

    # Add tuple button
    tk.Button(self.root, text="View Table", command=lambda: self.view_table(variable.get())).grid(row=row, column=3, sticky="w")

def display_customer_lookup(self, row):
    phone_label = tk.Label(self.root, text="Phone Number:").grid(row=row, column=1)
    phone_entry = tk.Entry(self.root)
    phone_entry.grid(row=row, column=2)
    tk.Button(self.root, text="Search", command=lambda: self.lookup_customer(phone_entry)).grid(row=row, column=3)

def display_main_screen(self):
    self.display_CRUD_add(1)
    self.display_CRUD_update(2)
    self.display_CRUD_delete(3)
    self.display_CRUD_viewtable(4)
    self.display_customer_lookup(6)
