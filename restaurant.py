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
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(5, weight=1)
        self.root.grid_rowconfigure(7, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(5, weight=1)
        self.root.title("Restaurant Manager")
        self.root.geometry("800x600")

    def clear_screen(self, window):
        for element in window.winfo_children():
            element.destroy()

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

    display_CRUD_add = display.display_CRUD_add
    display_CRUD_update = display.display_CRUD_update
    display_CRUD_delete = display.display_CRUD_delete
    display_CRUD_viewtable = display.display_CRUD_viewtable
    display_customer_lookup = display.display_customer_lookup
    display_main_screen = display.display_main_screen


