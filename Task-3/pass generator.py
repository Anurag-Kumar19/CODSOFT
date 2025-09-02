from tkinter import *
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

root=Tk()
root.geometry("600x350")
root.title("PASSWORD GENERATOR")
root.configure(bg="#b5e48c")

def generate_password():
    length = int(entry.get())
    chars = letters+numbers+symbols
    password = ''.join(random.choice(chars) for _ in range(length))
    password_var.set(password)


ask=Label(root, text="Password length:", fg="black", bg="#d9ed92", font=("Helvetica", 20))
ask.pack(pady=5)
entry = Entry(root, relief="sunken", font=("Helvetica", 25))
entry.pack(pady=5)

password_var = StringVar()
password=Label(root, text="Generated Password:",fg="black", bg="#d9ed92", font=("Helvetica", 20))
password.pack(pady=5)
password_entry = Entry(root, textvariable=password_var, width=30, font=("Helvetica", 25),relief="sunken")
password_entry.pack(pady=5)

Button(root, text="Generate Password", font=("Helvetica", 18), command=generate_password).pack(pady=10)

root.mainloop()
