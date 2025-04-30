import tkinter as tk
import mysql.connector
from tkinter import messagebox
import restaurant

R = restaurant.Restaurant()

R.display_main_screen()

R.root.mainloop()

# Shit to add maybe
#     Additional functions:
#         'add food to order'
#
#     Improve input method for transaction processing
#     Styling
#     Input validation
#     Input auto drop downs
