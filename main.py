from tkinter import *

window = Tk()
window.title("Password Manager")
window.minsize(height=240, width=240)
window.config(padx=20, pady=20)

lock_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0,column=1)

window.mainloop()