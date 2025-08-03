import tkinter as tk
import random
from tkinter import simpledialog, messagebox

def pin():
    c = str(random.randint(1000, 9999))
    result_label.config(text="Your pin is: " + c)

def password():
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    symbols = '!@#$%^&*()'
    all_chars = lower + upper + digits + symbols

    try:
        length = simpledialog.askinteger("Password Length", "Enter the length of password (For stronger passwords use a 12 character password):")
        if length is None:
            return  
        if length <= 0:
            raise ValueError
        password = ''.join(random.choice(all_chars) for _ in range(length))
        result_label.config(text="Your password is: " + password)
    except:
        messagebox.showerror("Invalid Input", "Please enter a valid positive number.")

root = tk.Tk()
root.title("Pin/Password Generator")
root.geometry("400x250")
root.config(bg="#1593c9")

title_label = tk.Label(root, text="Choose an option to generate:", bg="#1260e6", font=("Arial", 14))
title_label.pack(pady=20)

pin_btn = tk.Button(root, text="Generate PIN", command=pin, bg="cyan", fg="white", width=20, font=("Arial", 11))
pin_btn.pack(pady=5)

password_btn = tk.Button(root, text="Generate Password", command=password, bg="black", fg="white", width=20, font=("Arial", 11))
password_btn.pack(pady=5)

result_label = tk.Label(root, text="", bg="#28cf70", font=("Arial", 12, "bold"))
result_label.pack(pady=20)

root.mainloop()
