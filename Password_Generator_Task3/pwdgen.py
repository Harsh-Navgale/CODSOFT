import tkinter as tk
import secrets
import string
import pyperclip

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            show_temporary_message("Invalid Password Length")
        else:
            strength = strength_var.get()

            if strength == "Weak":
                characters = string.ascii_letters
            elif strength == "Moderate":
                characters = string.ascii_letters + string.digits
            else:
                characters = string.ascii_letters + string.digits + string.punctuation

            password = ''.join(secrets.choice(characters) for _ in range(length))
            result_label.config(text="Generated Password: " + password)
            show_temporary_message("Password Generated ")
            
    except ValueError:
        result_label.config(text="Please enter a valid password length.")
        show_temporary_message("Invalid Password Length")

def copy_password():
    password = result_label.cget("text").split(": ")[1]
    pyperclip.copy(password)
    show_temporary_message("Password Copied to Clipboard")

def show_temporary_message(message, duration=2000):
    temp_label.config(text=message)
    window.after(duration, lambda: temp_label.config(text=""))  

# Create the main window
window = tk.Tk()
window.title("Password Generator")
window.geometry("500x350")  

# Label for password length
length_label = tk.Label(window, text="Password Length:")
length_label.pack()

# Entry for password length
length_entry = tk.Entry(window)
length_entry.pack()

# Label for password strength
strength_label = tk.Label(window, text="Password Strength:")
strength_label.pack()

# Radio buttons for password strength
strength_var = tk.StringVar()
strength_var.set("Weak")
weak_radio = tk.Radiobutton(window, text="Weak", variable=strength_var, value="Weak")
moderate_radio = tk.Radiobutton(window, text="Moderate", variable=strength_var, value="Moderate")
strong_radio = tk.Radiobutton(window, text="Strong", variable=strength_var, value="Strong")
weak_radio.pack()
moderate_radio.pack()
strong_radio.pack()

# Button to generate password
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack()

# Label to display the generated password
result_label = tk.Label(window, text="", wraplength=450)  # Wrap text within 450 pixels
result_label.pack()

# Button to copy the generated password
copy_button = tk.Button(window, text="Copy Password", command=copy_password)
copy_button.pack()

# Temporary message label
temp_label = tk.Label(window, text="", fg="red")
temp_label.pack()

# Center the window on the screen
window.eval('tk::PlaceWindow . center')

window.mainloop()
