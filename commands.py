import tkinter as tk
import mysql.connector
from tkinter import messagebox
from tkinter import ttk

def add_tuple(self, table_name):
    new_win = tk.Toplevel(self.root)
    new_win.title("Add new tuple")

    self.cursor.execute(f"DESCRIBE `{table_name}`")
    columns = self.cursor.fetchall()
    height = max(len(columns) * 50, 200)
    new_win.geometry(f"300x{height}")

    entry_widgets = {}

    for col in columns:
        col_name = col[0]
        # Skip auto-increment ID
        if 'auto_increment' in col[-1]:
            continue

        label = tk.Label(new_win, text=col_name)
        label.pack()

        entry = tk.Entry(new_win)
        entry.pack()

        entry_widgets[col_name] = entry

    def submit():
        values = []
        fields = []
        for col_name, entry in entry_widgets.items():
            fields.append(col_name)
            values.append(entry.get())

        sql = f"INSERT INTO `{table_name}` ({', '.join(fields)}) VALUES ({', '.join(['%s']*len(fields))})"
        self.cursor.execute(sql, values)
        self.db.commit()
        tk.messagebox.showinfo("Success", f"Record added to {table_name}!")

    submit_button = tk.Button(new_win, text="Add Record", command=submit)
    submit_button.pack()

def update_tuple(self, table_name):

    # Create new window
    new_win = tk.Toplevel(self.root)
    new_win.title("Update tuple")
    new_win.geometry("300x200")

    # Dictionary to store entry boxes
    entry_widgets = {}

    # Get the list of columns from the chosen table
    self.cursor.execute(f"DESCRIBE `{table_name}`")
    columns = self.cursor.fetchall()

    # Get the name of the first column
    col_key = columns[0][0]

    # Create a label and entry box for searching by key value
    key_label = tk.Label(new_win, text=col_key)
    key_label.pack()
    key_entry = tk.Entry(new_win)
    key_entry.pack()
    entry_widgets[0] = key_entry

    # Function to search for the value inside key_entry
    def find_tuple():
        query = f"SELECT * FROM `{table_name}` WHERE {col_key} = %s"
        self.cursor.execute(query, (key_entry.get(),))
        result = self.cursor.fetchone()
        if result:
            height = max(len(columns) * 50, 200)
            new_win.geometry(f"300x{height + 20}")

            # Create a label and entry for each attribute
            count = 0
            for col in columns:
                col_name = col[0]
                if col == columns[0]:
                    count = count + 1
                    continue

                label = tk.Label(new_win, text=col_name)
                label.pack()

                entry_text = tk.StringVar()
                entry_text.set(result[count])
                entry = tk.Entry(new_win, textvariable=entry_text)
                entry.pack()

                entry_widgets[col_name] = entry
                count = count + 1

            # Function call for submitting the update parameters
            def submit():

                # Get the values stored in each entry table
                values = []
                for col_name, entry in entry_widgets.items():
                    values.append(entry.get())

                sql = f"UPDATE {table_name} SET {', '.join(f"{attr[0]} = \'{value}\'" for attr, value in zip(columns, values))} WHERE {col_key} = {key_entry.get()}"
                print(sql)
                self.cursor.execute(sql)
                self.db.commit()
                tk.messagebox.showinfo("Success", f"Record updated in {table_name}!")
                new_win.destroy()

            submit_button = tk.Button(new_win, text="Update Record", command=submit)
            submit_button.pack()
        else:
            messagebox.showinfo("Error", "Tuple not found")
    tk.Button(new_win, text="Search", command=find_tuple).pack()

    #height = max(len(columns) * 50, 200)
    #new_win.geometry(f"300x{height}")

def delete_tuple(self, table_name):

    # Create new window
    new_win = tk.Toplevel(self.root)
    new_win.title("Delete tuple")
    new_win.geometry("300x200")

    # Get the list of columns from the chosen table
    self.cursor.execute(f"DESCRIBE `{table_name}`")
    columns = self.cursor.fetchall()

    # Get the name of the first column
    col_key = columns[0][0]

    # Create a label and entry box for searching by key value
    key_label = tk.Label(new_win, text=col_key)
    key_label.pack()
    key_entry = tk.Entry(new_win)
    key_entry.pack()

    # Function to search for the value inside key_entry
    def find_tuple():
        query = f"SELECT * FROM `{table_name}` WHERE {col_key} = %s"
        self.cursor.execute(query, (key_entry.get(),))
        result = self.cursor.fetchone()

        if result:
            sql = f"DELETE FROM `{table_name}` WHERE `{col_key}` = %s"
            self.cursor.execute(sql, (key_entry.get(),))
            self.db.commit()
            tk.messagebox.showinfo("Success", f"Record deleted from {table_name}!")
            new_win.destroy()

        else:
            messagebox.showinfo("Error", "Tuple not found")
    tk.Button(new_win, text="Delete", command=find_tuple).pack()

def view_table(self, table_name):
    # Create new window
    new_win = tk.Toplevel(self.root)
    new_win.title(f"{table_name} View")
    new_win.geometry("800x600")

    # Get the list of columns from the chosen table
    self.cursor.execute(f"DESCRIBE `{table_name}`")
    columns = self.cursor.fetchall()

    # Create the Treeview widget
    tree = ttk.Treeview(new_win)
    tree.pack(padx=20, pady=20)

    col_names_list = []
    for col in columns:
         col_names_list.append(col[0])

    tree["columns"] = col_names_list
    tree["show"] = "headings"

    for name in col_names_list:
        tree.heading(name, text=name)

    self.cursor.execute(f"SELECT * FROM `{table_name}`")
    rows = self.cursor.fetchall()

    for row in rows:
        tree.insert("", "end", values=row)

def add_customer(self, phone):
    new_win = tk.Toplevel(self.root)
    new_win.title("Add New Customer")
    new_win.geometry("300x200")

    tk.Label(new_win, text="Name:").grid(row=0, column=0)
    name_entry = tk.Entry(new_win)
    name_entry.grid(row=0, column=1, sticky="n")

    def insert_customer():
        name = name_entry.get()
        status = "waiting"
        restaurant = "R0001"

        insert_query = """
        INSERT INTO Customer VALUES (%s, %s, %s, %s, %s)
        """
        self.cursor.execute(insert_query, (phone, name, status, restaurant, None))
        self.db.commit()
        messagebox.showinfo("Success", "Customer added!")
        new_win.destroy()

    tk.Button(new_win, text="Submit", command=insert_customer).grid(row="0", column="3", padx=5)

def lookup_customer(self, phone_entry):
    phone = phone_entry.get()
    query = "SELECT * FROM Customer WHERE Phone_number = %s"
    self.cursor.execute(query, (phone,))
    result = self.cursor.fetchone()
    if result:
        messagebox.showinfo("Customer Found", f"Name: {result[1]}\nStatus: {result[2]}\nTable: {result[4]}")
    else:
        self.add_customer(phone)
