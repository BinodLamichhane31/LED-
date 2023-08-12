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

def on_focus_in(event):
    if event.widget.get() in ("Full Name", "Contact No.", "Email"):
        event.widget.delete(0, "end")
    if event.widget.get() in ("New Password", "Confirm New Password"):
        event.widget.delete(0, END)

def on_focus_out(event):
    if event.widget.get() == "":
        if event.widget == pwdEntry or event.widget == confirmPwdEntry:
            event.widget.insert(0, "New Password" if event.widget == pwdEntry else "Confirm New Password")
        elif event.widget == unameEntry:
            event.widget.insert(0, "Full Name")
        elif event.widget == phoneEntry:
            event.widget.insert(0, "Contact No.")


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
            uname = unameEntry.get()
            # email = email_entry.get()
            phone = phoneEntry.get()
            password = pwdEntry.get()
            confirm = confirmPwdEntry.get() 

            if not (uname and phone and password and confirm):
                messagebox.showerror("Registration Failed", "Please fill out all the required details and try again.")
            else:
                # Continue with password validation and other checks
                if password != confirm:
                    messagebox.showerror('Registration Failed', "Password didn't match. Please try re-entering the password.")
                    confirmPwdEntry.delete(0, END)
                elif football_collection.find_one({'phone': phone}):
                    messagebox.showwarning('Registration Failed', 'Account with this number already exists. You may want to login.')
                elif not re.match(r"^\d{10}$", phone):
                    messagebox.showerror('Registration Failed', 'Please provide a valid 10-digit phone number.')
                elif len(password) < 7 or not any(char.isupper() for char in password) or \
                        not any(char.isdigit() for char in password) or \
                        not any(char in '!@#$%' for char in password):
                    messagebox.showerror('Password Error', 'Password must be at least 7 characters long and should contain at least one uppercase letter, one number, and one special character (!@#$%).')
                else:
                    hashed_password = hashlib.sha256(password.encode()).hexdigest()
                    football_collection.insert_one({'fullName':uname,'phone':phone,'password':hashed_password})
                    messagebox.showinfo('Registration Success',"Account Successfully Registered.")
                    # To clear the entry fields 
                    unameEntry.delete(0, 'end')
                    # email_entry.delete(0, 'end')
                    phoneEntry.delete(0, 'end')
                    pwdEntry.delete(0, 'end')
                    confirmPwdEntry.delete(0, 'end')
                    signupBgRound.destroy()
                    login()
        global signupBgRound, unameEntry, email_entry, phoneEntry, pwdEntry, confirmPwdEntry           
        # GUI elements of the signup page   
        signupBgRound = Label(image = bgRoundSignup, bg = "#f2f2f2")
        signupBgRound.place(x = 780, y = 60)

        signin_icon = Image.open("Images\\loginicon.png")
        signin_image = signin_icon.resize((50,50))
        signin_image = ImageTk.PhotoImage(signin_image)
        signin_img_label = Label(signupBgRound,image=signin_image,border=0, bg = "#fff")
        signin_img_label.image = signin_image  
        signin_img_label.place(x=210,y=82)

        label_login = Label(signupBgRound, text="Create an Account", bg="#fff",border=0, font=('League Spartan Medium', '16', 'bold'))
        label_login.place(x=158, y=34)
        
        unameLabel = Label(signupBgRound, text = "Full Name *", font=('Tahoma', '12', ''), bg = "#FFF", border = 0)
        unameLabel.place(x=110, y=150)

        unameEntry =Entry(signupBgRound, font=('Tahoma', '12', ''), width = 28, bg = "#FFF", border = 0)
        unameEntry.place(x=112, y=178, height = 26)

        phoneLabel = Label(signupBgRound, text = "Contact No. *", font=('Tahoma', '12', ''), bg = "#FFF", border = 0)
        phoneLabel.place(x=110, y=224)

        phoneEntry =Entry(signupBgRound, font=('Tahoma', '12', ''), width = 28, bg = "#FFF", border = 0)
        phoneEntry.place(x=112, y=253, height = 26)

        passwordLabel = Label(signupBgRound, text = "Password *", font=('Tahoma', '12', ''), bg = "#FFF", border = 0)
        passwordLabel.place(x=110, y=300)

        pwdEntry =Entry(signupBgRound, font=('Tahoma', '12', ''), width = 28, bg = "#FFF", border = 0)  
        pwdEntry.place(x=112, y=328, height = 26)

        cfmPasswordLabel = Label(signupBgRound, text = "Confirm Password *", font=('Tahoma', '12', ''), bg = "#FFF", border = 0)
        cfmPasswordLabel.place(x=110, y=374)

        confirmPwdEntry =Entry(signupBgRound, font=('Tahoma', '12', ''), width = 28, bg = "#FFF", border = 0)
        confirmPwdEntry.place(x=112, y=403, height = 26)
        
        create_button = Button(signupBgRound, image = imageSignup, cursor = "hand2", compound = CENTER, width = 116, border = 0, bg = "#FFF", fg = "#FFF", font = ("League Spartan", 8, "bold"), command=signup_work)
        create_button.place(x=184, y=454, height = 62)

        app.bind('<Return>',lambda e: signup_work())

        signupBgRound_label = Label(signupBgRound,text="Already have an account?",font=('Tahoma','10',''),bg="#fff",border=0)
        signupBgRound_label.place(x=149,y=540)
        log_in_btn = Button(signupBgRound,text="LOGIN", cursor = "hand2", font=('League Spartan SemiBold', '10', ''),bg="#fff",border=0,fg="blue",command=back_to_login)
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
            phone = phoneEntry1.get()
            psw = passwordEntry.get()
            hashed_psw = hashlib.sha256(psw.encode()).hexdigest()
            user_data = get_login_data(phone)
            remember = remember_var.get()


            #  Login Validation
            if user_data:
                stored_psw = user_data['password']
                if stored_psw == hashed_psw:
                    if remember == True:
                        with open('Scripts\\remember.txt','w') as rem:
                            rem.write(phone)
                    messagebox.showinfo("Login Result", "Login Successful.")
                    app.destroy()
                    with open("Scripts\\phone_number.txt", "w") as file:
                        file.write(phone)
                    import Dashboard 
                else:
                    messagebox.showerror("Login Failed", "Incorrect Password!")
            else:
                messagebox.showerror("Login Failed", "No user account found with this phone number.")
                
        except Exception as e:
            messagebox.showerror('Login Error', 'An error occurred during login: ' + str(e))
    
    def show_password():
        passwordEntry.config(show="")
        show_password_button.config(image=hide_img, command=hide_password)

    def hide_password():
        passwordEntry.config(show="●")
        show_password_button.config(image=show_img, command=show_password)

    def on_password_focus_in(event):
        phone = phoneEntry1.get()
        user_data = get_login_data(phone)
        if user_data:
            stored_psw = user_data['password']
            stored_phone = user_data['phone']
            stored_remember = user_data.get('Save Password', False)
            if stored_phone == phone and stored_remember:
                passwordEntry.delete(0, END)
                passwordEntry.insert(0, stored_psw)

    # GUI elements for login page
    global right_frame
    login_icon = Image.open("Images\\loginicon.png")
    login_image = login_icon.resize((50, 50))
    login_image = ImageTk.PhotoImage(login_image)
    login_img_label = Label(roundImgLabel, image=login_image, border=0, bg = "#fff")
    login_img_label.image = login_image
    login_img_label.place(x= 216, y=110)

    label_login = Label(roundImgLabel, text="Welcome! Please Login To Continue.", bg="#fff", border=0,
                        font=('League Spartan Medium', '16', 'bold'))
    label_login.place(x=82, y=40)

    phone_n_label = Label(entryLabel, text="Phone *", bg="#fff", font=('Tahoma', '12', ''))
    phone_n_label.place(x=12, y=0)
    phoneEntry1 = Entry(entryLabel, width = 26, border = 0, font=('Tahoma', '12', ''), bg = "#fff")
    phoneEntry1.place(x=14, y=32, height = 28)

    password_label = Label(entryLabel, text="Password *", bg="#fff", font=('Tahoma', '12', ''))
    password_label.place(x=12, y=80)
    passwordEntry = Entry(entryLabel, width = 22, border = 0, font=('Tahoma', '12', ''), show="●", bg = "#fff")
    passwordEntry.place(x=14, y=112, height = 28)
    passwordEntry.bind("<FocusIn>", on_password_focus_in)
    remember_var = BooleanVar()
    remember_check = Checkbutton(roundImgLabel, text="Remember Me", cursor = "hand2", variable=remember_var, bg = "#fff")
    remember_check.place(x = 128, y = 336)

    show_icon = Image.open("Images\\show.png").resize((20, 20))
    hide_icon = Image.open("Images\\hide.png").resize((20, 20))

    show_img = ImageTk.PhotoImage(show_icon)
    hide_img = ImageTk.PhotoImage(hide_icon)

    show_password_button = Button(entryLabel, image=show_img, cursor = "hand2", border=0, bg = "#fff", command=show_password)
    show_password_button.place(x=222, y=115)

    login_button = Button(roundImgLabel, image = imageLogin, cursor = "hand2", border = 0, bg = "#fff", command=login_work)
    login_button.place(x=196, y=396, height = 52)

    try:
        with open('Scripts\\remember.txt','r') as r:
            rem_ph = r.read().strip()
        phoneEntry1.insert(0,rem_ph)
    except Exception as e:
        pass

    app.bind('<Return>', lambda e: login_work())

    right_frame_label = Label(roundImgLabel, text="Don't have an account?", font=('Tahoma', '10'), bg="#fff",border=0)
    right_frame_label.place(x=156, y=520)

    signupButton = Button(roundImgLabel, text="SIGN UP", cursor = "hand2", font=('League Spartan SemiBold', '10', "bold"), bg="#fff", border=0,fg="blue", command=sign_up)
    signupButton.place(x=294, y=514)

# Function for about us
def about_us():
    import aboutus

app = Tk()
app.geometry("1350x700")
app.config(bg="Black")
app.state("zoomed")
app.iconbitmap('Images\\football.ico')
app.resizable(0, 0)
app.title("Login Page")

# Creating the frames 
right_frame = Frame(app, width=1366, height=700, bg="#f2f2f2", border=1)
right_frame.place(x=0, y=0)
lower_frame = Frame(app, width=1366, height=46, bg="#f2f2f2")
lower_frame.place(x=0, y=702)

verticalLine = Frame(right_frame, width = 2, height = 520, bg = "#000")
verticalLine.place(x = 640, y = 100)

football_img = Image.open("Images\\logonp.png")
football_photo = football_img.resize((160,160))
football_photo1 = ImageTk.PhotoImage(football_photo)
football_label = Label(right_frame,image=football_photo1,border=0,background = "#f2f2f2")
football_label.image = football_photo  # Store a reference to the image to prevent it from being garbage collected
football_label.place(x=562,y=224)

entryImg = Image.open("Images\\entryImg.png")
imgEntry = ImageTk.PhotoImage(entryImg)

roundBg = Image.open("Images\\roundBg.png")
resizeBg = roundBg.resize((480, 580))
bgRound = ImageTk.PhotoImage(resizeBg)

roundImgLabel = Label(right_frame, image = bgRound, bg = "#f2f2f2")
roundImgLabel.image = bgRound
roundImgLabel.place(x = 780, y = 60)

roundBgSignup = Image.open("Images\\roundBgSignup.png")
resizeBgSignup = roundBgSignup.resize((480, 580))
bgRoundSignup = ImageTk.PhotoImage(resizeBgSignup)

kick_png = Image.open("Images\\stadium.png")
kick_photo = kick_png.resize((380,320))
kick_photo = ImageTk.PhotoImage(kick_photo)
kick_label = Label(right_frame,image=kick_photo,border=0,bg="#f2f2f2")
kick_label.image = kick_photo  
kick_label.place(x=66,y=156)

loginImage = Image.open("Images\\loginButton.png")
resizedLogin = loginImage.resize((100, 50))
imageLogin = ImageTk.PhotoImage(resizedLogin)

signupImage = Image.open("Images\\button.png")
imageSignup = ImageTk.PhotoImage(signupImage)

trophyImage = Image.open("Images\\football.png")
resizedTrophy = trophyImage.resize((54, 84))
imageTrophy = ImageTk.PhotoImage(resizedTrophy)

mainHeading = Image.open("Images\\mainHeading.png")
resizedHeading = mainHeading.resize((400, 80))
headingMain = ImageTk.PhotoImage(resizedHeading)

mainHeadingLabel = Label(right_frame, image = headingMain, bg ='#f2f2f2')
mainHeadingLabel.place(x = 60, y = 40)

trophyLabel = Label(right_frame, image = imageTrophy, bg = "#f2f2f2")
trophyLabel.place(x = 480, y = 30)

entryLabel = Label(roundImgLabel, image = imgEntry, bg = "#fff")
entryLabel.place(x = 110, y = 180)


unleash_label = Label(right_frame,text = 'UNLEASH YOUR FOOTBALL PASSION',font=('League Spartan Medium', '18', 'bold'),bg="#f2f2f2")
unleash_label.place(x=60,y=510)

about_us_btn = Button(right_frame,text="About Us 🡢",bg="#f2f2f2",border=0, cursor = "hand2", font=('League Spartan Medium', '12', ''),command=about_us)
about_us_btn.place(x=60,y=570)


copyright_label = Label(right_frame, text="Copyright © Martyr's Memorial Inc. All rights reserved.",font=('Tahoma', '10'), bg="#f2f2f2")
copyright_label.place(x=58,y=630)

login()

app.mainloop()
