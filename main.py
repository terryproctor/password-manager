from tkinter import *

window = Tk()
window.title("Password Manager")
window.minsize(height=240, width=240)
window.config(padx=20, pady=20)

lock_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1, columnspan=1)

website_lb = Label(text="Website:")
website_lb.grid(row=1, column=0)

email_lb = Label(text="Email/Username:")
email_lb.grid(row=2, column=0)

password_lb = Label(text="Password:")
password_lb.grid(row=3, column=0)

website_entry = Entry()
website_entry.config(width=35)
website_entry.grid(row=1, column=1, columnspan=2)

email_entry = Entry()
email_entry.config(width=35)
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry()
password_entry.config(width=21)
password_entry.grid(row=3, column=1, columnspan=1)

generate_btn = Button()
generate_btn.config(text="Generate Password")
generate_btn.grid(row= 3, column=2, columnspan=1)

add_btn = Button()
add_btn.config(text="Add", width=36)
add_btn.grid(row= 4, column=1, columnspan=2)


window.mainloop()