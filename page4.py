from tkinter import *
from tkinter import font
from tkinter import messagebox
import re

window = Tk()
window.title("Sign in")
window.geometry("1000x600")
window.config(background="white")

#name
def is_valid_name(name):
    return bool(re.match(r'^[A-Za-z\s]+$', name))

def is_valid_ID(ID):
    return ID.isdigit()

def onclick():
    name = name_entry.get().strip()
    ID = id_entry.get().strip()

    if not name or not ID:
        messagebox.showerror("Incomplete details","Please fill all the Fields!")
        return

    if not is_valid_name(name):
        messagebox.showerror("Invalid Name", "Invalid Name! Please Enter a valid Name.")
        return

    if not is_valid_ID(ID):
        messagebox.showerror("Invalid ID","Please Enter a Valid ID!")
        return
    
custom_font = font.Font(family="Poppins", size=30)
custom_font1 = font.Font(family="Poppins", size=20)
custom_font2 = font.Font(family="Poppins", size=15)
custom_font3 = font.Font(family="Poppins", size=10)
    
#labels and entries
heading = Label(text = "Welcome Back", bg = "white",fg="#229799",  font = custom_font)
heading.place(x=340,y=40)

subheading = Label(text = "Hello user! Please fill the below details to Login! ", bg = "white",fg="#48CFCB", font = custom_font2)
subheading.place(x=260,y=120)

name_text = Label(window,text = "Enter Your Name:", bg = "white",fg="#229799",  font = custom_font2)
name_text.place(x = 350, y = 180)

name_entry = Entry(window,width=22, border=2, fg="black",bg="#F5F7F8", font = custom_font2)
name_entry.place(x=350, y = 220)

ID_label = Label(window,text = "Enter Customer Id:", bg = "white",fg="#229799",  font = custom_font2)
ID_label.place(x = 350, y = 295)

id_entry = Entry(window, width=22, border=2, fg="black",bg="#F5F7F8", font = custom_font2)
id_entry.place(x=350, y = 340)

submit_button = Button(window,text = "Submit",font = custom_font2 ,width = 10,height = 1,relief = RAISED,command = onclick,fg = "black")
submit_button.place(x=430,y=410)

window.mainloop()
