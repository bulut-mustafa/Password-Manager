import tkinter
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def generate():
   
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, tkinter.END)
    password_entry.insert(0, password)
    
    # copies password to the clipboard
    pyperclip.copy(password_entry.get())

# ---------------------------- SAVE PASSWORD ------------------------------- #



def add_button():
    
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email":email,
            "password":password
        }
    }
    
    #checks if the user left any field empty
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning", message="Please don't leave any fields empty")
    else:
        #checks with the user to make sure everything is correct
        answer = messagebox.askokcancel(title="aga", message=f"These are the detail entered: \nEmail: {email}"
                            f"\nPassword: {password}\n Is it ok?", )
        
        #if yes saves the informations, if not doesn't do anything
        if answer:
            try:
                with open("data.json", "r") as data_file:
                    try:
                        data = json.load(data_file)
                    except json.decoder.JSONDecodeError:
                        data = {}
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json" , "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, tkinter.END)
                email_entry.delete(0, tkinter.END)
                password_entry.delete(0, tkinter.END)
                website_entry.focus()
                
        


# ---------------------------- UI SETUP ------------------------------- #



window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=80, pady=80)

canvas = tkinter.Canvas(width=200, height=200)
logo = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo)
canvas.grid(column=1, row=0)


#website label
website_label = tkinter.Label(text="Website:")
website_label.grid(column=0,row=1)

#username/mail label
username_label = tkinter.Label(text="Email/Username:")
username_label.grid(column=0,row=2)

#password label
password_label = tkinter.Label(text="Pasword:")
password_label.grid(column=0,row=3)

#password entry 
password_entry = tkinter.Entry(width=18)
password_entry.grid(column=1,row=3)

#website entry
website_entry = tkinter.Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)

#email entry
email_entry = tkinter.Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)


generater_button = tkinter.Button(text="Generate Password", command=generate)
generater_button.grid(column=2, row=3)

add_button = tkinter.Button(text="Add", width=33, command=add_button)
add_button.grid(column=1, row=4,columnspan=2)

website_entry.focus()

window.mainloop()