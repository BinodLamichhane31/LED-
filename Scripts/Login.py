#Importing the libraries
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
from pymongo import MongoClient
import re, subprocess
import hashlib
import time

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
    signupBgRound.destroy()
    login()

def sign_up():
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
                    messagebox.showerror("Registration",'No fields can be empty.')

                elif password!=confirm:
                    messagebox.showerror('Registration','Password and confirm password are not matching.')

                elif football_collection.find_one({'phone':phone}):
                    messagebox.showwarning('Registration','This number already exists.')

                elif not re.match(r"[^@]+@[^@]+\.[^@]+",email):
                    messagebox.showerror('Registration', 'Please give the valid email address.')
                    
                elif not re.match(r"^\d{10}$",phone) :
                    messagebox.showerror('Registration', 'Please give the valid phone number')

                elif len(password)<7 or not re.search('[A-Z]',password) or not re.search('[0-9]',password) or not re.search('[!@#$%]',password):
                    messagebox.showerror('Registration', 'Password must be at least 6 characters long and contain at least one uppercase letter, one number, and one special character (!@#$%^&*).')

                else:
                    hashed_password = hashlib.sha256(password.encode()).hexdigest()
                    football_collection.insert_one({'fullName':uname,'email':email,'phone':phone,'password':hashed_password})
                    messagebox.showinfo('Registration',"Registration Successful!! \\nYou have to use your phone number as your username.")
                    # To clear the entry fields 
                    uname_entry.delete(0, 'end')
                    email_entry.delete(0, 'end')
                    phone_entry.delete(0, 'end')
                    psw_entry.delete(0, 'end')
                    confirm_entry.delete(0, 'end')
                    signupBgRound.destroy()
                    login()
            except Exception as e:
                messagebox.showerror('Registration', 'An error occurred during registration: ' + str(e))
    
        global signupBgRound           
        # GUI elements of the signup page   
        signupBgRound = Label(image = bgRoundSignup, bg = "#FFFACD")
        signupBgRound.place(x = 780, y = 60)

        signin_icon = Image.open("Images\\loginicon.png")
        signin_image = signin_icon.resize((50,50))
        signin_image = ImageTk.PhotoImage(signin_image)
        signin_img_label = Label(signupBgRound,image=signin_image,border=0, bg = "#fff")
        signin_img_label.image = signin_image  
        signin_img_label.place(x=210,y=60)
        label_login = Label(signupBgRound, text="Create an Account", bg="#fff",border=0, font=('League Spartan Medium', '16', 'bold'))
        label_login.place(x=158, y=22)

        uname_label = Label(signupBgRound, text="Full Name *", bg="#fff", border=0,font=('Tahoma', '12', ''))
        uname_label.place(x=108, y=121)
        uname_entry =Entry(signupBgRound, font=('Tahoma', '12', ''), width = 28, bg = "#fff", border = 0)
        uname_entry.place(x=108, y=148, height = 25)

        email_label = Label(signupBgRound, text="Email *", bg="#fff", border=0,font=('Tahoma', '12', ''))
        email_label.place(x=108, y=194)
        email_entry =Entry(signupBgRound, font=('Tahoma', '12', ''), width = 28, bg = "#fff", border = 0)
        email_entry.place(x=108, y=221, height = 25)

        phone_label = Label(signupBgRound, text="Phone Number *", bg="#fff", border=0,font=('Tahoma', '12', ''))
        phone_label.place(x=108, y=268)
        phone_entry =Entry(signupBgRound, font=('Tahoma', '12', ''), width = 28, bg = "#fff", border = 0)
        phone_entry.place(x=108, y=295, height = 25)

        psw_label = Label(signupBgRound, text="Passsword *", bg="#fff", border=0,font=('Tahoma', '12', ''))
        psw_label.place(x=108, y=342)
        psw_entry =Entry(signupBgRound, font=('Tahoma', '12', ''), width = 28, bg = "#fff", border = 0)
        psw_entry.place(x=108, y=369, height = 25)

        confirm_label = Label(signupBgRound, text="Confirm Passsword *", bg="#fff", border=0,font=('Tahoma', '12', ''))
        confirm_label.place(x=108, y=416)
        confirm_entry =Entry(signupBgRound, font=('Tahoma', '12', ''), width = 28, bg = "#fff", border = 0)
        confirm_entry.place(x=108, y=443, height = 25)

        create_button = Button(signupBgRound, image = imageSignup , border = 0, bg = "#fff", command=signup_work)
        create_button.place(x=192, y=475)

        app.bind('<Return>',lambda e: signup_work())

        signupBgRound_label = Label(signupBgRound,text="Already have an account?",font=('Tahoma','10',''),bg="#fff",border=0)
        signupBgRound_label.place(x=149,y=540)
        log_in_btn = Button(signupBgRound,text="LOGIN",font=('League Spartan SemiBold', '10', ''),bg="#fff",border=0,fg="blue",command=back_to_login)
        log_in_btn.place(x=299,y=534)
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
    try:
        football_collection['users']
    except Exception as e:
        messagebox.showerror("MongoDB connection error", str(e))
    
    def login_work():
        try:
            phone = phone_n_entry.get()
            psw = password_entry.get()
            hashed_psw = hashlib.sha256(psw.encode()).hexdigest()
            user_data = get_login_data(phone)
            remember = remember_var.get()
            
            filter = {'phone': phone}
            
            update = {
                "$set":{
                    'Save Password' : remember
                }
            }

            football_collection.update_one(filter, update)

            #  Login Validation
            if user_data:
                stored_psw = user_data['password']
                stored_phone = user_data['phone']
                stored_remember = user_data.get('Save Password')
                if stored_psw == hashed_psw:
                    messagebox.showinfo("Login Result", "Login Successful.")
                    app.destroy()
                    with open("Scripts\\phone_number.txt", "w") as file:
                        file.write(phone)
                    import Dashboard 
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
        password_entry.config(show="●")
        show_password_button.config(image=show_img, command=show_password)

    def on_password_focus_in(event):
        phone = phone_n_entry.get()
        user_data = get_login_data(phone)
        if user_data:
            stored_psw = user_data['password']
            stored_phone = user_data['phone']
            stored_remember = user_data.get('Save Password', False)
            if stored_phone == phone and stored_remember:
                password_entry.delete(0, END)
                password_entry.insert(0, stored_psw)

    # GUI elements for login page
    global right_frame
    login_icon = Image.open("Images\\loginicon.png")
    login_image = login_icon.resize((50, 50))
    login_image = ImageTk.PhotoImage(login_image)
    login_img_label = Label(roundImgLabel, image=login_image, border=0, bg = "#fff")
    login_img_label.image = login_image
    login_img_label.place(x= 216, y=110)

    label_login = Label(roundImgLabel, text="Welcome! Please Login into your Account.", bg="#fff", border=0,
                        font=('League Spartan Medium', '16', 'bold'))
    label_login.place(x=58, y=40)

    phone_n_label = Label(entryLabel, text="Phone *", bg="#fff", font=('Tahoma', '12', ''))
    phone_n_label.place(x=12, y=0)
    phone_n_entry = Entry(entryLabel, width = 26, border = 0, font=('Tahoma', '12', ''), bg = "#fff")
    phone_n_entry.place(x=14, y=32, height = 28)

    password_label = Label(entryLabel, text="Password *", bg="#fff", font=('Tahoma', '12', ''))
    password_label.place(x=12, y=80)
    password_entry = Entry(entryLabel, width = 22, border = 0, font=('Tahoma', '12', ''), show="●", bg = "#fff")
    password_entry.place(x=14, y=112, height = 28)
    password_entry.bind("<FocusIn>", on_password_focus_in)
    remember_var = BooleanVar()
    remember_check = Checkbutton(roundImgLabel, text="Remember Me", variable=remember_var, bg = "#fff")
    remember_check.place(x = 128, y = 342)

    forgotPwd = Button(roundImgLabel, text = "Forgot Password?", bg = "#fff", border = 0, fg ="blue")
    forgotPwd.place(x = 260, y = 344)

    show_icon = Image.open("Images\\show.png").resize((20, 20))
    hide_icon = Image.open("Images\\hide.png").resize((20, 20))

    show_img = ImageTk.PhotoImage(show_icon)
    hide_img = ImageTk.PhotoImage(hide_icon)

    show_password_button = Button(entryLabel, image=show_img, border=0, bg = "#fff", command=show_password)
    show_password_button.place(x=222, y=115)

    login_button = Button(roundImgLabel, image = imageLogin, border = 0, bg = "#fff", command=login_work)
    login_button.place(x=196, y=380)

    app.bind('<Return>', lambda e: login_work())



    right_frame_label = Label(roundImgLabel, text="Don't have an account?", font=('Tahoma', '10'), bg="#fff",border=0)
    right_frame_label.place(x=156, y=520)

    signupButton = Button(roundImgLabel, text="SIGN UP", font=('League Spartan SemiBold', '10', "bold"), bg="#fff", border=0,fg="blue", command=sign_up)
    signupButton.place(x=294, y=514)

# Function for about us
def about_us():
    import aboutus

app = Tk()
app.geometry("1350x700")
app.config(bg="Black")
app.state("zoomed")
app.resizable(0, 0)
app.title("Login Page")

# Creating the frames 
right_frame = Frame(app, width=1366, height=700, bg="#FFFACD", border=1)
right_frame.place(x=0, y=0)
lower_frame = Frame(app, width=1366, height=46, bg="#FFFACD")
lower_frame.place(x=0, y=702)

verticalLine = Frame(right_frame, width = 2, height = 520, bg = "#000")
verticalLine.place(x = 640, y = 100)

football_img = Image.open("Images\\logonp.png")
football_photo = football_img.resize((160,160))
football_photo1 = ImageTk.PhotoImage(football_photo)
football_label = Label(right_frame,image=football_photo1,border=0,background = "#FFFACD")
football_label.image = football_photo  # Store a reference to the image to prevent it from being garbage collected
football_label.place(x=560,y=220)

entryImg = Image.open("Images\\entryImg.png")
imgEntry = ImageTk.PhotoImage(entryImg)

roundBg = Image.open("Images\\roundBg.png")
resizeBg = roundBg.resize((480, 580))
bgRound = ImageTk.PhotoImage(resizeBg)

roundImgLabel = Label(right_frame, image = bgRound, bg = "#FFFACD")
roundImgLabel.image = bgRound
roundImgLabel.place(x = 780, y = 60)

roundBgSignup = Image.open("Images\\roundBgSignup.png")
resizeBgSignup = roundBgSignup.resize((480, 580))
bgRoundSignup = ImageTk.PhotoImage(resizeBgSignup)

kick_png = Image.open("Images\\pitch.png")
kick_photo = kick_png.resize((400,350))
kick_photo = ImageTk.PhotoImage(kick_photo)
kick_label = Label(right_frame,image=kick_photo,border=0,bg="#FFFACD")
kick_label.image = kick_photo  
kick_label.place(x=60,y=156)

loginImage = Image.open("Images\\loginButton.png")
resizedLogin = loginImage.resize((100, 50))
imageLogin = ImageTk.PhotoImage(resizedLogin)

signupImage = Image.open("Images\\signupbtn.png")
resizedSignup = signupImage.resize((100, 50))
imageSignup = ImageTk.PhotoImage(resizedSignup)

trophyImage = Image.open("Images\\football.png")
resizedTrophy = trophyImage.resize((54, 84))
imageTrophy = ImageTk.PhotoImage(resizedTrophy)

mainHeading = Image.open("Images\\mainHeading.png")
resizedHeading = mainHeading.resize((400, 80))
headingMain = ImageTk.PhotoImage(resizedHeading)

mainHeadingLabel = Label(right_frame, image = headingMain, bg ='#FFFACD')
mainHeadingLabel.place(x = 60, y = 40)

trophyLabel = Label(right_frame, image = imageTrophy, bg = "#FFFACD")
trophyLabel.place(x = 480, y = 30)

entryLabel = Label(roundImgLabel, image = imgEntry, bg = "#fff")
entryLabel.place(x = 110, y = 180)


unleash_label = Label(right_frame,text = 'UNLEASH YOUR FOOTBALL PASSION',font=('League Spartan Medium', '18', 'bold'),bg="#FFFACD")
unleash_label.place(x=60,y=510)

about_us_btn = Button(right_frame,text="About Us",bg="#FFFACD",border=0,font=('League Spartan Medium', '12', ''),command=about_us)
about_us_btn.place(x=60,y=570)
arrow_label = Label(right_frame,text="🡢",bg="#FFFACD",border=0,font=('League Spartan Medium', '12', 'bold'))
arrow_label.place(x=136,y=577)

copyright_label = Label(right_frame, text="Copyright © Martyr's Memorial Inc. All rights reserved.",font=('Tahoma', '10'), bg="#FFFACD")
copyright_label.place(x=58,y=630)

login()

app.mainloop()
