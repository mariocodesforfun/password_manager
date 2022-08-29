import tkinter
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(2, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 10))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, f"{password}")
    pyperclip.copy(password)


def add_data():

    website_data = website_entry.get()
    email_data = username_entry.get()
    password_data = password_entry.get()
    new_data = {website_data: {
        "email": email_data,
        "password": password_data
    }
    }

    if len(website_data) == 0 or len(password_data) == 0:
        messagebox.showinfo(title="Oops", message="Please fill all the fields")
    else:

        try:

            with open("data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)
            # updating old data with new data
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:

            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:

            website_entry.delete(0, 1000)
            password_entry.delete(0, 1000)
            # website_entry.focus()


def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", meassage="This data file does not exit")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword:{password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")







window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=100)

canvas = tkinter.Canvas(width=200, height=300, highlightthickness=False)
logo_img = tkinter.PhotoImage(file="/Users/mariogegprifti/Desktop/learn/PasswordManager/mypass.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


# Labels
website_label = tkinter.Label(text="Website:", font=("Courier", 25, "bold"))
website_label.grid(column=0, row=1)

email_label = tkinter.Label(text="Email/Username:", font=("Courier", 25, "bold"))
email_label.grid(column=0, row=2)

password_label = tkinter.Label(text="Password:", font=("Courier", 25, "bold"))
password_label.grid(column=0, row=3)


# entries
website_entry = tkinter.Entry(width=20)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=1)

username_entry = tkinter.Entry(width=45)
username_entry.insert(0, "gegpriftimario@gmail.com")
username_entry.grid(column=1, row=2, columnspan=2)

password_entry = tkinter.Entry(width=21)
password_entry.grid(column=1, row=3)


# buttons
generate_password_button = tkinter.Button(width=14, text="Generate Password", font=("courier", 20, "bold"), command=generate_password)
generate_password_button.grid(column=2, row=3, columnspan=1)

add_button = tkinter.Button(width=30, text="Add", font=("courier", 20, "bold"), command=add_data)
add_button.grid(column=1, row=6, columnspan=2)

search_button = tkinter.Button(width=15, text="Search", font=("courier", 20, "bold"), command=find_password, bg="blue")
search_button.grid(column=2, row=1, columnspan=1)


window.mainloop()
