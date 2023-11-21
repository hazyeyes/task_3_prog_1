import tkinter as tk

def on_button_order_fruits():

    label.grid_forget()
    label_options.grid_forget()
    button.grid_forget()

    label_personal_info_details.grid(row=0, column=0, columnspan=2, pady=5)
    
    name_label.grid(row=1, column=0, pady=5, sticky=tk.E)
    name_entry.grid(row=1, column=1, pady=5, sticky=tk.W)

    contact_label.grid(row=2, column=0, pady=5, sticky=tk.E)
    contact_entry.grid(row=2, column=1, pady=5, sticky=tk.W)

    email_label.grid(row=3, column=0, pady=5, sticky=tk.E)
    email_entry.grid(row=3, column=1, pady=5, sticky=tk.W)

    address_label.grid(row=4, column=0, pady=5, sticky=tk.E)
    address_entry.grid(row=4, column=1, pady=5, sticky=tk.W)

    proceed_button.grid(row=5, column=0, columnspan=2, pady=5)

def on_button_proceed():
    label_personal_info_details.grid_forget()
    name_label.grid_forget()
    name_entry.grid_forget()
    contact_label.grid_forget()
    contact_entry.grid_forget()
    email_label.grid_forget()
    email_entry.grid_forget()
    address_label.grid_forget()
    address_entry.grid_forget()
    proceed_button.grid_forget()

    label_order_information.grid(row=0, column=0, columnspan=2, pady=5)

    product_1_label.grid(row=1, column=0, pady=5, sticky=tk.W)
    quantity_entry_apple.grid(row=1, column=1, pady=5, sticky=tk.W)
    minus.grid(row=1, column=2, pady=5, sticky=tk.E)
    plus.grid(row=1, column=1, pady=5, sticky=tk.E)
    cost_label_apple.grid(row=1, column=0, pady=5, sticky=tk.E)
    total_cost_label_apple.grid(row=1, column=3, pady=5, sticky=tk.W)

    product_2_label.grid(row=2, column=0, pady=5, sticky=tk.W)
    quantity_entry_orange.grid(row=2, column=1, pady=5, sticky=tk.W)
    minus_2.grid(row=2, column=2, pady=5, sticky=tk.E)
    plus_2.grid(row=2, column=1, pady=5, sticky=tk.E)
    cost_label_orange.grid(row=2, column=0, pady=5, sticky=tk.E)
    total_cost_label_orange.grid(row=2, column=3, pady=5, sticky=tk.W)

    total_label.grid(row=4, column=0, pady=5, sticky=tk.E)
    total_cost.grid(row=4, column=1, pady=5, sticky=tk.W)

    confirm_order_button.grid(row=5, column=0, columnspan=2, pady=5)

def compute_total_cost():
    total_cost.grid_forget()
    total_cost_label_apple.grid_forget()
    total_cost_label_orange.grid_forget()
    confirm_order_button.grid_forget()
    total_cost_apple_value = (int(quantity_entry_apple.get()) * 20)
    total_cost_orange_value = (int(quantity_entry_orange.get()) * 25)
    total_cost_value = (int(quantity_entry_apple.get()) * 20) + (int(quantity_entry_orange.get()) * 25)
    total_cost_label_apple.config(text=f"PHP {total_cost_apple_value: .2f}")
    total_cost_label_orange.config(text=f"PHP {total_cost_orange_value: .2f}")
    total_cost.config(text=f"PHP {total_cost_value: .2f}")
    total_cost_label_apple.grid(row=1, column=3, pady=5, sticky=tk.W)
    total_cost_label_orange.grid(row=2, column=3, pady=5, sticky=tk.W)
    total_cost.grid(row=4, column=1, pady=5, sticky=tk.W)
    payment_button.grid(row=5, column=0, columnspan=2, pady=5)

def mode_of_payment():
    label_order_information.grid_forget()
    product_1_label.grid_forget()
    quantity_entry_apple.grid_forget()
    minus.grid_forget()
    plus.grid_forget()
    cost_label_apple.grid_forget()
    total_cost_label_apple.grid_forget()
    product_2_label.grid_forget()
    quantity_entry_orange.grid_forget()
    minus_2.grid_forget()
    plus_2.grid_forget()
    cost_label_orange.grid_forget()
    total_cost_label_orange.grid_forget()
    total_label.grid_forget()
    total_cost.grid_forget()
    payment_button.grid_forget()
    
    payment_label.grid(row=3, column=1, pady=5, sticky=tk.W)
    button_cod.grid(row=5, column=1, pady=5, sticky=tk.W)
    button_card.grid(row=7, column=1, pady=5, sticky=tk.W)
    
def cash_on_delivery():
    payment_label.grid_forget()
    button_cod.grid_forget()
    button_card.grid_forget()
    card_label.grid_forget()
    card_number_label.grid_forget()
    card_number.grid_forget()
    security_code_label.grid_forget()
    security_code.grid_forget()
    card_owner_label.grid_forget()
    card_owner.grid_forget()
    exp_month_label.grid_forget()
    exp_month.grid_forget()
    exp_year_label.grid_forget()
    exp_year.grid_forget()
    checkout_button.grid_forget()

    cod_label.grid(row=1, column=0, pady=5, sticky=tk.W)

    name_label_text.grid(row=2, column=0, pady=5, sticky=tk.W)
    name_entry.grid(row=2, column=1, pady=5, sticky=tk.W)

    contact_label_text.grid(row=3, column=0, pady=5, sticky=tk.W)
    contact_entry.grid(row=3, column=1, pady=5, sticky=tk.W)

    email_label_text.grid(row=4, column=0, pady=5, sticky=tk.W)
    email_entry.grid(row=4, column=1, pady=5, sticky=tk.W)

    address_label_text.grid(row=5, column=0, pady=5, sticky=tk.W)
    address_entry.grid(row=5, column=1, pady=5, sticky=tk.W)

    confirm_info_button.grid(row=6, column=1, pady=5, sticky=tk.W)

def credit_card():
    payment_label.grid_forget()
    button_cod.grid_forget()
    button_card.grid_forget()

    card_label.grid(row=1, column=0, pady=5, sticky=tk.W)
    card_number_label.grid(row=2, column=0, pady=5, sticky=tk.W)
    card_number.grid(row=2, column=1, pady=5, sticky=tk.W)
    security_code_label.grid(row=3, column=0, pady=5, sticky=tk.W)
    security_code.grid(row=3, column=1, pady=5, sticky=tk.W)
    card_owner_label.grid(row=4, column=0, pady=5, stick=tk.W)
    card_owner.grid(row=4, column=1, pady=5, sticky=tk.W)
    exp_month_label.grid(row=5, column=0, pady=5, sticky=tk.W)
    exp_month.grid(row=5, column=1, pady=5, sticky=tk.W)
    exp_year_label.grid(row=6, column=0, pady=5, sticky=tk.W)
    exp_year.grid(row=6, column=1, pady=5, sticky=tk.W)

    checkout_button.grid(row=7, column=1, pady=5, sticky=tk.W)

def order_confirmation():
    cod_label.grid_forget()
    name_label_text.grid_forget()
    name_entry.grid_forget()
    contact_label_text.grid_forget()
    contact_entry.grid_forget()
    email_label_text.grid_forget()
    email_entry.grid_forget()
    address_label_text.grid_forget()
    address_entry.grid_forget()
    confirm_info_button.grid_forget()

    confirm_payment.grid(row=1, column=1, pady=5, sticky=tk.W)
    total_cost.grid(row=2, column=1, pady=5, sticky=tk.W)
    button_confirm.grid(row=3, column=1, padx=3, sticky=tk.W)
    button_deny.grid(row=3, column=1, pady=3, sticky=tk.E)

def order_done():
    confirm_payment.grid_forget()
    total_cost.grid_forget()
    button_confirm.grid_forget()
    button_deny.grid_forget()

    confirmation_text.grid(row=1, column=0, pady=5, sticky=tk.W)
    confirmation_subtext.grid(row=2, column=0, pady=5, sticky=tk.W)

    done_button.grid(row=3, column=0, pady=5, sticky=tk.W)

def order_deny():
    confirm_payment.grid_forget()
    total_cost.grid_forget()
    button_confirm.grid_forget()
    button_deny.grid_forget()

    button_deny_message.grid(row=1, column=0, pady=0, sticky=tk.W)
    exit_button.grid(row=3, column=0, pady=5, sticky=tk.W)

def increase_quantity(entry):
    current_quantity = int(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, str(current_quantity + 1))

def decrease_quantity(entry):
    current_quantity = int(entry.get())
    if current_quantity > 1:
        entry.delete(0, tk.END)
        entry.insert(0, str(current_quantity - 1))

def close_window():
    window.destroy()

# Main window
window = tk.Tk()
window.title("VS Browser")

window.geometry("500x250")

# Introductory
label = tk.Label(window, text="Welcome to Lea's Apples and Oranges!")
label.grid(row=0, column=0, columnspan=2, pady=10)

label_options = tk.Label(window, text="Please select any of the options below")
label_options.grid(row=1, column=0, columnspan=2, pady=10)

button = tk.Button(text="Order Fruits", command=on_button_order_fruits)
button.grid(row=2, column=0, columnspan=2, pady=10)

# Personal Information
label_personal_info_details = tk.Label(window, text="Before we proceed, kindly fill up the following information below:")

name_label = tk.Label(window, text="Name:")
name_entry = tk.Entry(window, width=30)

contact_label = tk.Label(window, text="Contact Number:")
contact_entry = tk.Entry(window, width=30)

email_label = tk.Label(window, text="E-mail:")
email_entry = tk.Entry(window, width=30)

address_label = tk.Label(window, text="Address:")
address_entry = tk.Entry(window, width=30)

proceed_button = tk.Button(text="Proceed", command=on_button_proceed)

# Order Details
label_order_information = tk.Label(window, text="Please select the amount of apples and/or oranges you want to purchase")

product_1_label = tk.Label(window, text="Apples:")
minus = tk.Button(window, text="-", command=lambda: decrease_quantity(quantity_entry_apple))
plus = tk.Button(window, text="+", command=lambda: increase_quantity(quantity_entry_apple))
quantity_entry_apple = tk.Entry(window)
quantity_entry_apple.insert(0,"0")
cost_label_apple = tk.Label(window, text = "PHP 20.00 x ")
total_cost_label_apple = tk.Label(window, text = "PHP 0.00")

product_2_label = tk.Label(window, text="Oranges:")
minus_2 = tk.Button(window, text="-", command=lambda: decrease_quantity(quantity_entry_orange))
plus_2 = tk.Button(window, text="+", command=lambda: increase_quantity(quantity_entry_orange))
quantity_entry_orange = tk.Entry(window)
quantity_entry_orange.insert(0,"0")
cost_label_orange = tk.Label(window, text = "PHP 25.00 x ")
total_cost_label_orange = tk.Label(window, text= "PHP 0.00")

total_label = tk.Label(window, text="Total Cost:")
total_cost = tk.Label(window, text = "PHP 0.00")
confirm_order_button = tk.Button(window, text="Confirm Order", command=compute_total_cost)

payment_button = tk.Button(window, text="Proceed to Payment", command=mode_of_payment)

payment_label = tk.Label(window, text="Mode of Payment")

button_cod = tk.Button(window, text="Cash on Delivery", command=cash_on_delivery)
cod_label = tk.Label(window, text="Checkout Information")

name_label_text = tk.Label(window, text="Name:")
contact_label_text = tk.Label(window, text="Contact Number:")
email_label_text = tk.Label(window, text="E-mail:")
address_label_text = tk.Label(window, text="Address:")

button_card = tk.Button(window, text="Credit Card", command=credit_card)
card_label = tk.Label(window, text="Checkout with Credit Card")
card_number_label = tk.Label(window, text="Card number")
card_number = tk.Entry(window, width=30)
security_code_label = tk.Label(window, text="Security Code")
security_code = tk.Entry(window, width=30)
card_owner_label = tk.Label(window, text="Card Owner")
card_owner = tk.Entry(window, width=30)
exp_month_label = tk.Label(window, text="Expiration Month")
exp_month = tk.Entry(window, width=30)
exp_year_label = tk.Label (window, text="Expiration Year")
exp_year = tk.Entry(window, width=30)

checkout_button = tk.Button(window, text="Checkout", command=cash_on_delivery)

confirm_info_button = tk.Button(window, text="Confirm Information", command=order_confirmation)

confirm_payment = tk.Label(window, text="Are you sure you want to pay the following amount?")
button_confirm = tk.Button(window, text=" Yes ", command=order_done)
button_deny = tk.Button(window, text=" No ", command=order_deny)

button_deny_message = tk.Label(window, text= " Please try again... ")

confirmation_text = tk.Label(window, text="ORDER RECEIVED!")
confirmation_subtext = tk.Label(window, text="Thank you for purchasing our fruits! We hope you have a great day.")

done_button = tk.Button(window, text="Done", command=close_window)
exit_button = tk.Button(window, text="Exit", command=close_window)



window.mainloop()
