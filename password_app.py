"""
    This module makes use of the user input in numbers and generates a password with random characters without repeating 
    the same character (this is because of the set()). Passwords can be copied to your clipboard with the copy button in the interface
"""

import random
import tkinter as tk
from tkinter import messagebox

def gen_password():
    alphabets= ["a", "q","w","e","r","t","y","u","i","o","p","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m","Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
    numbers= ["1","2","3","4","5","6","7","8","9","0"]
    symbols= ["!","#","$","%","&","(",")","*","+"]

    password_list = alphabets+numbers+symbols
    password_list1= set()
    for i in range(int(ask_entry.get())):
        password_list1.add(random.choice(password_list))

    password =""
    for i in password_list1:
        password += i

    password_entry.delete(0, tk.END)
    password_entry.insert(tk.END, password)


def copy_password():
    password= password_entry.get()
    if password :
        master.clipboard_clear()
        master.clipboard_append(password)
        master.update()
        messagebox.showinfo("Password Copied", "Password has been copied to clipboard")

    else:
        messagebox.showwarning("No Password", "No password generated")


master = tk.Tk()
master.title("Password Generator")
master.geometry("300x200")


ask_label = tk.Label(master, text= "how many characters do you want?")
ask_label.pack()
ask_entry = tk.Entry(master, width= 30)
ask_entry.pack()
password_label = tk.Label(master, text= "Generated Password: ")
password_label.pack()

password_entry = tk.Entry(master, width= 30)
password_entry.pack()

gen_button= tk.Button(master, text="Generate Password", command= gen_password, background="green")
gen_button.pack(pady=10)
copy_button= tk.Button(master, text= "Copy Password", command=copy_password, background= "yellow")
copy_button.pack(pady=10)

master.mainloop()