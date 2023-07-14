#Importing the libraries
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
from pymongo import MongoClient
import re, subprocess
import hashlib

try:
    # Creating MongoClient, connecting to database and collection
    football_client = MongoClient('mongodb://localhost:27017/')
    football_database = football_client['football_database']
    football_collection = football_database['users']
except:
    messagebox.showerror('Error','Database Connection Error')

# Function to go back to login page after clicking Sign In button in signup page
def back_to_login():
    '''
    Destroy the signup frame and display the login section.
    '''
    signup_frame.destroy()
    login()

def sign_in():
        '''
        Display the sign in section.
        '''
        def signup_work():
            '''
            Ask user information and store in the database.
            '''
            global phone, password
            # Getting the  data from entries
            uname = uname_entry.get()
            email = email_entry.get()
            phone = phone_entry.get()
            password = psw_entry.get()
            confirm = confirm_entry.get() 
            try:   
                # input validation
                if uname=='' or email =='' or phone =='' or password == '' or confirm == '':
                    messagebox.showerror("Registeration",'No fields can be empty.')
                elif password!=confirm:
                    messagebox.showerror('Registeration','Password and confirm password are not matching.')
                elif football_collection.find_one({'phone':phone}):
                    messagebox.showwarning('Registeration','This number already exists.')
                elif not re.match(r"[^@]+@[^@]+\.[^@]+",email):
                    messagebox.showerror('Registration', 'Please give the valid email address.')
                elif not re.match(r"^\d{10}$",phone) :
                    messagebox.showerror('Registration', 'Please give the valid phone number')

                elif len(password)<7 or not re.search('[A-Z]',password) or not re.search('[0-9]',password) or not re.search('[!@#$%]',password):
                    messagebox.showerror('Registration', 'Password must be at least 6 characters long and contain at least one uppercase letter, one number, and one special character (!@#$%^&*).')
                else:
                    hashed_password = hashlib.sha256(password.encode()).hexdigest()
                    football_collection.insert_one({'fullName':uname,'email':email,'phone':phone,'password':hashed_password})
                    messagebox.showinfo('Registeration',"Registeration Successful!!")
                    # To clear the entry fields 
                    uname_entry.delete(0, 'end')
                    email_entry.delete(0, 'end')
                    phone_entry.delete(0, 'end')
                    psw_entry.delete(0, 'end')
                    confirm_entry.delete(0, 'end')
            except Exception as e:
                messagebox.showerror('Registration', 'An error occurred during registration: ' + str(e))
    
                        
        # Signup GUI   
        global signup_frame
        signup_frame = Frame(app, width=900, height=668, bg="sky blue", border=1)
        signup_frame.place(x=451, y=1)

        signin_icon = Image.open("Images/loginicon.png")
        signin_image = signin_icon.resize((70,70))
        signin_image = ImageTk.PhotoImage(signin_image)
        signin_img_label = Label(signup_frame,image=signin_image,border=0)
        signin_img_label.image = signin_image  
        signin_img_label.place(x=420,y=105)
        label_login = Label(signup_frame, text="Create an Account", bg="sky blue",border=0, font=('Segoe Print', '16', 'bold'))
        label_login.place(x=350, y=55)

        uname_label = Label(signup_frame, text="Full Name", bg="sky blue", border=0,font=('Segoe Print', '12', ''))
        uname_label.place(x=350, y=185)
        uname_entry =Entry(signup_frame, font=('Segoe Print', '10', ''))
        uname_entry.place(x=350, y=215)

        email_label = Label(signup_frame, text="Email", bg="sky blue", border=0,font=('Segoe Print', '12', ''))
        email_label.place(x=350, y=245)
        email_entry =Entry(signup_frame, font=('Segoe Print', '10', ''))
        email_entry.place(x=350, y=275)

        phone_label = Label(signup_frame, text="Phone Number", bg="sky blue", border=0,font=('Segoe Print', '12', ''))
        phone_label.place(x=350, y=310)
        phone_entry =Entry(signup_frame, font=('Segoe Print', '10', ''))
        phone_entry.place(x=350, y=340)

        psw_label = Label(signup_frame, text="Passsword", bg="sky blue", border=0,font=('Segoe Print', '12', ''))
        psw_label.place(x=350, y=370)
        psw_entry =Entry(signup_frame, font=('Segoe Print', '10', ''),show='*')
        psw_entry.place(x=350, y=400)

        confirm_label = Label(signup_frame, text="Confirm Passsword", bg="sky blue", border=0,font=('Segoe Print', '12', ''))
        confirm_label.place(x=350, y=430)
        confirm_entry =Entry(signup_frame, font=('Segoe Print', '10', ''),show='*')
        confirm_entry.place(x=350, y=460)

        create_button = Button(signup_frame,text="CREATE ACCOUNT",font=('Segoe Print', '10', ''),height=1,bg="sky blue",border=1,command=signup_work)
        create_button.place(x=385,y=495)
        app.bind('<Return>',lambda e: signup_work())

        signup_frame_label = Label(signup_frame,text="Already have an account?",font=('Segoe Print','9',''),bg="sky blue",border=0)
        signup_frame_label.place(x=345,y=540)
        log_in_btn = Button(signup_frame,text="Log In",font=('Segoe Print', '9', ''),bg="sky blue",border=0,fg="blue",command=back_to_login)
        log_in_btn.place(x=505,y=535)
# Function to get the user's data from the database
def get_login_data(phone):
    global user
    user = football_collection.find_one({'phone':phone})   
    return user
# Function for login
def login():
    '''
    Display the login section.
    '''
    def login_work():
        try:
            phone = phone_n_entry.get()
            psw = password_entry.get()
            hashed_psw = hashlib.sha256(psw.encode()).hexdigest()
            user_data = get_login_data(phone)

            #  Login Validation
            if user_data:
                stored_psw = user_data['password']
                stored_uname = user_data['phone']
                if stored_psw == hashed_psw:
                    messagebox.showinfo("Login Result", "Login Successful.")
                    app.destroy()  
                    with open("C:/Users/Dell/Desktop/Python Project/phone_number.txt", "w") as file:
                        file.write(phone)
                    subprocess.Popen(["python", "Scripts/dashboard.py"]) 
                else:
                    messagebox.showerror("Login Result", "Login Unsuccessful.")
            else:
                messagebox.showerror("Login Result", "User not found.")
        except Exception as e:
            messagebox.showerror('Login Error', 'An error occurred during login: ' + str(e))
    
    def show_password():
        password_entry.config(show="")
        show_password_button.config(image=hide_img, command=hide_password)

    def hide_password():
        password_entry.config(show="*")
        show_password_button.config(image=show_img, command=show_password)

    # GUI elements for login page
    global right_frame
    login_icon = Image.open("Images/loginicon.png")
    login_image = login_icon.resize((70, 70))
    login_image = ImageTk.PhotoImage(login_image)
    login_img_label = Label(right_frame, image=login_image, border=0)
    login_img_label.image = login_image
    login_img_label.place(x=450, y=165)
    label_login = Label(right_frame, text="Welcome! Please Login into your Account.", bg="sky blue", border=0,
                        font=('Segoe Print', '16', 'bold'))
    label_login.place(x=250, y=120)

    phone_n_label = Label(right_frame, text="Phone", bg="sky blue", border=0, font=('Segoe Print', '12', ''))
    phone_n_label.place(x=380, y=240)
    phone_n_entry = Entry(right_frame, font=('Segoe Print', '10', ''))
    phone_n_entry.place(x=380, y=270)

    password_label = Label(right_frame, text="Password", bg="sky blue", border=0, font=('Segoe Print', '12', ''))
    password_label.place(x=380, y=310)
    password_entry = Entry(right_frame, font=('Segoe Print', '10', ''), show="*")
    password_entry.place(x=380, y=340)

    show_icon = Image.open("Images/show.png").resize((20, 20))
    hide_icon = Image.open("Images/hide.png").resize((20, 20))

    show_img = ImageTk.PhotoImage(show_icon)
    hide_img = ImageTk.PhotoImage(hide_icon)

    show_password_button = Button(right_frame, image=show_img, border=0, command=show_password)
    show_password_button.place(x=560, y=342)

    login_button = Button(right_frame, text="LOGIN", font=('Segoe Print', '10', ''), height=1, bg="sky blue", border=1,
                          command=login_work)
    login_button.place(x=460, y=380)

    app.bind('<Return>', lambda e: login_work())

    right_frame_label = Label(right_frame, text="Don't have an account?", font=('Segoe Print', '9', ''), bg="sky blue",
                              border=0)
    right_frame_label.place(x=380, y=430)
    sign_in_btn = Button(right_frame, text="Sign In", font=('Segoe Print', '9', ''), bg="sky blue", border=0,
                         fg="blue", command=sign_in)
    sign_in_btn.place(x=530, y=425)

# Function for about us
def about_us():
    def back():
        about_frame.destroy()
    about_frame = Frame(app, width=700, height=600, bg="sky blue", border=1, relief='raised')
    about_frame.place(x=550, y=30)
    back_btn = Button(about_frame,height=1,text="╳",bg="sky blue",font=('Segoe Print', '10', ''),border=0,command=back)
    back_btn.place(x=675,y=0)

def create_login_gui():
    # Creating the main window of the application
    global app, right_frame, left_frame
    app = Tk()
    app.geometry("1350x700")
    app.config(bg="Black")
    app.resizable(0, 0)
    app.title("Login Page")

    # Creating the frames 
    left_frame = Frame(app, width=450, height=668, bg="sky blue", border=1)
    left_frame.place(x=0, y=1)
    right_frame = Frame(app, width=900, height=668, bg="sky blue", border=1)
    right_frame.place(x=451, y=1)
    lower_frame = Frame(app, width=1350, height=30, bg="sky blue")
    lower_frame.place(x=0, y=670)

    # Calling the login function
    login()

    # GUI elements for left frame
    app_name_label = Label(left_frame,text ="A-Division \t    \n Football League",font=('Segoe Print', '36', 'bold'),bg="sky blue")
    app_name_label.place(x=25,y=60)

    football_img = Image.open("Images/football.png")
    football_photo = football_img.resize((70,100))
    football_photo = ImageTk.PhotoImage(football_photo)
    football_label = Label(left_frame,image=football_photo,border=0,bg='sky blue')
    football_label.image = football_photo  # Store a reference to the image to prevent it from being garbage collected
    football_label.place(x=320,y=40)

    pitch_png = Image.open("Images/pitch.png")
    pitch_photo = pitch_png.resize((400,350))
    pitch_photo = ImageTk.PhotoImage(pitch_photo)
    pitch_label = Label(left_frame,image=pitch_photo,border=0,bg="sky blue")
    pitch_label.image = pitch_photo  
    pitch_label.place(x=30,y=230)

    unleash_label = Label(left_frame,text = '"Unleash your football passion"',font=('Segoe Print', '18', 'bold'),bg="sky blue")
    unleash_label.place(x=50,y=510)

    about_us_btn = Button(left_frame,text="About Us",bg="sky blue",border=0,font=('Segoe Print', '12', ''),command=about_us)
    about_us_btn.place(x=50,y=580)
    arrow_label = Label(left_frame,text="🡢",bg="sky blue",border=0,font=('Segoe Print', '12', 'bold'))
    arrow_label.place(x=140,y=587)

    copyright_label = Label(left_frame, text="\u00a9 2023 HaHaHa K Cha?. All rights reserved.",font=('Segoe Print', '10'), bg="sky blue")
    copyright_label.place(x=50,y=630)

    app.mainloop()
create_login_gui()
