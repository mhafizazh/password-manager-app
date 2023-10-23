import tkinter
from tkinter import *
from tkinter import messagebox
import random
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_passowrd():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
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
def add_button():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0 :
        messagebox.showinfo(title="Invalid input", message="Please fill all the boxes")
    else:
        is_save = messagebox.askokcancel(title=website, message=f"these are your information: \n"
                                                                f"website: {website}\n"
                                                                f"email: {email} \n"
                                                                f"password: {password}")
        if is_save:
            with open("data.json", "r") as data_file:
                # data_file.write(f"{website} | email: {email} | password: {password} \n")
                data= json.load(data_file)
                data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)
# ---------------------------- POP UP GUI ------------------------------- #
def pop_up_window(text):
    popup = Toplevel(window)
    popup.title("Popup Window")

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate the position to center the popup window
    popup_width = 300  # Specify the width of the popup
    popup_height = 100  # Specify the height of the popup
    x_position = (screen_width - popup_width) // 2
    y_position = (screen_height - popup_height) // 2

    # Set the geometry of the popup window
    popup.geometry(f"{popup_width}x{popup_height}+{x_position}+{y_position}")

    label = Label(popup, text=text)
    label.pack(padx=10, pady=10)

    close_button = Button(popup, text="Close", command=popup.destroy)
    close_button.pack(pady=10)

    # Make the popup modal
    popup.grab_set()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=20,padx=20)

canvas = Canvas(height=250,width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=0, columnspan=3)

# labels
website_label = Label(text="Website: ", width=20)
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username: ", width=20)
email_label.grid(row=2, column=0)
password_label = Label(text="Password: ", width=20)
password_label.grid(row=3,column=0)

# entry
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=17)
password_entry.grid(row=3, column=1)

# button
generate_password = Button(text="Generate password", command=generate_passowrd)
generate_password.grid(row=3, column=2, columnspan=2)
add_button = Button(text="add", width=36, command=add_button)
add_button.grid(row=4, column=1, columnspan=2)

print(tkinter.TkVersion)

window.mainloop()