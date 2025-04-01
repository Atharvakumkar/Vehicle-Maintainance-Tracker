from tkinter import *
from tkinter import messagebox
from tkinter import font
import re

def vehicle_click():
    global main_window
    main_window = None

    # Get values from input fields
    vehicle_name_check = vehicle_name.get().strip()
    vehicle_type_check = vehicle_type.get().strip()
    vehicle_year_check = vehicle_year.get().strip()
    running_check = running.get().strip()
    service_check = service.get().strip()
    insurance_check = insurance.get().strip()

    # Validation for empty fields
    if (vehicle_name_check == "" or vehicle_type_check == "" or vehicle_year_check == "" or running_check == "" or service_check == "" or insurance_check == ""):
        messagebox.showerror(title="Oops!", message="Please fill all the details!")
    # Validate if the running field contains digits only
    elif not is_valid_running(running_check):
        messagebox.showerror(title="Oops!", message="Please enter lifetime running in numbers only!")
    else:
        # If everything is valid, disable the submit button
        vehicle_submit['state'] = DISABLED
        messagebox.showinfo(title="Success!", message="Vehicle details submitted successfully!")

vehicle = Tk()
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
heading = Label(text="Please fill the vehicle details below", bg="white",fg="#48CFCB", font=custom_font1)
heading.place(x=280, y=20)

vehicle_name_text = Label(text="Enter Your Vehicle Name:", bg="white",fg="#229799", font=custom_font2)
vehicle_name_text.place(x=350, y=80)

vehicle_name = Entry(width=40, border=2, fg="black", bg="#F5F7F8", font=custom_font3)
vehicle_name.place(x=350, y=120)

vehicle_type_text = Label(text="Enter Your Fuel Type:", bg="white",fg="#229799", font=custom_font2)
vehicle_type_text.place(x=350, y=160)

vehicle_type = Entry(width=40, border=2, fg="black", bg="#F5F7F8", font=custom_font3)
vehicle_type.place(x=350, y=200)

vehicle_year_text = Label(text="Enter Your Registration Year:", bg="white",fg="#229799", font=custom_font2)
vehicle_year_text.place(x=350, y=240)

vehicle_year = Entry(width=40, border=2, fg="black", bg="#F5F7F8", font=custom_font3)
vehicle_year.place(x=350, y=280)
vehicle_cc = Label(text="Enter in YYYY-MM-DD format", bg="white", fg="grey", font=custom_font3)
vehicle_cc.place(x=350, y=310)

running_text = Label(text="Enter Lifetime running in kms:", bg="white",fg="#229799", font=custom_font2)
running_text.place(x=350, y=340)

running = Entry(width=40, border=2, fg="black",bg="#F5F7F8", font=custom_font3)
running.place(x=350, y=380)

service_text = Label(text="Enter Last Service Date:", bg="white",fg="#229799", font=custom_font2)
service_text.place(x=350, y=410)

service = Entry(width=40, border=2, fg="black",bg="#F5F7F8", font=custom_font3)
service.place(x=350, y=450)
service_cc = Label(text="Enter in YYYY-MM-DD format", bg="white", fg="grey", font=custom_font3)
service_cc.place(x=350, y=480)

insurance_text = Label(text="Enter Insurance Expiry Date:", bg="white",fg="#229799", font=custom_font2)
insurance_text.place(x=350, y=510)

insurance = Entry(width=40, border=2, fg="black",bg="#F5F7F8", font=custom_font3)
insurance.place(x=350, y=550)
insurance_cc = Label(text="Enter in YYYY-MM-DD format", bg="white", fg="grey", font=custom_font3)
insurance_cc.place(x=350, y=580)

# Submit button
vehicle_submit = Button(vehicle, text="Submit", font=custom_font3, width=10, height=1, command=vehicle_click)
vehicle_submit.place(x=450, y=620)

vehicle.mainloop()
