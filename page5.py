from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re
import pymysql
from tkinter import font
import time

#email
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

#phone number 
def is_valid_phone(phone):
    return bool(re.match(r'^[789]\d{9}$', phone))

#name
def is_valid_name(name):
    return bool(re.match(r'^[A-Z][a-z]+ [A-Z][a-zA-Z]+$', name))

#feedback function 
def submit_feedback():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    feedback = feedback_text.get("1.0", END).strip()

    if not name or not phone or not email or not feedback:
        messagebox.showerror("Incomplete Details", "Please fill in all the fields before submitting.")
        return
    
    if not is_valid_name(name):
        messagebox.showerror("Invalid Name", "Invalid Name! Please Enter a valid Name.")
        return

    if not is_valid_email(email):
        messagebox.showerror("Invalid Email", "Please enter a valid email address.")
        return

    if not is_valid_phone(phone):
        messagebox.showerror("Invalid Phone", "Invalid Phone Number.")
        return

def open_new_window():
    new_window = Toplevel(feedback)
    new_window.title("Thank You!")
    new_window.geometry("400x300")
    new_window.resizable(False, False)

    thank_you_label = Label(new_window, text="Thank you for your feedback!", font=myfont_1, fg="green")
    thank_you_label.pack(pady=50)
    
    close_button = Button(new_window, text="Close", command=new_window.destroy, font=myfont_3, bg="teal", fg="white")
    close_button.pack()

#gui
feedback = Tk()
feedback.geometry("1000x600")  
feedback.title("Customer Feedback")
feedback.resizable(False, False)
feedback.configure(bg="white")
 
myfont = font.Font(family="Poppins", size=30)
myfont_1 = font.Font(family="Poppins", size=25)
myfont_2 = font.Font(family="Poppins", size=15)
myfont_3 = font.Font(family="Poppins", size=10)

label_font = ("Arial", 12, "bold")
input_font = ("Arial", 12)
button_font = ("Arial", 14, "bold")
heading_font = ("Arial", 18, "bold")

heading = Label(feedback, text="Feedback Form", fg="#48A6A7", font=myfont_1, bg="White")
heading.pack(pady=10)

#Labels 
name_label = Label(feedback, text="Your Name:", bg="white", fg="#48A6A7",  font=myfont_2)
name_label.place(x=350, y=100)

phone_label = Label(feedback, text="Phone Number:", bg="white",fg="#48A6A7",  font=myfont_2)
phone_label.place(x=350, y=190)

email_label = Label(feedback, text="Email Address:", bg="white",fg="#48A6A7",  font=myfont_2)
email_label.place(x=350, y=270)

feedback_label = Label(feedback, text="Your Feedback:", bg="white", fg="#48A6A7", font=myfont_2)
feedback_label.place(x=350, y=350)

#input/entries
name_entry = Entry(feedback, width=40, border=2,bg="#F5F7F8",  font=myfont_3)
name_entry.place(x=350, y=140)

phone_entry = Entry(feedback, width=40, border=2, bg="#F5F7F8",  font=myfont_3)
phone_entry.place(x=350, y=230)

email_entry = Entry(feedback, width=40, border=2, bg="#F5F7F8", font=myfont_3)
email_entry.place(x=350, y=310)

feedback_text = Text(feedback, width=40, border=2,bg="#F5F7F8",  height=5, font=myfont_3)
feedback_text.place(x=350, y=390)

#Submit Button
submit_button = Button(feedback, text="Submit", command=submit_feedback, bg="teal", fg="white", font=myfont_3, relief="raised")
submit_button.place(x=470, y=530)


feedback.mainloop()
