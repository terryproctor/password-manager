from tkinter import *
from tkinter import messagebox
from password_generator import generate_password

def save():
    global website_input, email_entry, password_entry
    with open("saved_psw.csv", "a") as psw_file:
        website_input = website_entry.get()
        email_input = email_entry.get()
        password_input = password_entry.get()

        website_entry.delete(0, END)
        #email_entry.delete(0, END)
        password_entry.delete(0, END)

        is_ok = messagebox.askokcancel(title=f"website", message=f"These are the details added.\nWebsite: {website_input}\nEmail: {email_input}\nPassword: {password_input}\nOK to save?")
        if (is_ok):
            if(len(website_input) and len(email_input) and len(password_input)):
                psw_file.write(f"{website_input},{email_input},{password_input}\n")
            else:
                messagebox.showwarning(title="input error", message="Not enough information entered")
    return 1

def insert_gen_password():
    password_entry.delete(0, END)
    password_entry.insert(END, generate_password())

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#Canvas
lock_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

#Labels
website_lb = Label(text="Website:")
website_lb.grid(row=1, column=0)

email_lb = Label(text="Email/Username:")
email_lb.grid(row=2, column=0)

password_lb = Label(text="Password:")
password_lb.grid(row=3, column=0)

#Sticky EW sticks elements East and West of each item together 
#so they are aligned and neat

#Entries
website_entry = Entry()
website_entry.config(width=25)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")

email_entry = Entry()
email_entry.config(width=25)
email_entry.insert(END, "example@email.com")
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")

password_entry = Entry()
password_entry.config(width=21)
password_entry.grid(row=3, column=1, columnspan=1, sticky="EW")

#Buttons
generate_btn = Button(command=insert_gen_password)
generate_btn.config(text="Generate Password")
generate_btn.grid(row= 3, column=2, columnspan=1, sticky="EW")

add_btn = Button(command=save)
add_btn.config(text="Add", width=36)
add_btn.grid(row= 4, column=1, columnspan=2, sticky="EW")




window.mainloop()