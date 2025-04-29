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
#         Process transaction
#     Styling
#     Input validation
#     Input auto drop downs
