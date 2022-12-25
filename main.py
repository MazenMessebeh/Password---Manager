from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]

    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
file = open("data.txt", "a")


def save():
    web_data = web_entry.get()
    email_data = email_entry.get()
    pass_data = pass_entry.get()

    if len(web_data) == 0 or len(email_data) == 0 or len(pass_data) == 0:
        messagebox.showwarning(title="Warning", message="Please don't leave any fields empty.")
    else:
        is_ok = messagebox.askyesno(title=web_data, message=f"These are the data entered: \nEmail: {email_data}"
                                                            f"\nPassword: {pass_data} \n"
                                                            f"Want to save it?")
        if is_ok:
            file.write(f"{web_data} | {email_data} | {pass_data} \n")
            web_entry.delete(0, END)
            pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.minsize(width=600, height=550)
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

web_label = Label(text="Website: ")
web_label.grid(row=1, column=0)
web_entry = Entry(width=68)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()

email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0)
email_entry = Entry(width=68)
email_entry.grid(row=2, column=1, columnspan=2)

pass_label = Label(text="Password: ")
pass_label.grid(row=3, column=0)
pass_entry = Entry(width=35)
pass_entry.grid(row=3, column=1)

generate_button = Button(text="Generate Password", width=25, command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=57, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
