import random
import tkinter as tk
import tkinter.messagebox as messagebox
import pyperclip

# Create the application window
window = tk.Tk()
window.title("Password Generator")

# Create the widgets
label_length = tk.Label(window, text="Password Length:")
label_length.grid(row=0, column=0, padx=10, pady=10)

entry_length = tk.Entry(window)
entry_length.grid(row=0, column=1, padx=10, pady=10)

label_characters = tk.Label(window, text="Include Characters:")
label_characters.grid(row=1, column=0, padx=10, pady=10)

var_lowercase = tk.IntVar()
checkbutton_lowercase = tk.Checkbutton(window, text="Lowercase (a-z)", variable=var_lowercase)
checkbutton_lowercase.grid(row=2, column=0, padx=10, pady=5)

var_uppercase = tk.IntVar()
checkbutton_uppercase = tk.Checkbutton(window, text="Uppercase (A-Z)", variable=var_uppercase)
checkbutton_uppercase.grid(row=3, column=0, padx=10, pady=5)

var_numbers = tk.IntVar()
checkbutton_numbers = tk.Checkbutton(window, text="Numbers (0-9)", variable=var_numbers)
checkbutton_numbers.grid(row=4, column=0, padx=10, pady=5)

var_symbols = tk.IntVar()
checkbutton_symbols = tk.Checkbutton(window, text="Symbols (!@#$%^&*)", variable=var_symbols)
checkbutton_symbols.grid(row=5, column=0, padx=10, pady=5)

password_label = tk.Label(window, text="")
password_label.grid(row=6, column=0, padx=10, pady=10, columnspan=2)

# Define the function to generate the password
def generate_password():
    length = int(entry_length.get())
    lowercase = var_lowercase.get()
    uppercase = var_uppercase.get()
    numbers = var_numbers.get()
    symbols = var_symbols.get()

    # Define the possible characters to use in the password
    chars = ''
    if lowercase:
        chars += 'abcdefghijklmnopqrstuvwxyz'
    if uppercase:
        chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if numbers:
        chars += '0123456789'
    if symbols:
        chars += '!@#$%^&*()'

    # Generate the password
    password = ''
    for i in range(length):
        password += random.choice(chars)

    # Display the password
    password_label.config(text=password)
    pyperclip.copy(password)
    messagebox.showinfo("Password Generated", "Your password has been generated and copied to clipboard.")

# Create the generate button
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.grid(row=7, column=0, padx=10, pady=10, columnspan=2)

# Run the application
window.mainloop()
