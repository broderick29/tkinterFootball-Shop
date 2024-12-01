"""
Broderick Clapper

GUI application

"""
#import tkinter and messagebox for pop up messages
import tkinter as tk
from tkinter import ttk, messagebox

# Product data list
"""used image_alt as I have not inserted pictures yet"""
products = [
    {"name": "Football Helmet", "price": 120.0, "image_alt": "Helmet Image"},
    {"name": "Football Gloves", "price": 40.0, "image_alt": "Gloves Image"},
    {"name": "Football Cleats", "price": 100.0, "image_alt": "Cleats Image"},
]

# Cart list to store selected items
cart = []

# Functions:
#main window
def show_main_window():
    hide_all_windows()
    main_window.deiconify()

#product selection window
def show_product_screen():
    hide_all_windows()
    product_window.deiconify()

#checkout window
def show_checkout_screen():
    hide_all_windows()
    checkout_window.deiconify()
    update_cart_summary()

#Hide other windows function
def hide_all_windows():
    main_window.withdraw()
    product_window.withdraw()
    checkout_window.withdraw()

#Add to cart
def add_to_cart(product):
    cart.append(product)
    messagebox.showinfo("Cart Update", f"{product['name']} has been added to your cart!")

#Cart update function
def update_cart_summary():
    cart_summary_text = ""
    total_price = 0
    for item in cart:
        cart_summary_text += f"{item['name']} - ${item['price']:.2f}\n"
        total_price += item["price"]

    cart_summary_label.config(text=cart_summary_text)
    total_price_label.config(text=f"Total: ${total_price:.2f}")

#Check inputs and show errors
def submit_order():
    if not name_entry.get().strip():
        messagebox.showerror("Input Error", "Please enter your name.")
        return
    if not payment_entry.get().strip().isdigit():
        messagebox.showerror("Input Error", "Please enter a valid payment number.")
        return

    messagebox.showinfo("Order Submitted", "Thank you for your purchase!")
    cart.clear()
    show_main_window()

# Main Window with welcome message
main_window = tk.Tk()
main_window.title("Football Pro Shop")
main_window.geometry("400x300")

welcome_label = ttk.Label(main_window, text="Welcome to Football Pro Shop!", font=("Arial", 16))
welcome_label.pack(pady=20)

start_button = ttk.Button(main_window, text="Start Shopping", command=show_product_screen)
start_button.pack(pady=10)

# Product window with product display
product_window = tk.Toplevel(main_window)
product_window.title("Product Selection")
product_window.geometry("400x400")
product_window.withdraw()

product_label = ttk.Label(product_window, text="Choose Your Football Gear", font=("Arial", 16))
product_label.pack(pady=10)

for product in products:
    product_frame = ttk.Frame(product_window, padding=10)
    product_frame.pack(fill="x")

    product_name = ttk.Label(product_frame, text=product["name"])
    product_name.pack(side="left")

    product_price = ttk.Label(product_frame, text=f"${product['price']:.2f}")
    product_price.pack(side="left", padx=10)

    add_button = ttk.Button(product_frame, text="Add to Cart", command=lambda p=product: add_to_cart(p))
    add_button.pack(side="right")

product_back_button = ttk.Button(product_window, text="Go to Checkout", command=show_checkout_screen)
product_back_button.pack(pady=20)

# Checkout window with order summary, entry field of name, and order button to submit
checkout_window = tk.Toplevel(main_window)
checkout_window.title("Checkout")
checkout_window.geometry("400x400")
checkout_window.withdraw()

checkout_label = ttk.Label(checkout_window, text="Order Summary", font=("Arial", 16))
checkout_label.pack(pady=10)

cart_summary_label = ttk.Label(checkout_window, text="", justify="left")
cart_summary_label.pack(pady=10)

total_price_label = ttk.Label(checkout_window, text="Total: $0.00", font=("Arial", 16))
total_price_label.pack(pady=10)

name_label = ttk.Label(checkout_window, text="Name:")
name_label.pack(pady=5)
name_entry = ttk.Entry(checkout_window)
name_entry.pack(pady=5)

payment_label = ttk.Label(checkout_window, text="Payment (Card Number):")
payment_label.pack(pady=5)
payment_entry = ttk.Entry(checkout_window)
payment_entry.pack(pady=5)

submit_button = ttk.Button(checkout_window, text="Submit Order", command=submit_order)
submit_button.pack(pady=10)

checkout_back_button = ttk.Button(checkout_window, text="Back to Main", command=show_main_window)
checkout_back_button.pack(pady=10)

# Start the application
main_window.mainloop()
