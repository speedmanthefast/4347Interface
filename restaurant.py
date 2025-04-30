import tkinter as tk
import mysql.connector
from tkinter import messagebox

import display
import commands

class Restaurant:
    def __init__(self):
        self.RID = None
        self.db = mysql.connector.connect(
                host="speedman.xyz",
                user="user",
                password="password",
                database="byte_a_burger")
        self.cursor = self.db.cursor()
        self.root = tk.Tk()
        self.root.title("Restaurant Manager")
        self.root.geometry("800x800")
        self.nextRow = 0

    def clear_screen(self, window):
        for element in window.winfo_children():
            element.destroy()
        if window is self.root:
            self.nextRow = 0

    def setRID(self, RID):
        self.RID = RID

    def find_restaurant(self):
        rid_label = tk.Label(self.root, text="Enter Restaurant ID")
        rid_label.pack()
        rid_entry = tk.Entry(self.root)
        rid_entry.pack()

        def set_restaurant():
            tmp_rid = rid_entry.get()
            query = "SELECT * FROM Restaurant WHERE Restaurant_id = %s"
            self.cursor.execute(query, (tmp_rid,))
            result = self.cursor.fetchone()
            if result:
                self.setRID(tmp_rid)
                messagebox.showinfo("Restaurant Found!", "The restaurant has now been set")
                self.clear_screen(self.root)
                self.display_main_screen()
            else:
                messagebox.showinfo("Restaurant Not Found", "Please enter the ID of an existing restaurant")

        rid_button = tk.Button(self.root, text="Submit", command=set_restaurant)
        rid_button.pack()

    add_tuple = commands.add_tuple
    update_tuple = commands.update_tuple
    delete_tuple = commands.delete_tuple
    view_table = commands.view_table
    add_customer = commands.add_customer
    lookup_customer = commands.lookup_customer
    seat_customer = commands.seat_customer
    process_transaction = commands.process_transaction
    cook_food = commands.cook_food
    serve_order = commands.serve_order
    unseat_customer = commands.unseat_customer

    display_CRUD_add = display.display_CRUD_add
    display_CRUD_update = display.display_CRUD_update
    display_CRUD_delete = display.display_CRUD_delete
    display_CRUD_viewtable = display.display_CRUD_viewtable
    display_customer_lookup = display.display_customer_lookup
    display_main_screen = display.display_main_screen
    display_process_transaction=display.display_process_transaction
    display_seat_customer = display.display_seat_customer
    display_cook_food = display.display_cook_food
    display_serve_order = display.display_serve_order
    display_unseat_customer = display.display_unseat_customer

    def display_item(self, func, row=None, col=1):
        if row is None:
            row = self.nextRow
        func(self, row, col)
        if row == self.nextRow:
            self.nextRow = self.nextRow + 1

    def display_weight_row(self, row=None, weight=1):
        if row is None:
            row = self.nextRow
        self.root.grid_rowconfigure(row, weight=weight)
        if row == self.nextRow:
            self.nextRow = self.nextRow + 1

    def display_pad_row(self, row=None, minsize=20):
        if row is None:
            row = self.nextRow
        self.root.grid_rowconfigure(row, minsize=minsize)
        if row == self.nextRow:
            self.nextRow = self.nextRow + 1

    def display_weight_col(self, col, weight=1):
        self.root.grid_columnconfigure(col, weight=weight)

    def display_heading(self, text, size=10, row=None, col=1):
        if row is None:
            row = self.nextRow
        tk.Label(self.root, text=text, font=("Arial", size, "bold")).grid(row=row, column=col, columnspan=3, pady=10)
        if row == self.nextRow:
            self.nextRow = self.nextRow + 1



