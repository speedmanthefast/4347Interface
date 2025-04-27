import tkinter as tk
import mysql.connector
from tkinter import messagebox
import restaurant

R = restaurant.Restaurant()

R.find_restaurant()

R.root.mainloop()

