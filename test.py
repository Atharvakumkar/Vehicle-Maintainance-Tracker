from tkinter import *
from tkinter import messagebox
from tkinter import font
from PIL import ImageTk, Image
import re 

def exist():
    exist_window = Toplevel()
    exist_window.title("Sign in")
    exist_window.geometry("1000x600")
    exist_window.config(background="white")

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
    heading = Label(exist_window,text = "Welcome Back", bg = "white",fg="#229799",  font = custom_font)
    heading.place(x=340,y=40)

    subheading = Label(exist_window, text = "Hello user! Please fill the below details to Login! ", bg = "white",fg="#48CFCB", font = custom_font2)
    subheading.place(x=260,y=120)

    name_text = Label(exist_window,text = "Enter Your Name:", bg = "white",fg="#229799",  font = custom_font2)
    name_text.place(x = 350, y = 180)

    name_entry = Entry(exist_window,width=22, border=2, fg="black",bg="#F5F7F8", font = custom_font2)
    name_entry.place(x=350, y = 220)

    ID_label = Label(exist_window,text = "Enter Customer Id:", bg = "white",fg="#229799",  font = custom_font2)
    ID_label.place(x = 350, y = 295)

    id_entry = Entry(exist_window, width=22, border=2, fg="black",bg="#F5F7F8", font = custom_font2)
    id_entry.place(x=350, y = 340)

    submit_button = Button(exist_window,text = "Submit",font = custom_font2 ,width = 10,height = 1,command = onclick, relief = RAISED,fg = "black")
    submit_button.place(x=430,y=410)


def click():
    def is_valid_running(running_status):
        return running_status.isdigit()

    def vehicle_click():
        global main_window
        main_window = None

        vehicle_name_check = vehicle_name.get().strip()
        vehicle_type_check = vehicle_type.get().strip()
        vehicle_year_check = vehicle_year.get().strip()
        running_check = running.get().strip()
        service_check = service.get().strip()
        insurance_check = insurance.get().strip()

        if (vehicle_name_check == "" or vehicle_type_check == "" or vehicle_year_check == "" or running_check == "" or service_check == "" or insurance_check == ""):
            messagebox.showerror(title="Oops!", message="Please fill all the details!")
        
        elif not is_valid_running(running_check):
            messagebox.showerror(title="Oops!", message="Please enter lifetime running in numbers only!")

        else:
            vehicle_submit['state'] = DISABLED
            messagebox.showinfo(title="Success!", message="Vehicle details submitted successfully!")

    vehicle = Toplevel()
    vehicle.geometry("1000x700")
    vehicle.title("Vehicle Maintenance Tracker")
    vehicle.resizable(False, False)
    vehicle.config(backgroun='white')

    # Label for the login image
    custom_font = font.Font(family="Poppins", size=30)
    custom_font1 = font.Font(family="Poppins", size=20)
    custom_font2 = font.Font(family="Poppins", size=15)
    custom_font3 = font.Font(family="Poppins", size=10)

    #name = Label(text="Welcome to CarCare", font=custom_font, fg="red", background="white", compound="bottom")
    #name.place(x=5, y=25)

    # Other labels and inputs for the sign-up form
    heading = Label(vehicle, text="Please fill the vehicle details below", bg="white",fg="#48CFCB", font=custom_font1)
    heading.place(x=280, y=20)

    vehicle_name_text = Label(vehicle, text="Enter Your Vehicle Name:", bg="white",fg="#229799", font=custom_font2)
    vehicle_name_text.place(x=350, y=80)

    vehicle_name = Entry(vehicle, width=40, border=2, fg="black", bg="#F5F7F8", font=custom_font3)
    vehicle_name.place(x=350, y=120)

    vehicle_type_text = Label(vehicle, text="Enter Your Fuel Type:", bg="white",fg="#229799", font=custom_font2)
    vehicle_type_text.place(x=350, y=160)

    vehicle_type = Entry(vehicle, width=40, border=2, fg="black", bg="#F5F7F8", font=custom_font3)
    vehicle_type.place(x=350, y=200)

    vehicle_year_text = Label(vehicle, text="Enter Your Registration Year:", bg="white",fg="#229799", font=custom_font2)
    vehicle_year_text.place(x=350, y=240)

    vehicle_year = Entry(vehicle, width=40, border=2, fg="black", bg="#F5F7F8", font=custom_font3)
    vehicle_year.place(x=350, y=280)
    vehicle_cc = Label(vehicle, text="Enter in YYYY-MM-DD format", bg="white", fg="grey", font=custom_font3)
    vehicle_cc.place(x=350, y=310)

    running_text = Label(vehicle, text="Enter Lifetime running in kms:", bg="white",fg="#229799", font=custom_font2)
    running_text.place(x=350, y=340)

    running = Entry(vehicle, width=40, border=2, fg="black",bg="#F5F7F8", font=custom_font3)
    running.place(x=350, y=380)

    service_text = Label(vehicle, text="Enter Last Service Date:", bg="white",fg="#229799", font=custom_font2)
    service_text.place(x=350, y=410)

    service = Entry(vehicle, width=40, border=2, fg="black",bg="#F5F7F8", font=custom_font3)
    service.place(x=350, y=450)
    service_cc = Label(vehicle, text="Enter in YYYY-MM-DD format", bg="white", fg="grey", font=custom_font3)
    service_cc.place(x=350, y=480)

    insurance_text = Label(vehicle, text="Enter Insurance Expiry Date:", bg="white",fg="#229799", font=custom_font2)
    insurance_text.place(x=350, y=510)

    insurance = Entry(vehicle, width=40, border=2, fg="black",bg="#F5F7F8", font=custom_font3)
    insurance.place(x=350, y=550)
    insurance_cc = Label(vehicle, text="Enter in YYYY-MM-DD format", bg="white", fg="grey", font=custom_font3)
    insurance_cc.place(x=350, y=580)

    # Submit button
    vehicle_submit = Button(vehicle, text="Submit", font=custom_font3, width=10, height=1, command=vehicle_click)
    vehicle_submit.place(x=450, y=620)

def new():
    window = Toplevel()
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

    name = Entry(window, width=40, border=2, fg="black", font=custom_font3)
    name.place(x=350, y=270)

    contact_text = Label(window, text="Enter Your Contact Number:",fg="#48A6A7", bg="white", font=custom_font2)
    contact_text.place(x=350, y=310)

    contact = Entry(window, width=40, border=2, fg="black", font=custom_font3)
    contact.place(x=350, y=340)

    email_text = Label(window, text="Enter your Email-id:", bg="white",fg="#48A6A7", font=custom_font2)
    email_text.place(x=350, y=390)

    email = Entry(window, width=40, border=2, fg="black", font=custom_font3)
    email.place(x=350, y=430)

    submit = Button(window, text="Submit",font=custom_font3, height=1, width=20, command=click)
    submit.place(x=420, y=510)

def feed_click():
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

    feedback = Toplevel()
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
    submit_button = Button(feedback, text="Submit", bg="teal", fg="white", font=myfont_3, relief="raised", command = submit_feedback) #submit feddback
    submit_button.place(x=470, y=530)


main_window = Tk()
main_window.geometry("1000x700")
main_window.title("Vehicle Maintenance Tracker")
main_window.resizable(False, False)
icon = PhotoImage(file="icon1.png")
main_window.iconphoto(True, icon)
main_window.config(background="white")

login = PhotoImage(file="rsz_5main.png")

custom_font = font.Font(family="Cabin", size=35)
custom_font2 = font.Font(family="Fira Sans", size=15)
custom_font3 = font.Font(family="Fira Sans", size=10)

head = Label(main_window, text="Welcome to Car Care", font=custom_font, fg="Grey", background="white")
head.place(x=300, y=5)
name = Label(main_window, text=".", font=custom_font, fg="white", background="white", image=login, compound="bottom")
name.place(x=50, y=65)

text1 = Label(main_window, text="At CarCare, we understand how important your car is ", font=custom_font2, background="white")
text2 = Label(main_window, text="to your daily life, and keeping it in top condition ", font=custom_font2, background="white")
text3 = Label(main_window, text="ensures both safety and performance. Our Car ", font=custom_font2, background="white")
text4 = Label(main_window, text="Maintenance Tracker is designed to help you easily ", font=custom_font2, background="white")
text5 = Label(main_window, text="manage and stay on top of all your car’s maintenance ", font=custom_font2, background="white")
text6 = Label(main_window, text="needs—because we believe that preventive care is the", font=custom_font2, background="white")
text7 = Label(main_window, text="key to longevity on the road.", font=custom_font2, background="white")
text1.place(x=500, y=100)
text2.place(x=500, y=130)
text3.place(x=500, y=160)
text4.place(x=500, y=190)
text5.place(x=500, y=220)
text6.place(x=500, y=250)
text7.place(x=500, y=280)

f1 = PhotoImage(file="ic1.png")
f2 = PhotoImage(file="ic2.png")

feature1 = Label(main_window, image=f1, background="white")
feature1.place(x=500, y=360)
feature2 = Label(main_window, image=f2, background="white")
feature2.place(x=780, y=360)

f1_text = Label(main_window, text="Service Remainders", font=custom_font2, fg="grey", background="white")
f1_text.place(x=560, y=330)

f1_text = Label(main_window, text="Monitor Health", font=custom_font2, fg="grey", background="white")
f1_text.place(x=840, y=330)

f1_subtext = Label(main_window, text="Don’t lose sight of your ", font=custom_font3, fg="grey", background="white")
f1_subtext.place(x=560, y=360)
f2_subtext = Label(main_window, text="maintenance and services. ", font=custom_font3, fg="grey", background="white")
f2_subtext.place(x=560, y=380)
f3_subtext = Label(main_window, text="Log your services and we will", font=custom_font3, fg="grey", background="white")
f3_subtext.place(x=560, y=400)
f3_subtext = Label(main_window, text="remind you when it's due.", font=custom_font3, fg="grey", background="white")
f3_subtext.place(x=560, y=420)

f4_subtext = Label(main_window, text="Track the health of your", font=custom_font3, fg="grey", background="white")
f4_subtext.place(x=840, y=360)
f5_subtext = Label(main_window, text="vehicle to gain insights", font=custom_font3, fg="grey", background="white")
f5_subtext.place(x=840, y=380)
f6_subtext = Label(main_window, text="for services and potential", font=custom_font3, fg="grey", background="white")
f6_subtext.place(x=840, y=400)
f8_subtext = Label(main_window, text="faulty issues.", font=custom_font3, fg="grey", background="white")
f8_subtext.place(x=840, y=420)

button_head = Label(main_window, text="Let's Get Started -->", font=custom_font2, background="white")
button_head.place(x=500, y=460)

new_user = Button(main_window, text="New User", font=custom_font2, command=new)
new_user.place(x=500, y=500)

old_user = Button(main_window, text="Existing User", font=custom_font2, command=exist)
old_user.place(x=620, y=500)

question = Label(main_window, text="Have any questions?", font=custom_font2, background="white")
question_text = Label(main_window, text="Get in touch with us by clicking the button below!", font=custom_font3, background="white")
question.place(x=500, y=560)
question_text.place(x=500, y=590)

feedback_form = Button(main_window, text = "Feedback", font=custom_font2, command = feed_click)
feedback_form.place(x=500, y=615)

main_window.mainloop()
