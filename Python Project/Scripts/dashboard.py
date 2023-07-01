# importing the libraries
from tkinter import *
from tkinter import ttk,messagebox,Label,PhotoImage
from PIL import Image, ImageTk
from pymongo import MongoClient
from base64 import *
import io
import pandas as pd


football_client = MongoClient('mongodb://localhost:27017/')
football_database = football_client['football_database']
football_collection = football_database['users']
player_collection = football_database['players']
team_collection = football_database['teams']



with open("C:/Users/Dell/Desktop/Python Project/phone_number.txt", "r") as file:
    phone = file.read().strip()
user_data = football_collection.find_one({"phone":phone})
# Function for adding icons with buttons
def create_button_with_icon(frame, image_path, text, x, y,cmd):
    icon = Image.open(image_path)
    icon = icon.resize((20, 20))
    image = ImageTk.PhotoImage(icon)
    img_label = Label(frame, image=image, border=0, bg="sky blue")
    img_label.image = image
    img_label.place(x=x, y=y)
    btn = Button(frame, text=text, border=0, bg="sky blue", font=('Segoe Print', '12', 'bold'), width=25, anchor='w',command=cmd)
    btn.place(x=x+30, y=y-10)
    return btn

# Functions for changing the colour of button text when the button is clicked
def highlight_button(btn):
    btn.config(bg="sky blue",fg="blue")
# Functions to reset the colour of text of button    
def reset_button(btn):
    btn.config(bg="sky blue",fg="black")
# Functions for all the buttons
def home():
    home_frame()
    # messagebox.showerror('','HOME')
    highlight_button(buttons[0])  #Changes the colour of test of frist button
    for btn in buttons[1:]:       #Resets the text colour as nutton[1:] excludes button[0]
        reset_button(btn)
def live():
    live_frame()
    # messagebox.showerror('','LIVE')
    highlight_button(buttons[1])
    for btn in buttons[:1] + buttons[2:]:
        reset_button(btn)

def fav():
    favourites_frame()
    # messagebox.showerror('','Favourites')
    highlight_button(buttons[2])
    for btn in buttons[:2] + buttons[3:]:
        reset_button(btn)
def over():
    overview_frame()
    # messagebox.showerror('','Overview')
    highlight_button(buttons[3])
    for btn in buttons[:3] + buttons[4:]:
        reset_button(btn)
def news():
    news_frame()
    # messagebox.showerror('','News')
    highlight_button(buttons[4])
    for btn in buttons[:4] + buttons[5:]:
        reset_button(btn)
def match():
    matches_frame()
    # messagebox.showerror('','Matches')
    highlight_button(buttons[5])
    for btn in buttons[:5] + buttons[6:]:
        reset_button(btn)
def stand():
    standings_frame()
    # messagebox.showerror('','standing')
    highlight_button(buttons[6])
    for btn in buttons[:6] + buttons[7:]:
        reset_button(btn)
def personal():
    personaliztion_frame()
    highlight_button(buttons[7])
    for btn in buttons[:7] + buttons[8:]:
        reset_button(btn)
    
def feed():
    feedback_frame()
    # messagebox.showerror('','feedback')
    highlight_button(buttons[8])
    for btn in buttons[:8]:
        reset_button(btn)

#Creating the main window of the application
app = Tk()
app.geometry("1350x700")
app.config(bg="Black")
app.resizable(0, 0)
app.title("Dashboard")

# Styling the speparator
style = ttk.Style()
style.configure("Separator.TSeparator", background="black")

#Creating the frames
left_frame = Frame(app, width=300, height=668, bg="sky blue", border=1)
left_frame.place(x=0, y=1)
right_frame = Frame(app, width=1050, height=668, bg="sky blue", border=1)
right_frame.place(x=301, y=1)
lower_frame = Frame(app, width=1350, height=30, bg="sky blue")
lower_frame.place(x=0, y=670)

# GUI elements in th left frame
label_topic = Label(left_frame, text="A Division", font=('Segoe Print', '20', 'bold'), bg="sky blue")
label_topic.place(x=15, y=10)
label_topic1 = Label(left_frame, text="Football League", font=('Segoe Print', '20', 'bold'), bg="sky blue")
label_topic1.place(x=15, y=50)
ball = Image.open("C:/Users/Dell/Desktop/Python Project/Images/football.png")
foot = ball.resize((33,33))
foot = ImageTk.PhotoImage(foot)
foot_lbl = Label(left_frame,image=foot,border=0,bg="sky blue")
foot_lbl.place(x=175,y=15)

# Placing the separator line
separator = ttk.Separator(left_frame, orient='horizontal', style='Separator.TSeparator')
separator.place(x=0, y=100, relwidth=1)
try:
    welcome_text = "Hello! "+user_data['fullName']
    welcome_text_label = Label(right_frame,text=welcome_text,font=('Segoe Print', '20', 'bold'), bg="sky blue",anchor='center')
    welcome_text_label.place(relx=0.5,rely=0.5,anchor='center')
except:
    pass

buttons = [] #Creating the empty buttons

#Appending the icon with buttons
buttons.append(create_button_with_icon(left_frame, "C:/Users/Dell/Desktop/Python Project/Images/home.png", "Home", 20, 120,home))
buttons.append(create_button_with_icon(left_frame, "C:/Users/Dell/Desktop/Python Project/Images/live.png", "Live", 20, 180,live))
buttons.append(create_button_with_icon(left_frame, "C:/Users/Dell/Desktop/Python Project/Images/favourites.png", "Favourites", 20, 240,fav))
buttons.append(create_button_with_icon(left_frame, "C:/Users/Dell/Desktop/Python Project/Images/overview.png", "Overview", 20, 300,over))
buttons.append(create_button_with_icon(left_frame, "C:/Users/Dell/Desktop/Python Project/Images/news.png", "News & Updates", 20, 360,news))
buttons.append(create_button_with_icon(left_frame, "C:/Users/Dell/Desktop/Python Project/Images/matches.png", "Matches", 20, 420,match))
buttons.append(create_button_with_icon(left_frame, "C:/Users/Dell/Desktop/Python Project/Images/standings.png", "Standings", 20, 480,stand))
buttons.append(create_button_with_icon(left_frame,"C:/Users/Dell/Desktop/Python Project/Images/personalization.png","Personalization",20,540,personal))
separator = ttk.Separator(left_frame, orient='horizontal', style='Separator.TSeparator')
separator.place(x=0, y=600, relwidth=1)
buttons.append(create_button_with_icon(left_frame,"C:/Users/Dell/Desktop/Python Project/Images/feedback.png","Feedback & Support",20,620,feed))

def team_overview():
    print(1  )
    
def home_frame():
    frame_home =Frame(right_frame,width=1050, height=668, bg="sky blue", border=1)
    frame_home.place(x=0,y=0)
    frame_home.place(x=0,y=0)
    label_home = Label(frame_home,text="Home",font=('Segoe Print', '17', 'bold'),bg='sky blue')
    label_home.place(x=10,y=10)
    separator = ttk.Separator(frame_home, orient='horizontal', style='Separator.TSeparator')
    separator.place(x=0, y=65, relwidth=1)
def live_frame():
    frame_live = Frame(right_frame, width=1050, height=668, bg="sky blue", border=1)
    frame_live.place(x=0, y=0)
    frame_live.place(x=0, y=0)
    label_live = Label(frame_live, text="Live", font=('Segoe Print', '17', 'bold'), bg='sky blue')
    label_live.place(x=10, y=10)
    separator = ttk.Separator(frame_live, orient='horizontal', style='Separator.TSeparator')
    separator.place(x=0, y=65, relwidth=1)

    # Read the data from the Excel file
    live_data = pd.read_excel("C:/Users/Dell/Desktop/Python Project/Points/Point Table.xlsx", sheet_name="Live")

    # Create a pandas DataFrame from the data
    df = pd.DataFrame(live_data)

    # Create a treeview widget to display the data
    treeview1 = ttk.Treeview(frame_live, style='Custom.Treeview')
    treeview1.place(x=10, y=80, width=1030, height=570)

    # Configure the treeview columns
    treeview1["columns"] = list(df.columns)
    treeview1["show"] = "headings"

    # Define the custom column widths as a list
    column_widths = [25, 25, 5, 50, 20, 50, 300]  # Add more widths for additional columns

    # Create a custom style for the treeview
    style = ttk.Style()
    style.configure('Custom.Treeview', font=('Arial', 12), background='sky blue', foreground='black')  # Set the font and colors for the table

    style.configure('Custom.Treeview.Heading', font=('Arial', 12, 'bold'),background='sky blue')

    # Add the column headers to the treeview
    for i, column in enumerate(df.columns):
        treeview1.heading(column, text=column)

        # Get the width for the column
        width = column_widths[i] if i < len(column_widths) else 100  # Default width is 100 if not specified
        treeview1.heading(column, text=column, anchor='w')

        # Set the width of the column in the treeview
        treeview1.column(column, width=width)

    # Add the data rows to the treeview
    for index, row in df.iterrows():
        treeview1.insert("", "end", values=list(row))

    style.configure('Custom.Treeview', rowheight=38)
    style.configure('Custom.Treeview', spacing=5)

def favourites_frame():
    frame_favourites =Frame(right_frame,width=1050, height=668, bg="sky blue", border=1)
    frame_favourites.place(x=0,y=0)
    frame_favourites.place(x=0,y=0)
    label_favourites = Label(frame_favourites,text="Favourites",font=('Segoe Print', '17', 'bold'),bg='sky blue')
    label_favourites.place(x=10,y=10)
    separator = ttk.Separator(frame_favourites, orient='horizontal', style='Separator.TSeparator')
    separator.place(x=0, y=65, relwidth=1)
def overview_frame():
    global frame_overview
    frame_overview =Frame(right_frame,width=1050, height=668, bg="sky blue", border=1)
    frame_overview.place(x=0,y=0)
    frame_overview.place(x=0,y=0)
    label_overview = Label(frame_overview,text="Overview",font=('Segoe Print', '17', 'bold'),bg='sky blue')
    label_overview.place(x=10,y=10)
    separator = ttk.Separator(frame_overview, orient='horizontal', style='Separator.TSeparator')
    separator.place(x=0, y=65, relwidth=1)
    def overview_selection(select):
        global team_search_entry
        if select == "League":
            frame_league = Frame(frame_overview,bg="blue",height=600,width=1050)
            frame_league.place(x=0,y=70)
        elif select==options[1]:
            def team_search():
                team_data = team_collection.find_one({'name':team_search_entry.get()})
                def label_tame_details(frame_team,team_text,x,y):
                    label_team_info = Label(frame_team,text=team_text,font=('Segoe Print', '12', 'bold'),bg="sky blue")
                    label_team_info.place(x=x,y=y)
                team_info_list = []
                team_info_list.append(label_tame_details(frame_team,"Club Name:",350,150))
                team_info_list.append(label_tame_details(frame_team,team_data['name'],480,150))
                team_info_list.append(label_tame_details(frame_team,"Founded Year:",350,180))
                team_info_list.append(label_tame_details(frame_team,team_data['founded'],480,180))
                team_info_list.append(label_tame_details(frame_team,"Location:",350,210))
                team_info_list.append(label_tame_details(frame_team,team_data['location'],480,210))
                team_info_list.append(label_tame_details(frame_team,"Stadium:",350,240))
                team_info_list.append(label_tame_details(frame_team,team_data['stadium'],480,240))
                team_info_list.append(label_tame_details(frame_team,"President:",350,270))
                team_info_list.append(label_tame_details(frame_team,team_data['president'],480,270))
                team_info_list.append(label_tame_details(frame_team,"Manager:",350,300))
                team_info_list.append(label_tame_details(frame_team,team_data['manager'],480,300))
                team_info_list.append(label_tame_details(frame_team,"Captain:",350,330))
                team_info_list.append(label_tame_details(frame_team,team_data['captain'],480,330))

            def on_entry_click(event):
                if team_search_entry.get() == "Team's name":
                    team_search_entry.delete(0, END)  
            def on_focus_out(event):
                if team_search_entry.get() == '':
                    team_search_entry.insert(0, "Team's name")  
            frame_team = Frame(frame_overview,bg="sky blue",height=600,width=1050)
            frame_team.place(x=0,y=70)
            team_search_entry = Entry(frame_team,font=('Segoe Print', '12', 'bold'))
            team_search_entry.place(x=10,y=10)
            team_search_button = Button(frame_team,text="Search",font=('Segoe Print', '8', 'bold'),bg="sky blue",command=team_search)
            team_search_button.place(x=255,y=10)
            team_search_entry.insert(0,"Team's name")
            team_search_entry.bind('<FocusIn>',on_entry_click)
            team_search_entry.bind('<FocusOut>',on_focus_out)
        elif select == options[2]:
            def player_search():
                player_data = player_collection.find_one({'name':player_search_entry.get()})
                try:
                # Extract the image data from the document and convert it back to an image
                    encoded_image = player_data["image"]
                    image_data = b64decode(encoded_image)
                    image = Image.open(io.BytesIO(image_data))
                    image = image.resize((150,200))
                    # Convert the image to a Tkinter-compatible format
                    tk_image = ImageTk.PhotoImage(image)
                    # Create a Tkinter label and display the image
                    image_label = Label(frame_player, image=tk_image)
                    image_label.image = image
                    image_label.place(x=150,y=150)
                    def details_label(frame_player,players_text,x,y):
                        label_details = Label(frame_player,text=players_text,font=('Segoe Print', '12', 'bold'),bg="sky blue")
                        label_details.place(x=x,y=y)
                    label_the_details = []
                    label_the_details.append(details_label(frame_player,"Full Name:",350,150))
                    label_the_details.append(details_label(frame_player,player_data['name'],480,150))
                    label_the_details.append(details_label(frame_player,"Date of Birth:",350,180))
                    label_the_details.append(details_label(frame_player,player_data['dob'],480,180))
                    label_the_details.append(details_label(frame_player,"Nationality:",350,210))
                    label_the_details.append(details_label(frame_player,player_data['nationality'],480,210))
                    label_the_details.append(details_label(frame_player,"Current Club:",350,240))
                    label_the_details.append(details_label(frame_player,player_data['club'],480,240))
                    label_the_details.append(details_label(frame_player,"Number:",350,270))
                    label_the_details.append(details_label(frame_player,player_data['number'],480,270))
                    label_the_details.append(details_label(frame_player,"Position:",350,300))
                    label_the_details.append(details_label(frame_player,player_data['position'],480,300))
                except:
                    messagebox.showinfo('Message','Player not found')

            def on_entry_click_1(event):
                if player_search_entry.get() == "Player's name":
                    player_search_entry.delete(0, END)  
            def on_focus_out_1(event):
                if player_search_entry.get() == '':
                    player_search_entry.insert(0, "Player's name")
            frame_player = Frame(frame_overview,bg="sky blue",height=600,width=1050)
            frame_player.place(x=0,y=70)
            player_search_entry = Entry(frame_player,font=('Segoe Print', '12', 'bold'))
            player_search_entry.place(x=10,y=10)
            player_search_entry.insert(0,"Player's name")
            player_search_entry.bind('<FocusIn>',on_entry_click_1)
            player_search_entry.bind('<FocusOut>',on_focus_out_1)
            player_search_button = Button(frame_player,text="Search",font=('Segoe Print', '8', 'bold'),bg="sky blue",command=player_search)
            player_search_button.place(x=255,y=10)
  
    options = ["League", "Team", "Player"]
    selected_option = StringVar(frame_overview)
    selected_option.set("Choose an option")  # Set the default selected option
    option_menu = OptionMenu(frame_overview, selected_option, *options, command=overview_selection)
    option_menu.place(x=890,y=15)
    option_menu.config(font=('Segoe Print', '10', 'bold'),width=12,bg="sky blue")

def news_frame():
    frame_news =Frame(right_frame,width=1050, height=668, bg="sky blue", border=1)
    frame_news.place(x=0,y=0)
    frame_news.place(x=0,y=0)
    label_news = Label(frame_news,text="News & Updates",font=('Segoe Print', '17', 'bold'),bg='sky blue')
    label_news.place(x=10,y=10)
    separator = ttk.Separator(frame_news, orient='horizontal', style='Separator.TSeparator')
    separator.place(x=0, y=65, relwidth=1)
    
    
def matches_frame():
    frame_matches =Frame(right_frame,width=1050, height=668, bg="sky blue", border=1)
    frame_matches.place(x=0,y=0)
    label_matches = Label(frame_matches,text="Matches",font=('Segoe Print', '17', 'bold'),bg='sky blue')
    label_matches.place(x=10,y=10)
    separator = ttk.Separator(frame_matches, orient='horizontal', style='Separator.TSeparator')
    separator.place(x=0, y=65, relwidth=1)
        # Read the data from the Excel file
    date_time = pd.read_excel("C:/Users/Dell/Desktop/Python Project/Points/Point Table.xlsx",sheet_name="Matches Date")

    # Create a pandas DataFrame from the data
    df = pd.DataFrame(date_time)

    # Create a treeview widget to display the data
    treeview = ttk.Treeview(frame_matches, style='Custom.Treeview')
    treeview.place(x=10, y=80, width=1030, height=570)

    # Configure the treeview columns
    treeview["columns"] = list(df.columns)
    treeview["show"] = "headings"

    # Define the custom column widths as a list
    column_widths = [30,30,10,200,10,10,10,200]  # Add more widths for additional columns

    # Create a custom style for the treeview
    style = ttk.Style()
    style.configure('Custom.Treeview',font=('Arial', 12))  # Set the font for the table

    style.configure('Custom.Treeview.Heading', font=('Arial', 12, 'bold'))

    # Add the column headers to the treeview
    for i, column in enumerate(df.columns):
        treeview.heading(column, text=column)

        # Get the width for the column
        width = column_widths[i] if i < len(column_widths) else 100  # Default width is 100 if not specified
        treeview.heading(column, text=column, anchor='w')

        # Set the width of the column in the treeview
        treeview.column(column, width=width)

    # Add the data rows to the treeview
    for index, row in df.iterrows():
        treeview.insert("", "end", values=list(row))
    style.configure('Custom.Treeview', rowheight=38)
    style.configure('Custom.Treeview', spacing=5)


def standings_frame():
    frame_standings = Frame(right_frame, width=1050, height=668, bg="sky blue", border=1)
    frame_standings.place(x=0, y=0)
    label_standings = Label(frame_standings, text="Standings", font=('Segoe Print', 17, 'bold'), bg='sky blue')
    label_standings.place(x=10, y=10)
    separator = ttk.Separator(frame_standings, orient='horizontal', style='Separator.TSeparator')
    separator.place(x=0, y=65, relwidth=1)

    # Read the data from the Excel file
    standings_data = pd.read_excel("C:/Users/Dell/Desktop/Python Project/Points/Point Table.xlsx")

    # Create a pandas DataFrame from the data
    df = pd.DataFrame(standings_data)

    # Create a treeview widget to display the data
    treeview = ttk.Treeview(frame_standings, style='Custom.Treeview')
    treeview.place(x=10, y=80, width=1030, height=570)

    # Configure the treeview columns
    treeview["columns"] = list(df.columns)
    treeview["show"] = "headings"

    # Define the custom column widths as a list
    column_widths = [30, 200, 50, 50, 50, 50, 50, 50, 50, 30]  # Add more widths for additional columns

    # Create a custom style for the treeview
    style = ttk.Style()
    style.configure('Custom.Treeview',font=('Arial', 12))  # Set the font for the table

    style.configure('Custom.Treeview.Heading', font=('Arial', 12, 'bold'))

    # Add the column headers to the treeview
    for i, column in enumerate(df.columns):
        treeview.heading(column, text=column,anchor='w')

        # Get the width for the column
        width = column_widths[i] if i < len(column_widths) else 100  # Default width is 100 if not specified

        # Set the width of the column in the treeview
        treeview.column(column, width=width)


    # Add the data rows to the treeview
    for index, row in df.iterrows():
        treeview.insert("", "end", values=list(row))
    style.configure('Custom.Treeview', rowheight=38)
    style.configure('Custom.Treeview', spacing=5)
    
def personaliztion_frame():
    global frame_personaliztion
    frame_personaliztion =Frame(right_frame,width=1050, height=668, bg="sky blue", border=1)
    frame_personaliztion.place(x=0,y=0)
    label_personalization = Label(frame_personaliztion,text="Pesronalization",font=('Segoe Print', '17', 'bold'),bg='sky blue')
    label_personalization.place(x=10,y=10)
    separator = ttk.Separator(frame_personaliztion, orient='horizontal', style='Separator.TSeparator')
    separator.place(x=0, y=65, relwidth=1)
    def profile():
        highlight_button(personaliztion_button[0])
        for btn in personaliztion_button[1:]:
            reset_button(btn)
        frame_personaliztion.destroy()
        profile_frame = Frame(right_frame,width=1050, height=668, bg="sky blue", border=1)
        profile_frame.place(x=0,y=0)
        label_profile = Label(profile_frame,text="User Profile",font=('Segoe Print', '16', 'bold'), bg="sky blue")
        label_profile.place(x=10,y=10)
        separator = ttk.Separator(profile_frame, orient='horizontal', style='Separator.TSeparator')
        separator.place(x=0, y=65, relwidth=1)
        
        full_name_label = Label(profile_frame,text="Full Name:",font=('Segoe Print', '14', 'bold'), bg="sky blue")
        full_name_label.place(x=350,y=200)
        full_name_entry = Entry(profile_frame,font=('Segoe Print', '12', 'bold'),width=22)
        full_name_entry.place(x=480,y=200)
        phone_num_label = Label(profile_frame,text="Phone No.:",font=('Segoe Print', '14', 'bold'), bg="sky blue")
        phone_num_label.place(x=350,y=250)
        phone_num_entry = Entry(profile_frame,font=('Segoe Print', '12', 'bold'),width=22)
        phone_num_entry.place(x=480,y=250)
        email_add_label = Label(profile_frame,text="Email:",font=('Segoe Print', '14', 'bold'), bg="sky blue")
        email_add_label.place(x=350,y=300)
        email_add_entry = Entry(profile_frame,font=('Segoe Print', '12', 'bold'),width=22)
        email_add_entry.place(x=480,y=300)

        def enable_entry():
            full_name_entry.config(state='normal')
            phone_num_entry.config(state='normal')
            email_add_entry.config(state='normal')
            update_button.config(state='disabled')
            save_button = Button(profile_frame,text="Save",font=('Segoe Print', '12', 'bold'), bg="sky blue",command=enable_entry)
            save_button.place(x=350,y=350)

        update_button = Button(profile_frame,text="Edit",font=('Segoe Print', '12', 'bold'), bg="sky blue",command=enable_entry)
        update_button.place(x=350,y=350)
        
        full_name_entry.insert(0,user_data['fullName'])
        full_name_entry.config(state='disabled')
        phone_num_entry.insert(0,phone)
        phone_num_entry.config(state='disabled')
        email_add_entry.insert(0,user_data['email'])
        email_add_entry.config(state='disabled')

    def log_out():
        highlight_button(personaliztion_button[1])
        for btn in personaliztion_button[:1]+personaliztion_button[2:]:
            reset_button(btn)

        confirm = messagebox.askyesno('Logout','Are you sure want to logout?')
        if confirm:
            app.destroy()
            import login_page
        else:
            pass
    def delete():
        delete_window = Toplevel(frame_personaliztion)
        delete_window.title('Delete Account')
        delete_window.geometry('250x350')
        delete_window.config(bg="sky blue")
        def delete_acc():
            password_delete = delete_password_entry.get()
            if password_delete == user_data['password']:
                football_collection.delete_one({'password':user_data['password']})
                messagebox.showinfo("Account Deleted", "Your account has been deleted successfully.")
                app.destroy()
                import login_page
            else:
                messagebox.showerror("Delete Account", "Wrong password.")

        highlight_button(personaliztion_button[2])
        for btn in personaliztion_button[:2]+personaliztion_button[3:]:
            reset_button(btn)
        
        delete_password_label = Label(delete_window,text="Please enter your password:",bg="sky blue", font=('Segoe Print', '12', 'bold'))
        delete_password_label.place(x=10,y=120)
        delete_password_entry = Entry(delete_window, font=('Segoe Print', '12', 'bold'),width=19,show="*")
        delete_password_entry.place(x=10,y=160)
        delete_btn = Button(delete_window,text="DELETE",bg="sky blue", font=('Segoe Print', '10', 'bold'),command=delete_acc)
        delete_btn.place(x=175,y=240)
        # messagebox.askyesno('','Are you sure want to delete account?')
        delete_window.mainloop()
 
    def create_personalization_btns(frame_personaliztion, image_path1, text, x, y,cmd):
        personalization_icon = Image.open(image_path1)
        personalization_icon = personalization_icon.resize((20, 20))
        personalization_image = ImageTk.PhotoImage(personalization_icon)
        per_img_label = Label(frame_personaliztion, image=personalization_image, border=0, bg="sky blue")
        per_img_label.image = personalization_image
        per_img_label.place(x=x, y=y)
        per_btn = Button(frame_personaliztion, text=text,height=0, border=0, bg="sky blue", font=('Segoe Print', '12', 'bold'), width=20, anchor='w',command=cmd)
        per_btn.place(x=x+30, y=y-10)
        return per_btn
    personaliztion_button = []
    personaliztion_button.append(create_personalization_btns(frame_personaliztion,'C:/Users/Dell/Desktop/Python Project/Images/profile.png',"Profile",10,100,profile))
    personaliztion_button.append(create_personalization_btns(frame_personaliztion,'C:/Users/Dell/Desktop/Python Project/Images/logout.png',"Log Out",10,150,log_out))
    personaliztion_button.append(create_personalization_btns(frame_personaliztion,'C:/Users/Dell/Desktop/Python Project/Images/delete.png',"Delete Account",10,200,delete))
     
def feedback_frame():
    frame_feedback =Frame(right_frame,width=1050, height=668, bg="sky blue", border=1)
    frame_feedback.place(x=0,y=0)
    frame_feedback.place(x=0,y=0)
    label_feedback = Label(frame_feedback,text="Feedback & Support",font=('Segoe Print', '17', 'bold'),bg='sky blue')
    label_feedback.place(x=10,y=10)
    separator = ttk.Separator(frame_feedback, orient='horizontal', style='Separator.TSeparator')
    separator.place(x=0, y=65, relwidth=1)

app.mainloop()

