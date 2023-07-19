# Importing all the required libraries
from tkinter import *
from tkinter import ttk,messagebox,Label,PhotoImage, filedialog
from PIL import Image, ImageTk
from pymongo import MongoClient
from base64 import *
import io,webbrowser
import pandas as pd
import hashlib
from ButtonCreation import *

try:
    # Connecting to the database
    football_client = MongoClient('mongodb://localhost:27017/')
    football_database = football_client['football_database']
    football_collection = football_database['users']
    player_collection = football_database['players']
    team_collection = football_database['teams']
    picture_collection = football_database['picture']

except Exception as e:
    messagebox.showerror('Database Connection Error',str(e))

try:
    # Reading the phone number from a file
    with open("Scripts\\phone_number.txt", "r") as file:
        phone = file.read().strip()
    user_data = football_collection.find_one({"phone":phone})
except Exception as e:
    messagebox.showerror('System Error',"There is an error in the system.\nYou may face some problems while using app.\nWe will try to fix it asap.")


    
def home_section():
    '''
    Display the honme section.
    '''

    global frame_signup_back
    global frame_home
    frame_home =Frame(rightFrame,width=1070, height=668, bg="#FFFACD", border=1)
    frame_home.place(x=0,y=0)

    def playlive():
        webbrowser.open("https://www.youtube.com/live/O2ANLnuEBmg")
    frame_signup_back = Frame(frame_home, width = 540, bg = "#FFFACD", height = 180, highlightthickness = 1, relief = RAISED, highlightcolor = "#000")
    frame_signup_back.place(x = 120, y = 110)
    logoLabel = Label(frame_signup_back, image = imageLogo, bg = "#FFFACD")
    logoLabel.place(x = 350, y = 10)

    def facebook(e = None):
        webbrowser.open("https://www.facebook.com/Saugat Shahi Thakuri")
        facebook_button.config(fg = "#000000")
        facebook_button.config(bg = "#FFFACD")
    def facebook_leave(e = None):
        facebook_button.config(fg = "blue")
        facebook_button.config(bg = "#FFFACD")

    facebook_button = Button(frame_signup_back, image = iconRight, compound = RIGHT, bg = "#FFFACD",text="Connect with facebook  ", border = 0, font = ("Yu Gothic UI Semibold", 10, "bold"), command = facebook, fg = "blue")
    facebook_button.place(x = 32, y = 86)
    facebook_button.bind("<Button-1>", facebook)
    facebook_button.bind("<Leave>", facebook_leave)

    signup_frame_text = Label(frame_signup_back, text = "Your Favorite Teams in one place", font = ("League Spartan Thin SemiBold", 14), bg = "#FFFACD", fg = "#000000")
    signup_frame_text.place(x = 30, y = 36)

    live_match1_frame = Frame(frame_home, width = 244, height = 314)
    live_match1_frame.place(x = 130, y = 320)

    live_match2_frame = Frame(frame_home, width = 244, height = 314)
    live_match2_frame.place(x = 406, y = 320)

    live_ground_frame = Frame(frame_home, width = 232, height = 330, border = 2)
    live_ground_frame.place(x = 740, y = 114)
    groundLabel = Label(live_ground_frame, image = imageGround, relief = SOLID)
    groundLabel.pack()

    scores_frame = Frame(frame_home, width = 230, height = 100)
    scores_frame.place(x = 740, y = 474)

    label_live_match = Label(frame_home, text = "Streaming", font = ("Yu Gothic UI Semibold", 10), bg = "#FFFACD", fg = "black")
    label_live_match.place(x = 754, y = 84)

    watch_live = Button(frame_home, text = "LIVE", bg = "#FFFACD", border = 0, width = 5, height = 0, command = playlive, font = ("Yu Gothic UI Semibold", 10), fg = "red")
    watch_live.place(x = 908, y = 84)
    homeButton.config(fg="red", bg = "#FFFACD")
    liveButton.config(fg = "black")
    matchButton.config(fg = "black")
    overviewButton.config(fg = "black")
    standingsButton.config(fg = "black")
    personalizeButton.config(fg = "black")
    feedbackButton.config(fg = "black") 

    label_home = Label(frame_home,text="Home",font=('League Spartan Medium', '17', 'bold'),bg='#FFFACD')
    label_home.place(x=10,y=10)
    separator = Frame(frame_home, width = 1070, height = 2, bg = "#000")
    separator.place(x = 0, y = 64)
    try:
        welcome_text = "Hello! "+ user_data['fullName']
        welcome_text_label = Label(leftFrame,text=welcome_text,font=('League Spartan Medium', '11', 'bold'), bg="#FFFACD",anchor='center')
        welcome_text_label.place(x=10,y=10)
    except:
        pass

    try:
        frameFeedback.destroy()
    except NameError:
        pass

def live_section():
    '''
    Display the live section.
    '''

    homeButton.config(fg="black")
    liveButton.config(fg = "red")
    matchButton.config(fg = "black")
    overviewButton.config(fg = "black")
    standingsButton.config(fg = "black")
    personalizeButton.config(fg = "black")
    feedbackButton.config(fg = "black")

    frame_live = Frame(rightFrame, width=1070, height=668, bg="#FFFACD", border=1)
    frame_live.place(x=0, y=0)
    label_live = Label(frame_live, text="Live", font=('League Spartan Medium', '17', 'bold'), bg='#FFFACD')
    label_live.place(x=10, y=10)
    separator = Frame(frame_live, width = 1070, height = 2, bg = "#000")
    separator.place(x = 0, y = 64)

    # Read the data from the Excel file
    live_data = pd.read_excel("C:Points\\Point Table.xlsx", sheet_name="Live")
    # Create a pandas DataFrame from the data
    df = pd.DataFrame(live_data)
    # Create a treeview widget to display the data
    treeview1 = ttk.Treeview(frame_live, style='Custom.Treeview')
    treeview1.place(x=17, y=100, width=1030, height=558)
    # Configure the treeview columns
    treeview1["columns"] = list(df.columns)
    treeview1["show"] = "headings"
    # Define the custom column widths as a list
    column_widths = [25, 25, 5, 50, 20, 50, 300]  # Add more widths for additional columns
    # Create a custom style for the treeview
    style = ttk.Style()
    style.configure('Custom.Treeview', font=('Arial', 12), background='#FFFACD', foreground='black')  # Set the font and colors for the table
    style.configure('Custom.Treeview.Heading', font=('Arial', 12, 'bold'),background='#FFFACD')
    # Add the column headers to the treeview
    for i, column in enumerate(df.columns):
        treeview1.heading(column, text=column)
        # Get the width for the column
        width = column_widths[i] if i < len(column_widths) else 100  # Default width is 100 if not specified
        treeview1.heading(column, text=column, anchor='w')
        # Set the width of the column in the treeview
        treeview1.column(column, width=width)
    # Add the data rows to the treeview in reverse order
    for index, row in df[::-1].iterrows():
        treeview1.insert("", "end", values=list(row))
    style.configure('Custom.Treeview', rowheight=38)
    style.configure('Custom.Treeview', spacing=5)
    # Function to open the link in a web browser
    def open_link(event):
        # Retrieve the selected row's data
        item = treeview1.selection()
        values = treeview1.item(item)["values"]
        link = values[6]
        # Open the link in a web browser
        webbrowser.open(link)
    treeview1.bind("<<TreeviewSelect>>", open_link)
  

    try:
        frameFeedback.destroy()
    except NameError:
        pass

def overview_section():
    '''
    Display the overview section.
    '''

    homeButton.config(fg="black")
    liveButton.config(fg = "black")
    matchButton.config(fg = "black")
    overviewButton.config(fg = "red")
    standingsButton.config(fg = "black")
    personalizeButton.config(fg = "black")
    feedbackButton.config(fg = "black")

    global frame_overview
    frame_overview =Frame(rightFrame,width=1070, height=668, bg="#FFFACD", border=1)
    frame_overview.place(x=0,y=0)
    frame_overview.place(x=0,y=0)
    label_overview = Label(frame_overview,text="Overview",font=('League Spartan Medium', '17', 'bold'),bg='#FFFACD')
    label_overview.place(x=10,y=10)
    separator = Frame(frame_overview, width = 1070, height = 2, bg = "#000")
    separator.place(x = 0, y = 64)
    def overview_selection(select):
        '''
        Display the overview based on the selection from the option.
        Args:
            select: The selected option from the OptionMenu widget.
        '''
        global team_search_entry
        if select == "League":
            frame_league = Frame(frame_overview,bg="blue",height=600,width=1050)
            frame_league.place(x=0,y=70)
        elif select==options[1]:
            def team_search():
                '''
                Search the team and display it's information.
                '''
                team_data = team_collection.find_one({'name':team_search_entry.get()})
                encoded_logo = team_data['image']
                logo_data = b64decode(encoded_logo)
                logo = Image.open(io.BytesIO(logo_data))
                logo = logo.resize((150,200))
                # Convert the logo to a Tkinter-compatible format
                tk_logo = ImageTk.PhotoImage(logo)
                # Create a Tkinter label and display the logo
                logo_label = Label(frame_team, image=tk_logo)
                logo_label.image = tk_logo
                logo_label.place(x=150,y=150)

                def label_team_details(frame_team,label_text,x,y):
                    '''
                    Label and display the details of team.

                    Args:
                        frame_team: The frame for labeling and displaying the team information.
                        label_text: The text to display on the label.
                        x: x-coordinate of the label's position.
                        y: y-coordinate of the label's position.
                    '''
                    label_team_info = Label(frame_team,text=label_text,font=('Segoe Print', '12', 'bold'),bg="#FFFACD")
                    label_team_info.place(x=x,y=y)
                team_info_list = []
                if team_data is not None:
                    team_info_list.append(label_team_details(frame_team,"Club Name:",350,150))
                    team_info_list.append(label_team_details(frame_team,team_data['name'],480,150))
                    team_info_list.append(label_team_details(frame_team,"Founded Year:",350,180))
                    team_info_list.append(label_team_details(frame_team,team_data['founded'],480,180))
                    team_info_list.append(label_team_details(frame_team,"Location:",350,210))
                    team_info_list.append(label_team_details(frame_team,team_data['location'],480,210))
                    team_info_list.append(label_team_details(frame_team,"Stadium:",350,240))
                    team_info_list.append(label_team_details(frame_team,team_data['stadium'],480,240))
                    team_info_list.append(label_team_details(frame_team,"President:",350,270))
                    team_info_list.append(label_team_details(frame_team,team_data['president'],480,270))
                    team_info_list.append(label_team_details(frame_team,"Manager:",350,300))
                    team_info_list.append(label_team_details(frame_team,team_data['manager'],480,300))
                    team_info_list.append(label_team_details(frame_team,"Captain:",350,330))
                    team_info_list.append(label_team_details(frame_team,team_data['captain'],480,330))
            def on_entry_click(event):
                '''
                Perform actions when the team search entry field is clicked.
                
                Args:
                    event: The event object.
                '''
                if team_search_entry.get() == "Team's name":
                    team_search_entry.delete(0, END)  
            def on_focus_out(event):
                '''
                Perform actions when the team search entry field loses focus.
                
                Args:
                    event: The event object.
                '''
                if team_search_entry.get() == '':
                    team_search_entry.insert(0, "Team's name")  
            frame_team = Frame(frame_overview,bg="#FFFACD",height = 600, width = 1050)
            frame_team.place(x=0,y=70)
            team_search_entry = Entry(frame_team,font=('Segoe Print', '12', 'bold'))
            team_search_entry.place(x=10,y=10)
            team_search_button = Button(frame_team,text="Search",font=('Segoe Print', '8', 'bold'),bg="#FFFACD",command=team_search)
            team_search_button.place(x=255,y=10)
            team_search_entry.insert(0,"Team's name")
            team_search_entry.bind('<FocusIn>',on_entry_click)
            team_search_entry.bind('<FocusOut>',on_focus_out)
        elif select == options[2]:
            def player_search():
                '''
                Display the searched player information.
                '''
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
                    image_label = Label(frame_player, image = tk_image)
                    image_label.image = tk_image
                    image_label.place(x = 150,y = 150)
                    def details_label(frame_player,players_text,x,y):
                        '''
                        Create and place a label of player's details.

                        Args:
                            frame_player: The parent frame to place the label.
                            players_text: The text to display in label.
                            x: x-coordinate of the label's position.
                            y: y-coordinate of the label's position.

                        '''
                        label_details = Label(frame_player,text=players_text,font=('Segoe Print', '12', 'bold'),bg="#FFFACD")
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
                '''
                Perform actions when the team search entry field is clicked.
                
                Args:
                    event: The event object.
                '''
                if player_search_entry.get() == "Player's name":
                    player_search_entry.delete(0, END)  
            def on_focus_out_1(event):
                '''
                Perform actions when the team search entry field loses focus.
                
                Args:
                    event: The event object.
                '''
                if player_search_entry.get() == '':
                    player_search_entry.insert(0, "Player's name")
            frame_player = Frame(frame_overview,bg="#FFFACD",height = 600,width = 1050)
            frame_player.place(x = 0,y = 70)
            player_search_entry = Entry(frame_player,font=('Segoe Print', '12', 'bold'))
            player_search_entry.place(x = 10,y = 10)
            player_search_entry.insert(0,"Player's name")
            player_search_entry.bind('<FocusIn>',on_entry_click_1)
            player_search_entry.bind('<FocusOut>',on_focus_out_1)
            player_search_button = Button(frame_player,text="Search",font=('Segoe Print', '8', 'bold'),bg="#FFFACD",command=player_search)
            player_search_button.place(x=255,y=10)
  
    options = ["League", "Team", "Player"]
    selected_option = StringVar(frame_overview)
    selected_option.set("Choose an option")  # Set the default selected option
    option_menu = OptionMenu(frame_overview, selected_option, *options, command=overview_selection)
    option_menu.place(x=890,y=15)
    option_menu.config(font=('Segoe Print', '10', 'bold'),width=12,bg="#FFFACD")

    try:
        frameFeedback.destroy()
    except NameError:
        pass

def matches_section():
    '''
    Display the matches section.
    '''

    homeButton.config(fg="black")
    liveButton.config(fg = "black")
    matchButton.config(fg = "red")
    overviewButton.config(fg = "black")
    standingsButton.config(fg = "black")
    personalizeButton.config(fg = "black")
    feedbackButton.config(fg = "black")

    frame_matches =Frame(rightFrame,width=1070, height=668, bg="#FFFACD", border=1)
    frame_matches.place(x=0,y=0)
    label_matches = Label(frame_matches,text="Matches",font=('League Spartan Medium', '17', 'bold'),bg='#FFFACD')
    label_matches.place(x=10,y=10)
    separator = Frame(frame_matches, width = 1070, height = 2, bg = "#000")
    separator.place(x = 0, y = 64)
        # Read the data from the Excel file
    date_time = pd.read_excel("C:Points\\Point Table.xlsx",sheet_name="Matches Date")
    # Create a pandas DataFrame from the data
    df = pd.DataFrame(date_time)
    # Create a treeview widget to display the data
    treeview = ttk.Treeview(frame_matches, style='Custom.Treeview')
    treeview.place(x=17, y=100, width=1030, height=558)
    # Configure the treeview columns
    treeview["columns"] = list(df.columns)
    treeview["show"] = "headings"
    # Define the custom column widths as a list
    column_widths = [30,30,10,200,10,10,10,200]  # Add more widths for additional columns
    # Create a custom style for the treeview
    style = ttk.Style()
    style.configure('Custom.Treeview', font=('Arial', 12), background='#FFFACD', foreground='black')  # Set the font and colors for the table
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
    for index, row in df[::-1].iterrows():
        treeview.insert("", "end", values=list(row))
    style.configure('Custom.Treeview', rowheight=38)
    style.configure('Custom.Treeview', spacing=5)

    try:
        frameFeedback.destroy()
    except NameError:
        pass

def standing_section():
    '''
    Display the standing section.
    '''

    homeButton.config(fg="black")
    liveButton.config(fg = "black")
    matchButton.config(fg = "black")
    overviewButton.config(fg = "black")
    standingsButton.config(fg = "red")
    personalizeButton.config(fg = "black")
    feedbackButton.config(fg = "black")

    frame_standings = Frame(rightFrame, width=1070, height=668, bg="#FFFACD", border=1)
    frame_standings.place(x=0, y=0)
    label_standings = Label(frame_standings, text="Standings", font=('Segoe Print', 17, 'bold'), bg='#FFFACD')
    label_standings.place(x=10, y=10)
    separator = Frame(frame_standings, width = 1070, height = 2, bg = "#000")
    separator.place(x = 0, y = 64)
    # Read the data from the Excel file
    standings_data = pd.read_excel("C:Points\\Point Table.xlsx")
    # Create a pandas DataFrame from the data
    df = pd.DataFrame(standings_data)
    # Create a treeview widget to display the data
    treeview = ttk.Treeview(frame_standings, style='Custom.Treeview')
    treeview.place(x=17, y=100, width=1030, height=558)

    # Configure the treeview columns
    treeview["columns"] = list(df.columns)
    treeview["show"] = "headings"

    # Define the custom column widths as a list
    column_widths = [30, 200, 50, 50, 50, 50, 50, 50, 50, 30]  # Add more widths for additional columns

    # Create a custom style for the treeview
    style = ttk.Style()
    style.configure('Custom.Treeview', font=('Arial', 12), background='#FFFACD', foreground='black')  # Set the font and colors for the table

    style.configure('Custom.Treeview.Heading', font=('Arial', 12, 'bold'),background='#FFFACD', foreground='black')

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

    try:
        frameFeedback.destroy()
    except NameError:
        pass
    
def personalization_section():
    '''
    Display the personalization section.
    '''
    homeButton.config(fg="black")
    liveButton.config(fg = "black")
    matchButton.config(fg = "black")
    overviewButton.config(fg = "black")
    standingsButton.config(fg = "black")
    personalizeButton.config(fg = "red")
    feedbackButton.config(fg = "black")

    global frame_personalization
    frame_personalization = Frame(rightFrame, width=1070, height=668, bg="#FFFACD", border=1)
    frame_personalization.place(x=0, y=0)

    label_personalization = Label(frame_personalization, text="Personalization", font=('Segoe Print', '17', 'bold'), bg='#FFFACD')
    label_personalization.place(x=10, y=10)

    separator = Frame(frame_personalization, width = 1070, height = 2, bg = "#000")
    separator.place(x = 0, y = 64)

    def profile():
        '''
        Display the user's information.
        '''


        profile_frame = Frame(rightFrame, width=1070, height=668, bg="#FFFACD", border=1)
        profile_frame.place(x=0, y=0)

        label_profile = Label(profile_frame, text="User Profile", font=('Segoe Print', '16', 'bold'), bg="#FFFACD")
        label_profile.place(x=10, y=10)

        separator = Frame(profile_frame, width = 1070, height = 2, bg = "#000")
        separator.place(x = 0, y = 64)

        full_name_label = Label(profile_frame, text="Full Name:", font=('Segoe Print', '14', 'bold'), bg="#FFFACD")
        full_name_label.place(x=350, y=200)

        full_name_entry = Entry(profile_frame, font=('Segoe Print', '12', 'bold'), width=22)
        full_name_entry.place(x=480, y=200)

        phone_num_label = Label(profile_frame, text="Phone No.:", font=('Segoe Print', '14', 'bold'), bg="#FFFACD")
        phone_num_label.place(x=350, y=250)

        phone_num_entry = Entry(profile_frame, font=('Segoe Print', '12', 'bold'), width=22)
        phone_num_entry.place(x=480, y=250)

        email_add_label = Label(profile_frame, text="Email:", font=('Segoe Print', '14', 'bold'), bg="#FFFACD")
        email_add_label.place(x=350, y=300)

        email_add_entry = Entry(profile_frame, font=('Segoe Print', '12', 'bold'), width=22)
        email_add_entry.place(x=480, y=300)

        def enable_entry():
            '''
            Enable the entry fields for editing and disable the update button.
            '''
            full_name_entry.config(state = NORMAL)
            phone_num_entry.config(state = NORMAL)
            email_add_entry.config(state = NORMAL)
            update_button.config(state = DISABLED)
            save_button = Button(profile_frame, text="Save", font=('Segoe Print', '12', 'bold'), bg="#FFFACD", command=save_profile)
            save_button.place(x=350, y=350)

        def save_profile():
            '''
            Save the updated profile information to the database and disable the entry fields.
            '''
            try:
                new_full_name = full_name_entry.get()
                new_phone_num = phone_num_entry.get()
                new_email_add = email_add_entry.get()

                football_collection.update_one({'password': user_data['password']}, {'$set': {'fullName': new_full_name, 'phone': new_phone_num, 'email': new_email_add}})


                # Display a success message
                messagebox.showinfo("Profile Updated", "Your profile has been updated successfully.")

                # Disable the entry fields again
                full_name_entry.config(state = DISABLED)
                phone_num_entry.config(state = DISABLED)
                email_add_entry.config(state = DISABLED)
                update_button.config(state = NORMAL)

            except:
                messagebox.showerror("System Error!", "Sorry for the inconvenience. We are working on it.")

        update_button = Button(profile_frame, text="Edit", font=('Segoe Print', '12', 'bold'), bg="#FFFACD", command=enable_entry)
        update_button.place(x=350, y=350)

        full_name_entry.insert(0, user_data['fullName'])
        full_name_entry.config(state = DISABLED)

        phone_num_entry.insert(0, phone)
        phone_num_entry.config(state = DISABLED)

        email_add_entry.insert(0, user_data['email'])
        email_add_entry.config(state = DISABLED)

    def log_out():

        confirm = messagebox.askyesno('Logout', 'Are you sure you want to logout?')
        if confirm:
            app.destroy()
            import Login
        else:
            pass
    
    def change():
        '''
        Open another window and ask user to enter the current password.
        '''
        password_change_window = Toplevel(frame_personalization)
        password_change_window.title('Change your password')
        password_change_window.geometry('280x350')
        password_change_window.config(bg="#FFFACD")

        def password_change(): 
            '''
            Open the password change window.
            '''
            try:
                if user_data['password'] == hashlib.sha256(current_password_entry.get().encode()).hexdigest():
                    password_change_window.destroy()
                    password_change_window1 = Toplevel(frame_personalization)
                    password_change_window1.title('Change your password')
                    password_change_window1.geometry('280x350')
                    password_change_window1.config(bg="#FFFACD")

                    def confirm_change():
                        '''
                        Change the password and update in the database.
                        '''
                        if new_password_entry.get() == re_password_entry.get():
                            # Update the password in the database
                            new_hash_psw=hashlib.sha256(new_password_entry.get().encode()).hexdigest()
                            football_collection.update_one({'password': user_data['password']}, {'$set': {'password': new_hash_psw}})
                            messagebox.showinfo('Password Change', 'Password updated successfully.')
                        else:
                            messagebox.showerror('Password Change', "Password doesn't match.")

                    new_password_label = Label(password_change_window1, text='Enter New Password:', bg="#FFFACD", font=('Segoe Print', '12', 'bold'))
                    new_password_label.place(x=10, y=20)
                    new_password_entry = Entry(password_change_window1, font=('Segoe Print', '12', 'bold'),show='*')
                    new_password_entry.place(x=10, y=50)

                    re_password_label = Label(password_change_window1, text='Re-enter New Password:', bg="#FFFACD", font=('Segoe Print', '12', 'bold'))
                    re_password_label.place(x=10, y=90)
                    re_password_entry = Entry(password_change_window1, font=('Segoe Print', '12', 'bold'),show='*')
                    re_password_entry.place(x=10, y=120)

                    change_btn = Button(password_change_window1, text='Change', bg="sky blue", font=('Segoe Print', '12', 'bold'), command=confirm_change)
                    change_btn.place(x=180, y=170)

                else:
                    messagebox.showerror('Password Change', 'Wrong password')
            except:
                messagebox.showerror('System Error','Sorry for the inconvenience. We will fix it ASAP.')
        current_password_label = Label(password_change_window, text='Current Password:', bg="#FFFACD", font=('Segoe Print', '12', 'bold'))
        current_password_label.place(x=10, y=20)
        current_password_entry = Entry(password_change_window, font=('Segoe Print', '12', 'bold'),show='*')
        current_password_entry.place(x=10, y=50)

        next_btn = Button(password_change_window, text='Next', bg="#FFFACD", font=('Segoe Print', '12', 'bold'), command=password_change)
        next_btn.place(x=200, y=100)


    def delete():
        '''
        Open the window for delete.
        '''
        delete_window = Toplevel(frame_personalization)
        delete_window.title('Delete Account')
        delete_window.geometry('250x350')
        delete_window.config(bg="#FFFACD")

        def delete_acc():
            '''
            Delete the user account.
            '''
            account_delete = hashlib.sha256(delete_password_entry.get().encode()).hexdigest()
            if account_delete == user_data['password']:
                football_collection.delete_one({'password': user_data['password']})
                messagebox.showinfo("Account Deleted", "Your account has been deleted successfully.")
                app.destroy()
                import Login
            else:
                messagebox.showerror("Delete Account", "Wrong password.")

        # highlight_button(personaliztion_button[3])
        # for btn in personaliztion_button[:3] + personaliztion_button[4:]:
        #     reset_button(btn)

        delete_password_label = Label(delete_window, text="Please enter your password:", bg="#FFFACD", font=('Segoe Print', '12', 'bold'))
        delete_password_label.place(x=10, y=120)

        delete_password_entry = Entry(delete_window, font=('Segoe Print', '12', 'bold'), width=19, show="*")
        delete_password_entry.place(x=10, y=160)

        delete_btn = Button(delete_window, text="DELETE", bg="#FFFACD", font=('Segoe Print', '10', 'bold'), command=delete_acc)
        delete_btn.place(x=175, y=240)

        delete_window.mainloop()
    def setting():
        setting_window = Toplevel(frame_personalization)
        setting_window.title('Setting')
        setting_window.resizable(0,0)
        setting_window.geometry('250x350')
        setting_window.config(bg="#FFFACD")
        change_font_label = Label(setting_window,text="Change App Font",font=("Segoe Print", '12', ''),bg="#FFFACD")
        change_font_label.place(x=10,y=15)

    personaliztion_button = []
    personaliztion_button.append(create_personalization_btns(frame_personalization, 'C:Images\\profile.png', "Profile", 10, 100, profile))
    personaliztion_button.append(create_personalization_btns(frame_personalization, 'C:Images\\logout.png', "Log Out", 10, 150, log_out))
    personaliztion_button.append(create_personalization_btns(frame_personalization, 'C:Images\\change.png', "Change Password", 10, 200, change))
    personaliztion_button.append(create_personalization_btns(frame_personalization, 'C:Images\\delete.png', "Delete Account", 10, 250, delete))
    personaliztion_button.append(create_personalization_btns(frame_personalization, 'C:Images\\setting.png', "Setting", 10, 300, setting))



    try:
        frameFeedback.destroy()
    except NameError:
        pass
    
def feedback_section():

    homeButton.config(fg="black")
    liveButton.config(fg="black")
    matchButton.config(fg="black")
    overviewButton.config(fg="black")
    standingsButton.config(fg="black")
    personalizeButton.config(fg="black")
    feedbackButton.config(fg="red")

    global frameFeedback

    frameFeedback = Frame(rightFrame, width=1070, height=668, bg="#FFFACD", border=1)
    frameFeedback.place(x=0, y=0)

    feedbackLabel = Label(frameFeedback, image=ImageFeedback, border=0)
    feedbackLabel.place(x=-60, y=102)

    labelFeedback = Label(frameFeedback, text="Feedback & Support", font=('League Spartan Medium', '17', 'bold'), bg='#FFFACD')
    labelFeedback.place(x=20, y=10)

    separator = Frame(frameFeedback, width=1070, height=2, bg="#000")
    separator.place(x=0, y=64)

    try:
        feedCollection = football_database['feedBacks']
    except Exception as e:
        messagebox.showerror("MongoDB connection error", str(e))

    def feedSubmit():
        feedback = userExp.get()
        complaints = msgBox.get("1.0", END)
        fullName = fnameEntry.get()
        emailID = emailEntry.get()
        try:
            appRating = rating
        except:
            pass
        
        feedbackData = {'Full Name': fullName, 
                        'Email': emailID,
                        'Complaints': complaints,
                        'Feedback': feedback,
                        'Ratings': appRating
                            }
        
        try:
            feedCollection.insert_one(feedbackData)

            messagebox.showinfo("Thank you for the feedback!")

        except Exception as e:
            messagebox.showerror("Connection error!", str(e))


    fnameLabel = Label(feedbackLabel, text="Full Name*", font=("League Spartan", 15), bg="#FFFACD")
    fnameLabel.place(x=118, y=34)

    fnameEntry = Entry(feedbackLabel, width=17, border=0, bg="#FFFACD", font=("Tahoma", 12), justify=LEFT)
    fnameEntry.place(x=122, y=73, height=29)

    def importData():
        football_client = MongoClient('mongodb://localhost:27017/')
        football_database = football_client['football_database']
        football_collection = football_database['users']


    importName = Button(feedbackLabel,text = "Import \nfrom your\n profile", image = iconImport, compound = BOTTOM, border = 0, bg = "#FFFACD", font = ("Tahoma", 10), fg = "#545454", command = importData)
    importName.place(x = 336, y = 58)

    emailLabel = Label(feedbackLabel, text="Email ID*", font=("League Spartan", 15), bg="#FFFACD")
    emailLabel.place(x=118, y=113)

    complaintLabel = Label(feedbackLabel, text="Any Complaints*", font=("League Spartan", 15), bg="#FFFACD")
    complaintLabel.place(x=118, y=218)

    emailEntry = Entry(feedbackLabel, width=30, border=0, bg="#FFFACD", font=("Tahoma", 12), justify=LEFT)
    emailEntry.place(x=122, y=152, height=29)

    msgBox = Text(feedbackLabel, width = 32, height = 5, border = 0, bg = "#FFFACD", font = ("Tahoma", 12))
    msgBox.place(x = 118, y = 274)

    contactText = Label(feedbackLabel, text = "CONTACT US", font = ("League Spartan Semibold", 18), fg = "blue", bg = "#FFFACD")
    contactText.place(x = 484, y = 24)

    helpText = Label(feedbackLabel, text = "How can we help?", fg = "#000", bg = "#FFFACD", font = ("League Spartan Semibold", 16))
    helpText.place(x = 484, y = 62)

    descriptionText = Label(feedbackLabel, text = "To learn more about A-Divison\nFootball League, please fill out the\ncontact form and a member\nof our team will be in touch soon.", fg = "#000", bg = "#FFFACD", font = ("Tahoma", 12), justify = LEFT)
    descriptionText.place(x = 484, y = 100)

    rateText = Label(feedbackLabel, text = "Rate Us •", font = ("League Spartan Medium", 14), bg = "#FFFACD")
    rateText.place(x = 484, y = 196)

    rateAddon = Label(feedbackLabel, text = "Tell others what you think", bg = "#FFFACD", font = ("Tahoma", 12), fg = "#545454")
    rateAddon.place(x = 484, y = 230)

    def on_focus(e = None):
        userExp.delete(0, END)
    def out_focus(e = None):
        userExp.get()

    userExp = Entry(feedbackLabel, width = 30, border = 0, bg = "#FFFACD", fg = "#545454", font = ("Tahoma", 12), justify = CENTER)
    userExp.place(x = 498, y = 324, height = 30)

    userExp.insert(0, "Describe your experience (optional)")

    userExp.bind("<FocusIn>", on_focus)
    userExp.bind("<FocusOut>", out_focus)

    def on_star_enter(event):
        star = event.widget
        index = stars.index(star) + 1
        for i, s in enumerate(stars):
            if i < index:
                s.config(text='\u2605', fg='orange')
            else:
                s.config(text='\u2606')

    def on_star_leave(event):
        for i, s in enumerate(stars):
            try:
                if i >= rating:
                    s.config(text='\u2606', fg='orange')
                else:
                    s.config(text='\u2605', fg='orange')
            except:
                pass


    def on_star_click(event):
        star = event.widget
        global rating
        rating = stars.index(star) + 1
        for i, star in enumerate(stars):
            try:
                if i < rating:
                    star.config(text='\u2605', fg='orange')
                else:
                    star.config(text='\u2606')
                if rating_callback:
                    rating_callback(rating)
            except:
                pass 

    def handle_rating(rating):
        return rating

    feedback_frame = Frame(feedbackLabel, bg="#FFFACD")
    feedback_frame.place(x=482, y=260)

    stars = []
    rating_callback = handle_rating

    for i in range(5):
        star = Label(feedback_frame, text='\u2606', font=('Arial', 24), fg='orange', bg = "#FFFACD")
        star.bind('<Enter>', on_star_enter)
        star.bind('<Leave>', on_star_leave)
        star.bind('<Button-1>', on_star_click)
        star.pack(side=LEFT, padx=2)
        stars.append(star)

    
    verticalLine = Frame(frameFeedback, width = 2, height = 420, bg = "#545454")
    verticalLine.place(x = 750, y = 172)

    otherRatingsFrame = Frame(frameFeedback, width = 310, bg = "#FFFACD", height = 512)
    otherRatingsFrame.place(x = 754, y = 128)

    othersRatingText = Label(otherRatingsFrame, text = "WHAT OTHER SAYS?", font = ("League Spartan Semibold", 16), fg = "#f0710a", bg = "#FFFACD")
    othersRatingText.place(x = 8, y = 2)

    otherFeedsLabel = Label(otherRatingsFrame, image = imagefeedbackUser, bg = "#FFFACD")
    otherFeedsLabel.place(x = 8, y = 50)

    textSaugat = Label(otherFeedsLabel, text = "Saugat Shahi", font = ("Tahoma", 10), bg = "#FFFACD")
    textSaugat.place(x = 20, y = -5)

    submitButton = Button(feedbackLabel, text = "Submit ", bg = "#FFFACD", border = 0, image = iconSubmit, compound = RIGHT, font = ("Tahoma", 12), command = feedSubmit)
    submitButton.place(x = 602, y = 388)


    '''
    Create the application GUI and display the home section by default.
    '''
app = Tk()
app.geometry("1350x700")
app.config(bg="Black")
app.state("zoomed")
app.resizable(False, False)
app.title("Dashboard")

feedbackImage = Image.open("C:Images\\feedBox.png")
ImageFeedback = ImageTk.PhotoImage(feedbackImage)

groundImage = Image.open("C:Images\\ground.png")
imageGround = ImageTk.PhotoImage(groundImage)

logoImage = Image.open("C:Images\\logonp.png")
resizedLogo = logoImage.resize((160, 160))
imageLogo = ImageTk.PhotoImage(resizedLogo)

homeIcon = Image.open("C:Images\\home.png")
iconHome = ImageTk.PhotoImage(homeIcon)

liveIcon = Image.open("C:Images\\live.png")
iconLive= ImageTk.PhotoImage(liveIcon)

overviewIcon = Image.open("C:Images\\overview.png")
iconOverview = ImageTk.PhotoImage(overviewIcon)

matchIcon = Image.open("C:Images\\match.png")
iconMatch = ImageTk.PhotoImage(matchIcon)

standingsIcon = Image.open("C:Images\\standings.png")
iconStandings = ImageTk.PhotoImage(standingsIcon)

personalizeIcon = Image.open("C:Images\\personalize.png")
iconPersonalize = ImageTk.PhotoImage(personalizeIcon)

feedbackIcon = Image.open("C:Images\\feedbackIcon.png")
iconFeedback = ImageTk.PhotoImage(feedbackIcon)

rightIcon = Image.open("C:Images\\right.png")
iconRight = ImageTk.PhotoImage(rightIcon)

importIcon = Image.open("C:Images\\importIcon.png")
iconImport = ImageTk.PhotoImage(importIcon)

submitIcon = Image.open("C:Images\\next.png")
iconSubmit = ImageTk.PhotoImage(submitIcon)

userFeedbackImage = Image.open("C:Images\\otherFeeds.png")
imagefeedbackUser = ImageTk.PhotoImage(userFeedbackImage)

# Styling the speparator
style = ttk.Style()
style.configure("Separator.TSeparator", background="black")

#Creating the frames
leftFrame = Frame(app, width=300, height=700, bg="#FFFACD", border=1)
leftFrame.place(x=-4, y=0)
rightFrame = Frame(app, width=1070, height=700, bg="#FFFACD", border=1)
rightFrame.place(x=298, y=0)
lowerFrame = Frame(app, width=1366, height=46, bg="#FFFACD")
lowerFrame.place(x=0, y=702)

# GUI elements in th left frame

frame_home =Frame(rightFrame,width=1070, height=668, bg="#FFFACD", border=1)
frame_home.place(x=0,y=0)

def playlive():
    webbrowser.open("https://www.youtube.com/live/O2ANLnuEBmg")
frame_signup_back = Frame(frame_home, width = 540, bg = "#FFFACD", height = 180, highlightthickness = 1, relief = GROOVE, border= 4, highlightcolor="red")
frame_signup_back.place(x = 120, y = 110)
logoLabel = Label(frame_signup_back, image = imageLogo, bg = "#FFFACD")
logoLabel.place(x = 350, y = 10)

def facebook(e = None):
    webbrowser.open("https://www.facebook.com/Saugat Shahi Thakuri")
    facebook_button.config(fg = "#000000")
    facebook_button.config(bg = "#FFFACD")

def facebook_leave(e = None):
    facebook_button.config(fg = "blue")
    facebook_button.config(bg = "#FFFACD")

facebook_button = Button(frame_signup_back, image = iconRight, compound = RIGHT, bg = "#FFFACD",text="Connect with facebook  ", border = 0, font = ("Yu Gothic UI Semibold", 10, "bold"), command = facebook, fg = "blue")
facebook_button.place(x = 32, y = 86)
facebook_button.bind("<Button-1>", facebook)
facebook_button.bind("<Leave>", facebook_leave)

signup_frame_text = Label(frame_signup_back, text = "Your Favorite Teams in one place", font = ("League Spartan Thin SemiBold", 14), bg = "#FFFACD", fg = "#000000")
signup_frame_text.place(x = 30, y = 36)

live_match1_frame = Frame(frame_home, width = 244, height = 314)
live_match1_frame.place(x = 130, y = 320)

live_match2_frame = Frame(frame_home, width = 244, height = 314)
live_match2_frame.place(x = 406, y = 320)

live_ground_frame = Frame(frame_home, width = 232, height = 330, border = 2)
live_ground_frame.place(x = 740, y = 114)
groundLabel = Label(live_ground_frame, image = imageGround, relief = SOLID)
groundLabel.pack()

scores_frame = Frame(frame_home, width = 230, height = 100)
scores_frame.place(x = 740, y = 474)

label_live_match = Label(frame_home, text = "Streaming", font = ("Yu Gothic UI Semibold", 10), bg = "#FFFACD", fg = "black")
label_live_match.place(x = 754, y = 84)

watch_live = Button(frame_home, text = "LIVE", bg = "#FFFACD", border = 0, width = 5, height = 0, command = playlive, font = ("Yu Gothic UI Semibold", 10), fg = "red")
watch_live.place(x = 908, y = 84) 

label_home = Label(frame_home,text="Home",font=('League Spartan Medium', '17', 'bold'),bg='#FFFACD')
label_home.place(x=10,y=10)
separator = Frame(frame_home, width = 1070, height = 2, bg = "#000")
separator.place(x = 0, y = 64)

# Placing the separator line
separator = Frame(leftFrame, width = 80, height = 2, bg = "#000")
separator.place(x = 0, y = 64)

homeButton = Button(leftFrame, text = "   Home", border = 0, cursor = "hand2", width = 408, image = iconHome, compound = LEFT, height = 0, font = ("League Spartan", 14), bg = "#FFFACD", justify = LEFT, fg = "red", command = home_section)
homeButton.place(x = -108, y = 209)

liveButton = Button(leftFrame, text = "   Live", border = 0, compound = LEFT, width = 416, cursor = "hand2", image = iconLive, height = 0, font = ("League Spartan", 14), bg = "#FFFACD", justify = LEFT, command = live_section)
liveButton.place(x = -118, y = 282)

overviewButton = Button(leftFrame, text = "   Overview", cursor = "hand2", image = iconOverview, compound = LEFT, border = 0, width = 372, height = 0, font = ("League Spartan", 14), bg = "#FFFACD", justify = LEFT, command = overview_section)
overviewButton.place(x = -76, y = 348)

matchButton = Button(leftFrame, text = "   Matches", border = 0, cursor = "hand2", width = 390, image = iconMatch, compound = LEFT, height = 0, font = ("League Spartan", 14), bg = "#FFFACD", justify = LEFT, command = matches_section)
matchButton.place(x = -90, y = 414)

standingsButton = Button(leftFrame, text = "   Standings", cursor = "hand2", image = iconStandings, compound=LEFT, border = 0, width = 390, height = 0, font = ("League Spartan", 14), bg = "#FFFACD", justify = LEFT, command = standing_section)
standingsButton.place(x = -85, y = 480)

personalizeButton = Button(leftFrame, text = "   Personalization", cursor = "hand2", border = 0, image = iconPersonalize, compound = LEFT, width = 326, height = 0, font = ("League Spartan", 14), bg = "#FFFACD", justify = LEFT, command = personalization_section)
personalizeButton.place(x = -32, y = 546)

feedbackButton = Button(leftFrame, text = "   Feedback & Support", cursor = "hand2", image = iconFeedback, compound = LEFT, border = 0, width = 300, height = 0, font = ("League Spartan", 14), bg = "#FFFACD", justify = LEFT, command = feedback_section)
feedbackButton.place(x = 0, y = 612)

home_section()
app.mainloop()
