""" 
Broderick Clapper

GUI application
Description: This is a GUI application that has 3 different winds. There is a start up welcome windw, a shopping
window, and then a checkout window. The application walks the user through purchasing football gear.

Pseudocode:
Main Program
    import tkinter and ttk

    define global variables
        cart
        product data

    intialize main app window
    Define functions
        show_main_window
        diplay main screen
        dhow product screen
            display products
            list product with images and prices
            add to cart button for each product

        show checkout screen
            display checkout window
            show summart of items
            inpu fields for name and payment
            submit order button

product window
    define cart product functions
    define submit order function
        validates inputs
        if valid - clear cart and show a success message
        if invlaid - display error message

GUI components
    main window
        welcome message
        start shopping button

    product screen
        add a list of products
        add "add to cart" button
        add "back" button to return to main window

    Checkout Screen
        display order summary
        add input fields for user details
        add "submit" button for order

Start main_window

"""
# Import necessary libraries
# tkinter: GUI framework for creating the application
# ttk: Additional set of themed widgets for tkinter
# messagebox: For displaying pop-up messages
import tkinter as tk
from tkinter import ttk, messagebox

# Product data: List of dictionaries containing product details like name, price, and image file
# Each product in the list has a name, price, and a corresponding image file
products = [
    {"name": "Football Helmet", "price": 120.0, "image": "helmets.png"},  # Product 1 details
    {"name": "Football Gloves", "price": 40.0, "image": "glove.png"},     # Product 2 details
    {"name": "Football Cleats", "price": 100.0, "image": "cleats.png"},   # Product 3 details
]


# Cart: List to store the products that the user adds to their cart.
# This will be used to summarize the products at checkout.
cart = []

# Function: show_main_window
# This function displays the main window and hides all other windows.
def show_main_window():
    hide_all_windows()  # Hide all windows first
    main_window.deiconify()  # Show the main window

# Function: show_product_screen
# This function shows the product selection window and hides all other windows.
def show_product_screen():
    hide_all_windows()  # Hide all windows first
    product_window.deiconify()  # Show the product window

# Function: show_checkout_screen
# This function shows the checkout window and hides all other windows. 
# It also updates the cart summary to reflect the current items in the cart.
def show_checkout_screen():
    hide_all_windows()  # Hide all windows first
    checkout_window.deiconify()  # Show the checkout window
    update_cart_summary()  # Update the cart summary with the current items in the cart

# Function: hide_all_windows
# This function hides all windows in the application. It is called whenever we need to switch between screens.
def hide_all_windows():
    main_window.withdraw()  # Hide the main window
    product_window.withdraw()  # Hide the product window
    checkout_window.withdraw()  # Hide the checkout window

# Function: add_to_cart
# This function adds the selected product to the cart and shows a pop-up message confirming the addition.
def add_to_cart(product):
    cart.append(product)  # Add the selected product to the cart list
    messagebox.showinfo("Cart Update", f"{product['name']} has been added to your cart!")  # Show confirmation message

# Function: update_cart_summary
# This function updates the cart summary to show the list of items and total price in the checkout window.
def update_cart_summary():
    cart_summary_text = ""  # Initialize the cart summary text as an empty string
    total_price = 0  # Initialize the total price to 0

    # Loop through each item in the cart and update the summary
    for item in cart:
        cart_summary_text += f"{item['name']} - ${item['price']:.2f}\n"  # Add item name and price to summary
        total_price += item["price"]  # Add the item's price to the total price

    cart_summary_label.config(text=cart_summary_text)  # Update the cart summary label with the new summary
    total_price_label.config(text=f"Total: ${total_price:.2f}")  # Update the total price label

# Function: submit_order
# This function is called when the user submits the order at checkout. It validates the input and clears the cart if successful.
def submit_order():
    # Validate if the name field is empty
    if not name_entry.get().strip():
        messagebox.showerror("Input Error", "Please enter your name.")  # Show error if name is empty
        return

    # Validate if the payment field contains only digits
    if not payment_entry.get().strip().isdigit():
        messagebox.showerror("Input Error", "Please enter a valid payment number.")  # Show error if payment is invalid
        return

    messagebox.showinfo("Order Submitted", "Thank you for your purchase!")  # Show confirmation message
    cart.clear()  # Clear the cart after the order is submitted
    show_main_window()  # Return to the main window
    
# Main Window with welcome message
#Create main windwo and set up the intial interface
#this will set the window title and window size
main_window = tk.Tk()
main_window.title("Football Pro Shop")
main_window.geometry("400x300")

#Label in the main window with welcome message
welcome_label = ttk.Label(main_window, text="Welcome to Football Pro Shop!", font=("Arial", 16))
welcome_label.pack(pady=20)

#button to start shopping that will open the product selection window
start_button = ttk.Button(main_window, text="Start Shopping", command=show_product_screen)
start_button.pack(pady=10)

# Product window with product display
product_window = tk.Toplevel(main_window)
product_window.title("Product Selection")
product_window.geometry("400x400")
product_window.withdraw()

#Label for the product selection window
product_label = ttk.Label(product_window, text="Choose Your Football Gear", font=("Arial", 16))
product_label.pack(pady=10)

# dictionary for images
#Loop through the products list and display each product with its image, name, and price
product_images = {}

for product in products:
    product_frame = ttk.Frame(product_window, padding=10)
    product_frame.pack(fill="x") #Pack each product frame to fill horizontally

    # Load and scale down the product image
    product_images[product["name"]] = tk.PhotoImage(file=product["image"]).subsample(4, 4)  # Adjust subsample values as needed
    product_image_label = ttk.Label(product_frame, image=product_images[product["name"]])
    product_image_label.pack(side="left", padx=5)

    # Display product name and price
    product_name = ttk.Label(product_frame, text=product["name"])
    product_name.pack(side="left", padx=5)

    #Create label for displaying the product image
    product_price = ttk.Label(product_frame, text=f"${product['price']:.2f}")
    product_price.pack(side="left", padx=10)

    # Add to cart button
    add_button = ttk.Button(product_frame, text="Add to Cart", command=lambda p=product: add_to_cart(p))
    add_button.pack(side="right")


product_back_button = ttk.Button(product_window, text="Go to Checkout", command=show_checkout_screen)
product_back_button.pack(pady=20)

# Checkout window with order summary, entry field of name, and order button to submit
checkout_window = tk.Toplevel(main_window) 
checkout_window.title("Checkout") #Set window title
checkout_window.geometry("400x400") #Set window size 
checkout_window.withdraw()

#label for checkout Screen
checkout_label = ttk.Label(checkout_window, text="Order Summary", font=("Arial", 16))
checkout_label.pack(pady=10)

#Label for displaying the cart summary
cart_summary_label = ttk.Label(checkout_window, text="", justify="left")
cart_summary_label.pack(pady=10)

#Label for displaying total price
total_price_label = ttk.Label(checkout_window, text="Total: $0.00", font=("Arial", 16))
total_price_label.pack(pady=10)

#Entry fields for name and payment information
name_label = ttk.Label(checkout_window, text="Name:")
name_label.pack(pady=5)
name_entry = ttk.Entry(checkout_window)
name_entry.pack(pady=5)

#Labels for payments
payment_label = ttk.Label(checkout_window, text="Payment (Card Number):")
payment_label.pack(pady=5)
payment_entry = ttk.Entry(checkout_window)
payment_entry.pack(pady=5)

#Button to submit order
submit_button = ttk.Button(checkout_window, text="Submit Order", command=submit_order)
submit_button.pack(pady=10)

#button to go back to main window
checkout_back_button = ttk.Button(checkout_window, text="Back to Main", command=show_main_window)
checkout_back_button.pack(pady=10)

# Start the application
main_window.mainloop() 
