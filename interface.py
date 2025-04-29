import tkinter as tk
import mysql.connector
from tkinter import messagebox
import restaurant

R = restaurant.Restaurant()

R.display_main_screen()

R.root.mainloop()

# Shit to add maybe
#     Additional functions:
#         Seat customer
#         Take order
#         'Cook' Food
#         Serve Order
#         Clean table
#         Check Status of robots, check stock of ingredients
#     Improve input method for transaction processing
#     Styling
#     Input validation
#     Input auto drop downs
