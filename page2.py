from tkinter import *
from tkinter import messagebox
from tkinter import font

window = Tk()
window.geometry("1000x700")
window.title("Vehicle Maintainance Tracker")
window.resizable(False, False)
window.config(background="white")

    # Label for the login image
custom_font = font.Font(family="Poppins", size=30)
custom_font1 = font.Font(family="Poppins", size=20)
custom_font2 = font.Font(family="Poppins", size=15)
custom_font3 = font.Font(family="Poppins", size=10)

name = Label(window, text="Welcome to Car Care", font=custom_font, fg="#006A71", background="white")
name.place(x=300, y=25)

    # Other labels and inputs for the sign-up form
heading = Label(window, text="Sign Up", bg="white",fg="#48A6A7", font=custom_font1)
heading.place(x=455, y=120)
subheading = Label(window, text="Please fill the below details to proceed", bg="white",fg="#48A6A7", font=custom_font3)
subheading.place(x=385, y=175)

name_text = Label(window, text="Enter Your Name:", bg="white", fg="#48A6A7", font=custom_font2)
name_text.place(x=350, y=230)

name = Entry(window, width=40, border=2, fg="black",bg="#F5F7F8", font=custom_font3)
name.place(x=350, y=270)

contact_text = Label(window, text="Enter Your Contact Number:",fg="#48A6A7", bg="white", font=custom_font2)
contact_text.place(x=350, y=310)

contact = Entry(window, width=40, border=2, fg="black",bg="#F5F7F8", font=custom_font3)
contact.place(x=350, y=340)

email_text = Label(window, text="Enter your Email-id:", bg="white",fg="#48A6A7", font=custom_font2)
email_text.place(x=350, y=390)

email = Entry(window, width=40, border=2, fg="black",bg="#F5F7F8", font=custom_font3)
email.place(x=350, y=430)

submit = Button(window, text="Submit",font=custom_font3, height=1, width=20)
submit.place(x=420, y=510)

window.mainloop()
