from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_text.get().title()
    try:
        with open("data.json", "r") as password_file:
            data = json.load(password_file)
    except FileNotFoundError:
        messagebox.showwarning(title="Oops", message="File Not Found")
    else:
        if website in data:
            key = data[website]
            email = key["email"]
            password = key["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}, \n Password: {password}")
        else:
            messagebox.showwarning(title="Oops", message="No details for website exists")

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    letters_list = [choice(letters) for _ in range(randint(8, 10))]
    symbol_list = [choice(symbols) for _ in range(randint(2, 4))]
    num_list = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = letters_list + symbol_list + num_list
    shuffle(password_list)

    password = "".join(password_list)
    password_text.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_text.get().title()
    user = email_text.get()
    password = password_text.get()
    saved_str = website + " | " + user + " | " + password + "\n"
    new_data = {
        website: {
        "email" : user,
        "password" : password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else:
        try:
            with open("data.json", "r") as password_file:
                # Reading old data
                data = json.load(password_file)
        except FileNotFoundError:
            with open("data.json", "w") as password_file:
                json.dump(new_data, password_file)
        else:
            # Updating old data
            data.update(new_data)
            with open("data.json", "w") as password_file:
                # Save uploaded data
                json.dump(data, password_file, indent=4)
        finally:
            website_text.delete(0, 'end')
            password_text.delete(0, 'end')

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=50, pady=50)
window.title("My Pass")

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels

website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0)

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)


# Entries
website_text = Entry()
website_text.grid(row=1, column=1, sticky="EW")
website_text.focus()

email_text = Entry(width=35)
email_text.grid(row=2, column=1, columnspan=2, sticky="EW")
email_text.insert(0, "srithika@gmail.com")

password_text = Entry()
password_text.grid(row=3, column=1, sticky="EW")

# Buttons
search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2, sticky="EW")

gen_password_button = Button(text="Generate Password", command=generate_password)
gen_password_button.grid(row=3, column=2, sticky="EW")

add_button = Button(text="Add", width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")


window.mainloop()