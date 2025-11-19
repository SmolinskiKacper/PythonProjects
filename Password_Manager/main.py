from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    # join all items into a string using what you write between "" as separator
    password = "".join(password_list)
    password_input.delete(0, END)
    password_input.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    user_login = login_input.get()
    user_password = password_input.get()

    if len(website) == 0:
        messagebox.showerror("Error", "Please enter a website")
    elif len(user_login) == 0:
        messagebox.showerror("Error", "Please enter a login")

    elif len(user_password) == 0:
        messagebox.showerror("Error", "Please enter a password")

    else:

        is_correct = messagebox.askokcancel(title= website, message= f"Is this correct?\nEmail: {user_login}\nPassword: {user_password}")

        if is_correct:
            with open("passwords.txt", "a") as data_file:
                data_file.write(f"{website} | {user_login} | {user_password}\n")
            website_input.delete(0, END)
            password_input.delete(0, END)
            messagebox.showinfo("Success", "Password has been saved")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx= 55, pady= 55)

canvas = Canvas(width= 200, height = 200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo_img)
canvas.grid(row= 0,column= 1)

label_website = Label(text="Website:")
label_website.grid(row= 1, column= 0)
label_login = Label(text= "Email/Username:")
label_login.grid(row = 2, column= 0)
label_password = Label(text= "Password:")
label_password.grid(row= 3, column= 0)

website_input = Entry(width= 35)
website_input.grid(row= 1, column= 1, columnspan = 2, sticky="ew")
website_input.focus()
login_input = Entry(width= 35)
login_input.grid(row= 2, column= 1, columnspan = 2, sticky="ew")
login_input.insert(0,"kacper@gmail.com")
password_input = Entry(width= 21)
password_input.grid(row= 3, column = 1, sticky="ew")

button_generate = Button(text="Generate Password", command=generate_password)
button_generate.grid(row= 3, column= 2,sticky="ew")
button_add = Button(text="Add", width=50, command=save_password)
button_add.grid(row= 4, column= 1, columnspan = 2)



window.mainloop()