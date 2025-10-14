import tkinter
from tkinter import messagebox
import random
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def generate_password():

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

    password = ""
    for char in password_list:
      password += char

    password_entry.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_to_file():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0 :
        messagebox.showinfo(title="Oops",message="Please dont leave any fields empty ! ")
    else:

        try :
            with open("data.json", "r") as f:
                #read the json file
                data = json.load(f)

        except FileNotFoundError:
            with open("data.json","w") as f:
                #write the data back in the file
                json.dump(new_data, f, indent= 4)

        else:
                #update the data to put new record
            data.update(new_data)

            with open("data.json","w") as f:
                #write the data back in the file
                json.dump(data, f, indent= 4)

        finally:
            website_entry.delete(0, len(website_entry.get()))
            username_entry.delete(0, len(username_entry.get()))
            password_entry.delete(0, len(password_entry.get()))

# ---------------------------- Find Password------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as f:
            # read the json file
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found !")

    else:
        if website in data:
            details = data.get(website)
            username_to_show = details.get("username")
            pass_to_show = details.get("password")

            messagebox.showinfo(title="Info", message=f"Username: {username_to_show}\nPassword: {pass_to_show} ")
        else:
            messagebox.showinfo(title="Error", message="No Details for the website exists!")

    finally:
        website_entry.delete(0, len(website_entry.get()))

# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tkinter.Canvas(width=200, height=200)
my_pass_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100,112,image=my_pass_img)
canvas.grid(row=0, column=1)

#Labels

website_label = tkinter.Label(text="Website:")
website_label.grid(row=1, column=0)

username_label = tkinter.Label(text="Email/Username:")
username_label.grid(row=2, column=0)

password_label = tkinter.Label(text="Password:")
password_label.grid(row=3, column=0)

#Entry

website_entry = tkinter.Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

username_entry = tkinter.Entry(width=38)
username_entry.grid(row=2,column=1,columnspan=2)
username_entry.insert(0,"muley.akshay24@gmail.com")

password_entry = tkinter.Entry(width=21)
password_entry.grid(row=3, column=1)


#buttons

generate_button = tkinter.Button(text="Generate Password",command=generate_password)
generate_button.grid(row=3, column=2)

add_button = tkinter.Button(text="Add",width=36, command=save_to_file)
add_button.grid(row=4, column=1, columnspan=2)

search_button = tkinter.Button(text="Search",width=12,command=find_password)
search_button.grid(row=1,column=2)

window.mainloop()