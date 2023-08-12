# Importing all the required libraries
from tkinter import *
from tkinter import ttk,messagebox,Label, PhotoImage, filedialog
from PIL import Image, ImageTk, ImageDraw
from pymongo import MongoClient
from base64 import *
import io,webbrowser
import pandas as pd
from io import BytesIO
import hashlib, re
from ButtonCreation import *
from ImageModule import *
from datetime import *

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
    frame_home =Frame(rightFrame,width=1070, height=668, bg="#f2f2f2", border=1)
    frame_home.place(x=0,y=0)

    def playlive():
        webbrowser.open("https://www.youtube.com/live/O2ANLnuEBmg")

    frame_signup_back = Label(frame_home,image = frameBackImage, bg = "#f2f2f2")
    frame_signup_back.place(x = 120, y = 110)

    logoLabel = Label(frame_signup_back, image = imageLogo, bg = "#FFF")
    logoLabel.place(x = 376, y = 26)

    signup_frame_text = Label(frame_signup_back, text = "Your favorite teams in one place", font = ("Nunito", 14, 'bold'), bg = "#FFF", fg = "#000000")
    signup_frame_text.place(x = 36, y = 58)

    connectFacebook = Label(frame_signup_back, text = "Connect with facebook ", image = iconRight, cursor = "hand2", compound = RIGHT, bg = "#FFF", fg = "blue", font = ("Nunito", 12))
    connectFacebook.place(x = 36, y = 94)

    smallHRule = Frame(frame_signup_back, width = 2, height = 72, bg = "#777070")
    smallHRule.place(x = 354, y = 58)

    live_match1_frame = Label(frame_home, image = live1BackImage, bg = "#f2f2f2")
    live_match1_frame.place(x = 120, y = 332)

    live_match2_frame = Label(frame_home, image = live2BackImage, bg = "#f2f2f2")
    live_match2_frame.place(x = 412, y = 332)

    live_ground_frame = Frame(frame_home, width = 232, height = 330, border = 0, relief = RAISED)
    live_ground_frame.place(x = 740, y = 114)
    groundLabel = Label(live_ground_frame, image = imageGround, bg = "#f2f2f2", border = 0)
    groundLabel.pack()

    scores_frame = Label(frame_home, image = scoresImage, bg = "#f2f2f2")
    scores_frame.place(x = 740, y = 474)

    smallVRule = Frame(scores_frame, width = 176, height = 2, bg = "#777070")
    smallVRule.place(x = 24, y = 60)

    hRule = Frame(scores_frame, width = 2, height = 72, bg = "#777070")
    hRule.place(x = 128, y = 80)
    
    def summaryView():
        hoverFrame.place(x=2, y=352)
        overview_section()
    summaryButton = Button(scores_frame, text = "Summary", bg = "#FFF", fg = "red", border = 0, font = ("League Spartan", 14), cursor = "hand2", command = summaryView)
    summaryButton.place(x = 16, y = 12)
    
    def matchInfo():
        hoverFrame.place(x=2, y=418)
        matches_section()

    matchInfoButton = Button(scores_frame, text = "Match Info", bg = "#FFF", fg = "red", border = 0, font = ("League Spartan", 14), cursor = "hand2", command = matchInfo)
    matchInfoButton.place(x = 116, y = 13)

    label_live_match = Label(frame_home, text = "Streaming", font = ("Yu Gothic UI Semibold", 10), bg = "#f2f2f2", fg = "black")
    label_live_match.place(x = 754, y = 84)

    watch_live = Button(frame_home, text = "LIVE", bg = "#f2f2f2", border = 0, width = 5, cursor = "hand2", height = 0, command = playlive, font = ("Yu Gothic UI Semibold", 10), fg = "red")
    watch_live.place(x = 908, y = 84)
    homeButton.config(fg="red", bg = "#f2f2f2")
    liveButton.config(fg = "black")
    matchButton.config(fg = "black")
    overviewButton.config(fg = "black")
    standingsButton.config(fg = "black")
    personalizeButton.config(fg = "black")
    feedbackButton.config(fg = "black") 

    label_home = Label(frame_home,text="HOME •",font=('Nunito', '14', 'bold'),bg='#f2f2f2')
    label_home.place(x=20,y=16) 
    
    separator = Frame(frame_home, width = 1070, height = 2, bg = "#000")
    separator.place(x = 0, y = 64)
    try:
        username_text = user_data['fullName']
        username_text_label = Label(app, font=('Nunito', 12, "bold"), bg="#FFF", fg = "#545454", wraplength = 120, justify= LEFT)
        username_text_label.config(text=username_text)
        username_text_label.place(x=138,y=64)
    except:
        pass

    date_label = Label(leftFrame,text="Date: "+str(date.today()),font=('Nunito', 12, "bold"), bg = '#f2f2f2')
    date_label.place(x=30,y=6)

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

    frame_live = Frame(rightFrame, width=1070, height=668, bg="#f2f2f2", border=1)
    frame_live.place(x=0, y=0)
    label_live = Label(frame_live, text="LIVE •", font=('Nunito', '14', 'bold'), bg='#f2f2f2')
    label_live.place(x=20, y=16)
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
    column_widths = [40, 40, 5, 50, 20, 50, 300]  # Add more widths for additional columns
    # Create a custom style for the treeview
    style = ttk.Style()
    style.configure('Custom.Treeview', font=('Arial', 12), background='#f2f2f2', foreground='black')  # Set the font and colors for the table
    style.configure('Custom.Treeview.Heading', font=('Arial', 12, 'bold'),background='#f2f2f2')
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
    frame_overview =Frame(rightFrame,width=1070, height=668, bg="#f2f2f2", border=1)
    frame_overview.place(x=0,y=0)
    frame_overview.place(x=0,y=0)
    label_overview = Label(frame_overview,text="OVERVIEW •",font=('Nunito', '14', 'bold'),bg='#f2f2f2')
    label_overview.place(x=20,y=16)
    separator = Frame(frame_overview, width = 1070, height = 2, bg = "#000")
    separator.place(x = 0, y = 64)

    def overviewTeamGUI():

        clubframe = Label(frame_overview, image = imageClubList1, bg = "#f2f2f2")

        def on_enter_club1(e):
            clubframe.place(x=e.widget.winfo_x(), y=(e.widget.winfo_y()))  # placing the widget(button) just below the main button destination..
            clear_frame()
            playersName(clubframe, "1. Ananta Tamang (captain)", 20, 146)
            playersName(clubframe, "2. Kamal Shrestha", 20, 182)
            playersName(clubframe, "3. Arik Bista", 20, 218)
            playersName(clubframe, "4. Suvash Gurung", 20, 254)
            playersName(clubframe, "5. Ashish Chaudhary", 20, 290)
            clubframe.lift()
            Club1Name = Label(clubframe, text = "Church Boys United", font = ("Nunito", 12, "bold"),bg = "#FFF")
            Club1Name.place(x = 94, y = 26)
            Club1Estd = Label(clubframe, text = "Estd. 2009", font = ("Nunito", 10, "bold"),bg = "#FFF")
            Club1Estd.place(x = 94, y = 54)
            membersClub1 = Label(clubframe, text = "Current Squad. 26", font = ("Nunito", 10, "bold"),bg = "#FFF")
            membersClub1.place(x = 94, y = 76)
            logo1 = Label(clubframe, image = logoClub1, bg = "#FFF")
            logo1.place(x = 10, y = 6)
            hRULE = Frame(clubframe, width = 220, height = 3, bg = "#ff8e48")
            hRULE.place(x = 20, y = 118)

        def on_enter_club2(e):
            clubframe.place(x=e.widget.winfo_x(), y=(e.widget.winfo_y()))  # placing the widget(button) just below the main button destination..
            clear_frame()
            playersName(clubframe, "1. Sujal Shrestha (captain)", 20, 146)
            playersName(clubframe, "2. Devendra Tamang", 20, 182)
            playersName(clubframe, "3. Bishal Shrestha", 20, 218)
            playersName(clubframe, "4. Ranjit Dhimal", 20, 254)
            playersName(clubframe, "5. Sagar Thapa", 20, 290)
            clubframe.lift()
            Club2Name = Label(clubframe, text = "Machhindra FC", font = ("Nunito", 12, "bold"),bg = "#FFF")
            Club2Name.place(x = 102, y = 26)
            Club2Estd = Label(clubframe, text = "Estd. 1973", font = ("Nunito", 10, "bold"),bg = "#FFF")
            Club2Estd.place(x = 102, y = 54)
            membersClub2 = Label(clubframe, text = "Current Squad. 22", font = ("Nunito", 10, "bold"),bg = "#FFF")
            membersClub2.place(x = 102, y = 76)
            logo2 = Label(clubframe, image = logoClub2, bg = "#FFF")
            logo2.place(x = 10, y = 20)
            hRULE = Frame(clubframe, width = 220, height = 3, bg = "#ff8e48")
            hRULE.place(x = 20, y = 118)

        def on_enter_club3(e):

            clubframe.place(x=e.widget.winfo_x(), y=(e.widget.winfo_y()))  # placing the widget(button) just below the main button destination..
            clear_frame()
            playersName(clubframe, "1. Man Bahadur Tmg (captain)", 20, 146)
            playersName(clubframe, "2. Abhisek Baral", 20, 182)
            playersName(clubframe, "3. Mahendra Karki", 20, 218)
            playersName(clubframe, "4. Akash Budha Magar", 20, 254)
            playersName(clubframe, "5. Basanta Tamang", 20, 290)
            Club3Name = Label(clubframe, text = "Satdobato Youth FC", justify = LEFT, font = ("Nunito", 12, "bold"),bg = "#FFF")
            Club3Name.place(x = 88, y = 26)
            Club3Estd = Label(clubframe, text = "Estd. 1998", font = ("Nunito", 10, "bold"),bg = "#FFF")
            Club3Estd.place(x = 88, y = 54)
            membersClub3 = Label(clubframe, text = "Current Squad. 26", font = ("Nunito", 10, "bold"),bg = "#FFF")
            membersClub3.place(x = 88, y = 76)
            logo3 = Label(clubframe, image = logoClub3, bg = "#FFF")
            logo3.place(x = 10, y = 16)
            hRULE = Frame(clubframe, width = 220, height = 3, bg = "#ff8e48")
            hRULE.place(x = 20, y = 118)
            clubframe.lift()

   
        def on_enter_club4(e):

            clubframe.place(x=e.widget.winfo_x(), y=(e.widget.winfo_y()))  # placing the widget(button) just below the main button destination..
            clear_frame()
            playersName(clubframe, "1. Saroj Tamang", 20, 146)
            playersName(clubframe, "2. Ashok Thapa", 20, 182)
            playersName(clubframe, "3. Santosh Mahat", 20, 218)
            playersName(clubframe, "4. Nicolas Serge Song", 20, 254)
            playersName(clubframe, "5. Mohit Gurung", 20, 290)
            Club4Name = Label(clubframe, text = "New Road Team", justify = LEFT, font = ("Nunito", 12, "bold"),bg = "#FFF")
            Club4Name.place(x = 98, y = 26)
            Club4Estd = Label(clubframe, text = "Estd. 1934", font = ("Nunito", 10, "bold"),bg = "#FFF")
            Club4Estd.place(x = 98, y = 54)
            membersClub4 = Label(clubframe, text = "Current Squad. 27", font = ("Nunito", 10, "bold"),bg = "#FFF")
            membersClub4.place(x = 98, y = 76)
            logo4 = Label(clubframe, image = logoClub4, bg = "#FFF")
            logo4.place(x = 10, y = 16)
            hRULE = Frame(clubframe, width = 220, height = 3, bg = "#ff8e48")
            hRULE.place(x = 20, y = 118)
            
            clubframe.lift()
    
        def on_enter_club5(e):

            clubframe.place(x=e.widget.winfo_x(), y=(e.widget.winfo_y()))  # placing the widget(button) just below the main button destination..
            clear_frame()
            playersName(clubframe, "1. Simanta Thapa (captain)", 20, 146)
            playersName(clubframe, "2. Samiraj Thokar", 20, 182)
            playersName(clubframe, "3. Santosh Dahal", 20, 218)
            playersName(clubframe, "4. Anish Deula", 20, 254)
            playersName(clubframe, "5. Fode Fofana", 20, 290)
            Club5Name = Label(clubframe, text = "Jawalakhel YC.", justify = LEFT, font = ("Nunito", 12, "bold"),bg = "#FFF")
            Club5Name.place(x = 98, y = 26)
            Club5Estd = Label(clubframe, text = "Estd. 1972", font = ("Nunito", 10, "bold"),bg = "#FFF")
            Club5Estd.place(x = 98, y = 54)
            membersClub5 = Label(clubframe, text = "Current Squad. 23", font = ("Nunito", 10, "bold"),bg = "#FFF")
            membersClub5.place(x = 98, y = 76)
            logo5 = Label(clubframe, image = logoClub5, bg = "#FFF")
            logo5.place(x = 16, y = 16)
            hRULE = Frame(clubframe, width = 220, height = 3, bg = "#ff8e48")
            hRULE.place(x = 20, y = 118)
            clubframe.lift()
    
        def on_enter_club6(e):

            clubframe.place(x=e.widget.winfo_x(), y=(e.widget.winfo_y()))  # placing the widget(button) just below the main button destination..
            clear_frame()
            playersName(clubframe, "1. Bikram Lama (captain)", 20, 146)
            playersName(clubframe, "2. Ansumana Kromah", 20, 182)
            playersName(clubframe, "3. Yogesh Gurung", 20, 218)
            playersName(clubframe, "4. Dona Thapa  NEP", 20, 254)
            playersName(clubframe, "5. Nirajan Maharjan  NEP", 20, 290)
            Club6Name = Label(clubframe, text = "Three Star Club", justify = LEFT, font = ("Nunito", 12, "bold"),bg = "#FFF")
            Club6Name.place(x = 102, y = 26)
            Club6Estd = Label(clubframe, text = "Estd. 1974", font = ("Nunito", 10, "bold"),bg = "#FFF")
            Club6Estd.place(x = 102, y = 54)
            membersClub6 = Label(clubframe, text = "Current Squad. 26", font = ("Nunito", 10, "bold"),bg = "#FFF")
            membersClub6.place(x = 102, y = 76)
            logo6 = Label(clubframe, image = logoClub6, bg = "#FFF")
            logo6.place(x = 14, y = 22)
            hRULE = Frame(clubframe, width = 220, height = 3, bg = "#ff8e48")
            hRULE.place(x = 20, y = 118)
            clubframe.lift()
    

        def on_clubframe_leave(e): 
            clubframe.place_forget()

        def create_club_frames(frame, image, x, y, enter_callback):
            label = Label(frame, image = image, cursor = "hand2", bg = "#f2f2f2")
            label.place(x = x, y = y)
            label.bind("<Enter>", enter_callback)
            clubframe.bind("<Leave>", on_clubframe_leave)
            return label
    
        def playersName(frame, text, x, y):
            playerName = Label(frame, text=text, font=("Tahoma", 12), border=0, cursor="hand2", bg="#FFF")
            playerName.place(x=x, y=y)
            return playerName


        def clear_frame():
            for widget in clubframe.winfo_children():
                widget.destroy()

        labels = []
        labels.append(create_club_frames(frame_overview, imageClub1, 52 , 100, on_enter_club1))
        labels.append(create_club_frames(frame_overview, imageClub1, 398 , 100, on_enter_club2))
        labels.append(create_club_frames(frame_overview, imageClub1, 744 , 100, on_enter_club3))
        labels.append(create_club_frames(frame_overview, imageClub1, 52 , 260, on_enter_club4))
        labels.append(create_club_frames(frame_overview, imageClub1, 398 , 260, on_enter_club5))
        labels.append(create_club_frames(frame_overview, imageClub1, 744 , 260, on_enter_club6))

        Club1Name = Label(labels[0], text = "Church Boys United", font = ("Nunito", 12, "bold"),bg = "#FFF")
        Club1Name.place(x = 94, y = 26)
        Club1Estd = Label(labels[0], text = "Estd. 2009", font = ("Nunito", 10, "bold"),bg = "#FFF")
        Club1Estd.place(x = 94, y = 54)
        membersClub1 = Label(labels[0], text = "Current Squad. 26", font = ("Nunito", 10, "bold"),bg = "#FFF")
        membersClub1.place(x = 94, y = 76)
        logo1 = Label(labels[0], image = logoClub1, bg = "#FFF")
        logo1.place(x = 10, y = 6)

        Club2Name = Label(labels[1], text = "Machhindra FC", font = ("Nunito", 12, "bold"),bg = "#FFF")
        Club2Name.place(x = 102, y = 26)
        Club2Estd = Label(labels[1], text = "Estd. 1973", font = ("Nunito", 10, "bold"),bg = "#FFF")
        Club2Estd.place(x = 102, y = 54)
        membersClub2 = Label(labels[1], text = "Current Squad. 22", font = ("Nunito", 10, "bold"),bg = "#FFF")
        membersClub2.place(x = 102, y = 76)
        logo2 = Label(labels[1], image = logoClub2, bg = "#FFF")
        logo2.place(x = 10, y = 20)

        Club3Name = Label(labels[2], text = "Satdobato Youth FC", justify = LEFT, font = ("Nunito", 12, "bold"),bg = "#FFF")
        Club3Name.place(x = 88, y = 26)
        Club3Estd = Label(labels[2], text = "Estd. 1998", font = ("Nunito", 10, "bold"),bg = "#FFF")
        Club3Estd.place(x = 88, y = 54)
        membersClub3 = Label(labels[2], text = "Current Squad. 26", font = ("Nunito", 10, "bold"),bg = "#FFF")
        membersClub3.place(x = 88, y = 76)
        logo3 = Label(labels[2], image = logoClub3, bg = "#FFF")
        logo3.place(x = 10, y = 16)

        Club4Name = Label(labels[3], text = "New Road Team", justify = LEFT, font = ("Nunito", 12, "bold"),bg = "#FFF")
        Club4Name.place(x = 98, y = 26)
        Club4Estd = Label(labels[3], text = "Estd. 1934", font = ("Nunito", 10, "bold"),bg = "#FFF")
        Club4Estd.place(x = 98, y = 54)
        membersClub4 = Label(labels[3], text = "Current Squad. 27", font = ("Nunito", 10, "bold"),bg = "#FFF")
        membersClub4.place(x = 98, y = 76)
        logo4 = Label(labels[3], image = logoClub4, bg = "#FFF")
        logo4.place(x = 10, y = 18)

        Club5Name = Label(labels[4], text = "Jawalakhel YC.", justify = LEFT, font = ("Nunito", 12, "bold"),bg = "#FFF")
        Club5Name.place(x = 98, y = 26)
        Club5Estd = Label(labels[4], text = "Estd. 1972", font = ("Nunito", 10, "bold"),bg = "#FFF")
        Club5Estd.place(x = 98, y = 54)
        membersClub5 = Label(labels[4], text = "Current Squad. 23", font = ("Nunito", 10, "bold"),bg = "#FFF")
        membersClub5.place(x = 98, y = 76)
        logo5 = Label(labels[4], image = logoClub5, bg = "#FFF")
        logo5.place(x = 16, y = 18)

        Club6Name = Label(labels[5], text = "Three Star Club", justify = LEFT, font = ("Nunito", 12, "bold"),bg = "#FFF")
        Club6Name.place(x = 102, y = 26)
        Club6Estd = Label(labels[5], text = "Estd. 1974", font = ("Nunito", 10, "bold"),bg = "#FFF")
        Club6Estd.place(x = 102, y = 54)
        membersClub6 = Label(labels[5], text = "Current Squad. 26", font = ("Nunito", 10, "bold"),bg = "#FFF")
        membersClub6.place(x = 102, y = 76)
        logo6 = Label(labels[5], image = logoClub6, bg = "#FFF")
        logo6 .place(x = 14, y = 22)

        def display_players_Club1(name):
            playersName = Label(clubframe, text = name, bg = "#FFF")
            playersName.place(x = 20, y = 40)

        
    overviewTeamGUI()
    
    def overview_selection(select):
        '''
        Display the overview based on the selection from the option.
        Args:
            select: The selected option from the OptionMenu widget.
        '''
        global team_search_entry
        if select==options[0]:
            overview_section()
            
        if select == options[1]:
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
                    image = image.resize((380,400))
                    # Convert the image to a Tkinter-compatible format
                    tk_image = ImageTk.PhotoImage(image)
                    # Create a Tkinter label and display the image
                    image_label = Label(frame_player, image = tk_image, bg = "#f2f2f2")
                    image_label.image = tk_image
                    image_label.place(x = 0,y = 68)

                    def details_label(frame_player,players_text,x,y):
                        '''
                        Create and place a label of player's details.

                        Args:
                            frame_player: The parent frame to place the label.
                            players_text: The text to display in label.
                            x: x-coordinate of the label's position.
                            y: y-coordinate of the label's position.

                        '''
                        label_details = Label(frame_player,text=players_text,font=('Tahoma', '12'),bg="#f2f2f2")
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
                    label_the_details.append(details_label(frame_player,"Position:",350,270))
                    label_the_details.append(details_label(frame_player,player_data['position'],480,270))
                    label_the_details.append(details_label(frame_player,"Number:",350,300))
                    label_the_details.append(details_label(frame_player,player_data['number'],480,300))
                    label_the_details.append(details_label(frame_player,player_data['Age'],80,520))
                    label_the_details.append(details_label(frame_player,player_data['Height'],172,520))
                    label_the_details.append(details_label(frame_player,player_data['Weight'],260,520))



                    
                    PositionNumberLabel = Label(frame_player, text = player_data['number'], font = ("Oswald", 52, 'bold'), fg = "#545454", bg = "#f2f2f2")
                    PositionNumberLabel.place(x = 40, y = 160)
                    seasonText = Label(frame_player, text = "PLAYER'S DATA", font = ("League Spartan", 14, "bold"), bg = "#f2f2f2", fg = "#545454")
                    seasonText.place(x = 346, y = 94)

                    positionText = Label(frame_player, text = "PLAYING POSITIONS", font = ("League Spartan", 14, "bold"), bg = "#f2f2f2", fg = "#545454")
                    positionText.place(x = 724, y = 72)

                    playerPosition = Label(frame_player, image = playerposImage, bg = "#f2f2f2")
                    playerPosition.place(x = 720, y = 110)

                    playerweightLabel = Label(frame_player, text = "YR", font = ("Oswald", 10, "bold"), bg = "#f2f2f2", fg = "#545454")
                    playerweightLabel.place(x = 80, y = 548)

                    playerageLabel = Label(frame_player, text = "CM", font = ("Oswald", 10, "bold"), bg = "#f2f2f2", fg = "#545454")
                    playerageLabel.place(x = 172, y = 548)

                    playerheightLabel = Label(frame_player, text = "WEIGHT", font = ("Oswald", 10, "bold"), bg = "#f2f2f2", fg = "#545454")
                    playerheightLabel.place(x = 260, y = 548)

                except Exception as e:
                    messagebox.showinfo('Message','Player not found'+ str(e))


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

            frame_player = Frame(frame_overview,bg="#f2f2f2",height = 600,width = 1050)
            frame_player.place(x = 0,y = 70)

            playerSearchLabel = Label(frame_overview, image = entrySearch, border = 0, bg = "#f2f2f2")
            playerSearchLabel.image = entrySearch
            playerSearchLabel.place(x = 30, y = 92)

            player_search_entry = Entry(playerSearchLabel,font=('Tahoma', 12), border = 0, bg = "#f2f2f2")
            player_search_entry.place(x = 18,y = 8)

            player_search_entry.insert(0,"Player's name")
            player_search_entry.bind('<FocusIn>',on_entry_click_1)
            player_search_entry.bind('<FocusOut>',on_focus_out_1)

            player_search_button = Button(playerSearchLabel, image = buttonSearch, border = 0,bg="#f2f2f2",command=player_search)
            player_search_button.image_names = buttonSearch
            player_search_button.place(x=206,y=6)

            app.bind('<Return>',lambda e: player_search())
  
    options = ["Team", "Player"]
    selected_option = StringVar(frame_overview)
    selected_option.set("Team")  # Set the default selected option
    option_menu = OptionMenu(frame_overview, selected_option, *options, command=overview_selection)
    option_menu.place(x=890,y=15)
    option_menu.config(font=('Tahoma', '10'), justify = LEFT ,width=16,bg="#f2f2f2")

    try:
        frameFeedback.destroy()
    except NameError:
        pass
    try:
        def open():
            import FootBot
    except Exception as e:
        messagebox.showerror("FOOTBOT", "FootBot is currently out of service!")

    buttonChat = Button(frame_overview, text = "Open FootBot", command=open)
    buttonChat.place(x = 400, y = 600)

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

    frame_matches =Frame(rightFrame,width=1070, height=668, bg="#f2f2f2", border=1)
    frame_matches.place(x=0,y=0)
    label_matches = Label(frame_matches,text="MACTHES •",font=('Nunito', '14', 'bold'),bg='#f2f2f2')
    label_matches.place(x=20,y=16)
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
    column_widths = [46,46,10,200,10,10,10,200]  # Add more widths for additional columns
    # Create a custom style for the treeview
    style = ttk.Style()
    style.configure('Custom.Treeview', font=('Arial', 12), background='#f2f2f2', foreground='black')  # Set the font and colors for the table
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

    frame_standings = Frame(rightFrame, width=1070, height=668, bg="#f2f2f2", border=1)
    frame_standings.place(x=0, y=0)
    label_standings = Label(frame_standings, text="STANDINGS •", font=('Nunito', '14', 'bold'), bg='#f2f2f2')
    label_standings.place(x=20, y=16)
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
    style.configure('Custom.Treeview', font=('Arial', 12), background='#f2f2f2', foreground='black')  # Set the font and colors for the table

    style.configure('Custom.Treeview.Heading', font=('Arial', 12, 'bold'),background='#f2f2f2', foreground='black')

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
    frame_personalization = Frame(rightFrame, width=1070, height=668, bg="#f2f2f2", border=1)
    frame_personalization.place(x=0, y=0)

    label_personalization = Label(frame_personalization, text="PERSONALIZATION •", font=('Nunito', '14', 'bold'), bg='#f2f2f2')
    label_personalization.place(x=20, y=16)

    separator = Frame(frame_personalization, width = 1070, height = 2, bg = "#000")
    separator.place(x = 0, y = 64)

    def profile():
        global profilePersonalizeLabel
        '''
        Display the user's information.
        '''
        def back():
            '''
            Displays the personalozation section when back button is clicked.
            '''
            personalization_section()
        
        try:
            profile_picture1 = fetch_image_from_mongodb()
            pp = profile_picture1.resize((120, 120))
        except Exception as e:
            messagebox.showerror('error', e)

        profile_frame = Frame(rightFrame, width=1070, height=668, bg="#f2f2f2", border=1)
        profile_frame.place(x=0, y=0)

        entryLabel1 = Label(profile_frame, image = imageClub2, bg = '#f2f2f2')
        entryLabel1.place(x = 320, y = 180)

        entryLabel2 = Label(profile_frame, image = imageClub2, bg = '#f2f2f2')
        entryLabel2.place(x = 728, y = 180)
        
        entryBio = Label(profile_frame, image = imageClub3, bg = '#f2f2f2')
        entryBio.place(x = 320, y = 252)

        entryLabel3 = Label(profile_frame, image = imageClub2, bg = '#f2f2f2')
        entryLabel3.place(x = 320, y = 403)

        entryLabel4 = Label(profile_frame, image = imageClub2, bg = '#f2f2f2')
        entryLabel4.place(x = 728, y = 403)

        entryLabel5 = Label(profile_frame, image = imageClub2, bg = '#f2f2f2')
        entryLabel5.place(x = 320, y = 496)

        entryLabel6 = Label(profile_frame, image = imageClub2, bg = '#f2f2f2')
        entryLabel6.place(x = 728, y = 496)

        profilePersonalizeLabel = Label(profile_frame, bg = "#FFF")
        profilePersonalizeLabel.place(x=60,y=174)

        labelledFrame1 = Frame(profile_frame, width = 460, height = 2, bg = "#ff6100")
        labelledFrame1.place(x = 16, y = 132)

        labelledFrameText = Label(profile_frame, text = '  Compulsory Details  ', bg = '#f2f2f2', font = ('Tahoma', 13))
        labelledFrameText.place(x = 40, y = 118)

        labelledFrame2 = Frame(profile_frame, width = 460, height = 2, bg = "#ff6100")
        labelledFrame2.place(x = 16, y = 354)

        labelledFrameText1 = Label(profile_frame, text = '  Optional Details  ', bg = '#f2f2f2', font = ('Tahoma', 13))
        labelledFrameText1.place(x = 44, y = 340)


        photo1 = ImageTk.PhotoImage(pp)
        profilePersonalizeLabel.config(image=photo1, background="#f2f2f2")
        profilePersonalizeLabel.image = photo1

        label_profile = Label(profile_frame, text="User Profile", font=('Nunito', '14', 'bold'), bg="#f2f2f2")
        label_profile.place(x=10, y=10)

        separator = Frame(profile_frame, width = 1070, height = 2, bg = "#000")
        separator.place(x = 0, y = 64)

        full_name_label = Label(profile_frame, text="Full Name:", font=('Tahoma', '12'), bg="#f2f2f2")
        full_name_label.place(x=230, y=187)
       
        profileName = Entry(entryLabel1, font=('Tahoma', '12'), width=21, border = 0, bg="#f2f2f2")
        profileName.place(x=12, y=7)

        phone_num_label = Label(profile_frame, text="Phone Number:", font=('Tahoma', '12'), bg="#f2f2f2")
        phone_num_label.place(x=600, y=187)

        phoneNumEntry = Entry(entryLabel2, font=('Tahoma', '12'), width=21, border = 0, bg="#f2f2f2")
        phoneNumEntry.place(x=12, y=7)

        emailLabels = Label(profile_frame, text="Email ID:", font=('Tahoma', '12'), bg="#f2f2f2")
        emailLabels.place(x=240, y=412)

        emailEntry = Entry(entryLabel3, font=('Tahoma', '12'), width=21, border = 0, bg="#f2f2f2")
        emailEntry.place(x=12, y=7)

        addressLabel = Label(profile_frame, text="Address:", font=('Tahoma', '12'), bg="#f2f2f2")
        addressLabel.place(x=648, y=412)

        addressEntry = Entry(entryLabel4, font=('Tahoma', '12'), width=21, border = 0, bg="#f2f2f2")
        addressEntry.place(x=12, y=7)

        countryLabel = Label(profile_frame, text="Country:", font=('Tahoma', '12'), bg="#f2f2f2")
        countryLabel.place(x=240, y=506)

        countryEntry = Entry(entryLabel5, font=('Tahoma', '12'), width=21, border = 0, bg="#f2f2f2")
        countryEntry.place(x=12, y=7)

        nationalityLabel = Label(profile_frame, text="Nationality:", font=('Tahoma', '12'), bg="#f2f2f2")
        nationalityLabel.place(x=634, y=506)

        nationalityEntry = Entry(entryLabel6, font=('Tahoma', '12'), width=21, border = 0, bg="#f2f2f2")
        nationalityEntry.place(x=12, y=7)

        bioEntry = Entry(entryBio, font=('Tahoma', '12'), width=66, border = 0, bg="#f2f2f2")
        bioEntry.place(x=14, y=9, height = 30)

        bioEntryLabel = Label(profile_frame, text="Bio:", font=('Tahoma', '12'), bg="#f2f2f2")
        bioEntryLabel.place(x=248, y=264)


        back_button = Button(profile_frame,text="Back",font=('Tahoma', '12'),width = 7, bg="#f2f2f2",cursor = "hand2",command=back)
        back_button.place(x=960, y=88, height = 26)

        def enable_entry():
            '''
            Enable the entry fields for editing and disable the update button.
            '''
            global cancelButton, save_button
            profileName.config(state = NORMAL)
            phoneNumEntry.config(state = NORMAL)
            bioEntry.config(state = NORMAL)
            emailEntry.config(state = NORMAL)
            addressEntry.config(state = NORMAL)
            countryEntry.config(state = NORMAL)
            nationalityEntry.config(state = NORMAL)
            update_button.config(state = NORMAL)
            update_button.place_forget()

            save_button = Button(profile_frame, image = imageSaveButton, cursor = "hand2", font=('League Spartan Medium', '12', 'bold'), bg="#f2f2f2",border = 0, command=save_profile)
            save_button.place(x=390, y=620)
            app.bind('<Return>',lambda e: save_profile())
            cancelButton = Button(profile_frame, image = imageDeleteButton, cursor = "hand2", bg="#f2f2f2", command=disable_entry, border = 0)
            cancelButton.place(x=570, y=620)

        def save_profile():
            '''
            Save the updated profile information to the database and disable the entry fields.
            '''
            try:
                new_full_name = profileName.get()
                new_phone_num = phoneNumEntry.get()
                

                football_collection.update_one({'password': user_data['password']}, 
                                               {'$set': {'fullName': new_full_name, 'phone': new_phone_num,
                                                         'bio':bioEntry.get(),'email':emailEntry.get(),
                                                         'address':addressEntry.get(),'country':countryEntry.get(),
                                                         'nationality':nationalityEntry.get()}})

                # Display a success message
                messagebox.showinfo("Profile Updated", "Your profile has been updated successfully.")

                # Disable the entry fields again
                profileName.config(state = DISABLED)
                phoneNumEntry.config(state = DISABLED)
                bioEntry.config(state = DISABLED)
                emailEntry.config(state = DISABLED)
                addressEntry.config(state = DISABLED)
                countryEntry.config(state = DISABLED)
                nationalityEntry.config(state = DISABLED)
                update_button.config(state = NORMAL)

            except:
                messagebox.showerror("System Error!", "Sorry for the inconvenience. We are working on it.")

        update_button = Button(profile_frame, image = imageEditButton, bg="#f2f2f2", cursor = "hand2", command=enable_entry, border = 0)
        update_button.place(x=390, y=620)

        def disable_entry():
            profileName.config(state = DISABLED)
            phoneNumEntry.config(state = DISABLED)
            cancelButton.place_forget()
            update_button = Button(profile_frame, image = imageEditButton, bg="#f2f2f2", cursor = "hand2", command=enable_entry, border = 0)
            update_button.place(x=390, y=620)

        profileName.insert(0, user_data['fullName'])
        profileName.config(state = DISABLED)

        phoneNumEntry.insert(0, phone)
        phoneNumEntry.config(state = DISABLED)
        try:
            bioEntry.insert(0,user_data['bio'])
            bioEntry.config(state=DISABLED)

            emailEntry.insert(0,user_data['email'])
            emailEntry.config(state=DISABLED)

            addressEntry.insert(0,user_data['address'])
            addressEntry.config(state=DISABLED)

            countryEntry.insert(0,user_data['country'])
            countryEntry.config(state=DISABLED)

            nationalityEntry.insert(0,user_data['nationality'])
            nationalityEntry.config(state=DISABLED)
        except:
            pass

    def log_out():

        confirm = messagebox.askyesno('Logout', 'Are you sure you want to logout?')
        if confirm:
            app.destroy()
            import Login
        else:
            pass
    
    def change():
        def confirm_change():
            try:
                if user_data['password'] == hashlib.sha256(currentPwdEntry.get().encode()).hexdigest():
                    if newPwdEntry.get() == '' or rePwdEntry.get() == '':
                        messagebox.showinfo('Password Change', 'No fields can be empty.')
                    elif currentPwdEntry.get() == newPwdEntry.get():
                        messagebox.showinfo('Validation Error', "You can't keep your new password same as the previous.")
                    elif len(newPwdEntry.get())<7 or not re.search('[A-Z]',newPwdEntry.get()) or not re.search('[0-9]',newPwdEntry.get()) or not re.search('[!@#$%]',newPwdEntry.get()):
                        messagebox.showerror('Registration', 'Password must be at least 6 characters long and contain at least one uppercase letter, one number, and one special character (!@#$%^&*).')

                    elif newPwdEntry.get() == rePwdEntry.get():
                    # Update the password in the database
                        new_hash_psw = hashlib.sha256(newPwdEntry.get().encode()).hexdigest()
                        football_collection.update_one({'password': user_data['password']}, {'$set': {'password': new_hash_psw}})
                        messagebox.showinfo('Validataion Success', 'Password updated successfully.')
                        password_change_window.destroy()
                        messagebox.showinfo("Login Again", "Login with your new password!")
                        app.destroy()
                        import Login
                    else:
                        messagebox.showerror('Password Change', "Passwords don't match.")
                else:
                    messagebox.showerror('Change Declined', "Sorry, we can't verify that it's you.")
            except:
                messagebox.showerror('Account Error', 'Please login to your account')

        password_change_window = Toplevel(frame_personalization)
        password_change_window.title('Change your password')
    
    # Center the window on a screen with width 1366 and height 768
        window_width = 280
        window_height = 350
        screen_width = 1366
        screen_height = 768
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        password_change_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
        password_change_window.config(bg="#f2f2f2")
        
        pwdChangeLabel = Label(password_change_window, image = changePwd, bg = "#f2f2f2")
        pwdChangeLabel.place(x = 0, y = 0)

        current_password_label = Label(pwdChangeLabel, text='Current Password:', bg="#f2f2f2", font=('Tahoma', '12'))
        
        current_password_label.place(x=46, y=31)
        currentPwdEntry = Entry(pwdChangeLabel, font=('Tahoma', '12'), border = 0, bg = "#f2f2f2")
        currentPwdEntry.place(x=48, y=63)

        new_password_label = Label(pwdChangeLabel, text='Enter New Password:', bg="#f2f2f2", font=('Tahoma', '12'))
        new_password_label.place(x=46, y=100)
        newPwdEntry = Entry(pwdChangeLabel, font=('Tahoma', '12'), border = 0, bg = "#f2f2f2")
        newPwdEntry.place(x=48, y=133)

        re_password_label = Label(pwdChangeLabel, text='Re-enter New Password:', bg="#f2f2f2", font=('Tahoma', '12'))
        re_password_label.place(x=46, y=169)
        rePwdEntry = Entry(pwdChangeLabel, font=('Tahoma', '12'), border = 0, bg = "#f2f2f2")
        rePwdEntry.place(x=48, y=202)

        change_btn = Button(pwdChangeLabel, text='Change',width = 94, height = 24, border = 0, image = changePwdButton, compound = CENTER, bg="#f2f2f2", font=('Tahoma', '12'), command=confirm_change)
        change_btn.place(x=90, y=280)

        app.bind('<Return>',lambda e: confirm_change())

    def delete():
        '''
        Open the window for delete.
        '''
        delete_window = Toplevel(frame_personalization)
        delete_window.title('Delete Account')

        def delete_acc():
            '''
            Delete the user account.
            '''
            global deleteConfirmWindow
            account_delete = hashlib.sha256(deleteEntry.get().encode()).hexdigest()
            try:
                if account_delete == user_data['password']:
                    delete_window.destroy()
                    deleteConfirmWindow = Toplevel(frame_personalization)
                    deleteConfirmWindow.title("Confirm Deletion")
                    window_width = 320
                    window_height = 240
                    screen_width = 1366
                    screen_height = 768
                    x = (screen_width - window_width) // 2
                    y = (screen_height - window_height) // 2

                    deleteConfirmWindow.geometry(f"{window_width}x{window_height}+{x}+{y}")
         
                    deleteConfirmWindow.config(bg="#f2f2f2")

                    accDltImage = Label(deleteConfirmWindow, image = dltAccImage, border = 0, bg = "#f2f2f2")
                    accDltImage.place(x = 130, y = 30)

                    accDltWarn = Label(deleteConfirmWindow, text = "Are you sure, you want to delete your account?", wraplength = 180, font = ("Helvetica", 10, "bold"), bg = "#f2f2f2")
                    accDltWarn.place(x = 78, y = 108)

                    confirmed = Button(deleteConfirmWindow, width = 94, height = 24, image = buttonConDelete, compound = CENTER, border = 0, bg = "#f2f2f2", font = ("Arial", 10), fg = "#FFF", command = confirmDel)
                    confirmed.place(x = 38, y = 170)

                    keepacc = Button(deleteConfirmWindow, width = 94, height = 24, image = buttonCancelDlt, compound = CENTER, border = 0, bg = "#f2f2f2", font = ("Arial", 10), fg = "#FFF", command = stopDel)
                    keepacc.place(x = 180, y = 170)
                else:
                    messagebox.showerror("Failed","Sorry, We can't verify that the account belongs to you.")
            except Exception as e:
                messagebox.showerror("Account Error", "Account not found")
        try:
            def confirmDel():
                football_collection.delete_one({'password': user_data['password']})
                messagebox.showinfo("Deletion Success", "Your account has been deleted successfully.")
                app.destroy()
                import Login
        except Exception as e:
            messagebox.showerror("System Error", "We are working on it.")

        def stopDel():
            deleteConfirmWindow.destroy()
        window_width = 320
        window_height = 240
        screen_width = 1366
        screen_height = 768
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        delete_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
        delete_window.config(bg="#f2f2f2")

        delete_password_label = Label(delete_window, text="Verify that it's you!", bg="#f2f2f2", font=('Tahoma', '12'))
        delete_password_label.place(x=24, y=24)

        frameStyle = Frame(delete_window, height = 2, width = 220, bg = "red")
        frameStyle.place(x = 24, y = 56)

        dltEntryLabel = Label(delete_window, image = entryDlt, border = 0, bg = '#f2f2f2')
        dltEntryLabel.place(x = 24, y = 112)
        
        deleteEntry = Entry(dltEntryLabel, font=('Tahoma', '12'), width=24, border = 0, bg = "#f2f2f2")
        deleteEntry.place(x=12, y=6, height = 26)

        dltEntryText = Label(delete_window, text = "Enter Password: ", bg = "#f2f2f2", font= ("Tahoma", 12))
        dltEntryText.place(x = 32, y = 84)

        delete_btn = Button(delete_window, image = dltAccButton, width = 94, height = 24, compound = CENTER, bg="#f2f2f2", border = 0, fg = "#FFF", font=('Helvetica', '10', "bold"), command=delete_acc)
        delete_btn.image_names = dltAccButton
        delete_btn.place(x=108, y=184)

        delete_window.mainloop()


    personaliztion_button = []
    personaliztion_button.append(create_personalization_btns(frame_personalization,'C:Images\\profile.png', "Profile", 30, 100, profile))
    personaliztion_button.append(create_personalization_btns(frame_personalization, 'C:Images\\change.png', "Change Password", 30, 150, change))
    personaliztion_button.append(create_personalization_btns(frame_personalization, 'C:Images\\delete.png', "Delete Account", 30, 200, delete))
    personaliztion_button.append(create_personalization_btns(frame_personalization, 'C:Images\\logout.png', "Log Out", 30, 250, log_out))

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

    frameFeedback = Frame(rightFrame, width=1070, height=668, bg="#f2f2f2", border=1)
    frameFeedback.place(x=0, y=0)

    feedbackLabel = Label(frameFeedback, image=ImageFeedback, border=0)
    feedbackLabel.place(x=-60, y=102)

    labelFeedback = Label(frameFeedback, text="FEEDBACK & SUPPORT •", font=('Nunito', '14', 'bold'), bg='#f2f2f2')
    labelFeedback.place(x=20, y=16)

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
        phoneNumber = phoneEntry.get()
        try:
            if not None:
                appRating = rating
        except:
            pass
        
        feedbackData = {'Full Name': fullName, 
                        'Contact No': phoneNumber,
                        'Complaints': complaints,
                        'Feedback': feedback,
                        'Ratings': str(appRating) + "/ 5"
                            }
        
        
        try:
            feedCollection.insert_one(feedbackData)

            messagebox.showinfo("Feedback","Thank you for the feedback!")
            feedback_section()
            

        except Exception as e:
            messagebox.showerror("Connection error!", str(e))


    fnameLabel = Label(feedbackLabel, text="Full Name*", font=("League Spartan", 15), bg="#f2f2f2")
    fnameLabel.place(x=132, y=44, height = 30)

    fnameEntry = Entry(feedbackLabel, width=17, border=0, bg="#f2f2f2", font=("Tahoma", 12), justify=LEFT)
    fnameEntry.place(x=132, y=80, height=26)

    def importData():
        try:
            fnameEntry.insert(0, user_data['fullName'])
            fnameEntry.config(state = DISABLED, disabledbackground = "#f2f2f2", disabledforeground="#000")

            phoneEntry.insert(0, user_data['phone'])
            phoneEntry.config(state = DISABLED, disabledbackground = "#f2f2f2", disabledforeground="#000")
        except Exception as e:
            messagebox.showerror("Account error",'Please login and try again.')


    importName = Button(feedbackLabel,text = "Import Details  ", image = iconImport, compound = RIGHT, border = 0, bg = "#f2f2f2", font = ("Tahoma", 10), command = importData)
    importName.place(x = 310, y = 81)

    phoneLabel = Label(feedbackLabel, text="Contact No. *", font=("League Spartan", 15), bg="#f2f2f2")
    phoneLabel.place(x=132, y=122, height = 30)

    phoneEntry = Entry(feedbackLabel, width=30, border=0, bg="#f2f2f2", font=("Tahoma", 12), justify=LEFT)
    phoneEntry.place(x=132, y=158, height=26)

    complaintLabel = Label(feedbackLabel, text="Any Complaints*", font=("League Spartan", 15), bg="#f2f2f2")
    complaintLabel.place(x=132, y=234, height = 30)

    def on_enter(e):
    # Get the text from the Text widget
        message = msgBox.get("1.0", "end-1c")  # "1.0" means line 1, character 0. "end-1c" excludes the newline character at the end.
        character_count = len(message)
        if character_count >= 500:
            msgBox.config(state = DISABLED, bg = "#f2f2f2")
        else:
            msgBox.config(state = NORMAL, bg="#f2f2f2")
            labelcount.config(text = f"{character_count}/500")
    labelcount = Label(frameFeedback, text = "0/500", bg = "#f2f2f2", fg = "#545454")
    labelcount.place(x = 300, y = 344)

    msgBox = Text(feedbackLabel, width = 30, height = 5, border = 0, bg = "#f2f2f2", font = ("Tahoma", 12))
    msgBox.bind("<KeyRelease>", on_enter)
    msgBox.place(x = 132, y = 273)

    contactText = Label(feedbackLabel, text = "CONTACT US", font = ("League Spartan Semibold", 18), fg = "blue", bg = "#f2f2f2")
    contactText.place(x = 484, y = 24)

    helpText = Label(feedbackLabel, text = "How can we help?", fg = "#000", bg = "#f2f2f2", font = ("League Spartan Semibold", 16))
    helpText.place(x = 484, y = 62)

    descriptionText = Label(feedbackLabel, text = "To learn more about A-Divison\nFootball League, please fill out the\ncontact form and a member\nof our team will be in touch soon.", fg = "#000", bg = "#f2f2f2", font = ("Tahoma", 12), justify = LEFT)
    descriptionText.place(x = 484, y = 100)

    rateText = Label(feedbackLabel, text = "Rate Us •", font = ("League Spartan Medium", 14), bg = "#f2f2f2")
    rateText.place(x = 484, y = 192)

    rateAddon = Label(feedbackLabel, text = "Tell others what you think", bg = "#f2f2f2", font = ("Tahoma", 12), fg = "#545454")
    rateAddon.place(x = 484, y = 226)

    def on_focus(e = None):
        userExp.delete(0, END)
    def out_focus(e = None):
        userExp.get()

    userExp = Entry(feedbackLabel, width = 30, border = 0, bg = "#f2f2f2", fg = "#545454", font = ("Tahoma", 12), justify = CENTER)
    userExp.place(x = 495, y = 320, height = 30)

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
        global rating
        for i, s in enumerate(stars):
            try:
                if i >= rating:
                    s.config(text='\u2606', fg='orange')
                else:
                    s.config(text='\u2605', fg='orange')
            except:
                pass


    def on_star_click(event):
        global rating
        star = event.widget
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

    feedback_frame = Frame(feedbackLabel, bg="#f2f2f2")
    feedback_frame.place(x=482, y=254)

    stars = []
    rating_callback = handle_rating

    for i in range(5):
        star = Label(feedback_frame, text='\u2606', font=('Arial', 24), fg='orange', bg = "#f2f2f2")
        star.bind('<Enter>', on_star_enter)
        star.bind('<Leave>', on_star_leave)
        star.bind('<Button-1>', on_star_click)
        star.pack(side=LEFT, padx=2)
        stars.append(star)

    
    verticalLine = Frame(frameFeedback, width = 2, height = 420, bg = "#545454")
    verticalLine.place(x = 750, y = 172)

    otherRatingsFrame = Frame(frameFeedback, width = 310, bg = "#f2f2f2", height = 512)
    otherRatingsFrame.place(x = 754, y = 128)

    othersRatingText = Label(otherRatingsFrame, text = "WHAT OTHER SAYS?", font = ("League Spartan Semibold", 16), fg = "#f0710a", bg = "#f2f2f2")
    othersRatingText.place(x = 8, y = 10)

    otherFeedsLabel = Label(otherRatingsFrame, image = imagefeedbackUser, bg = "#f2f2f2")
    otherFeedsLabel.place(x = -2, y = 44)

    textSaugat = Label(otherFeedsLabel, text = "Saugat Shahi", font = ("Tahoma", 10), bg = "#f2f2f2")
    textSaugat.place(x = 24, y = 8)

    submitButton = Button(feedbackLabel, text = "Submit ", bg = "#f2f2f2", border = 0, image = iconSubmit, compound = RIGHT, font = ("Tahoma", 12), command = feedSubmit)
    submitButton.place(x = 598, y = 382)

    app.bind('<Return>',lambda e: feedSubmit())


    '''
    Create the application GUI and display the home section by default.
    '''
app = Tk()
app.geometry("1350x700")
app.config(bg="Black")
app.state("zoomed")
app.iconbitmap('Images\\football.ico')
app.resizable(False, False)
app.title("Dashboard")

feedbackImage = Image.open("C:Images\\feedBackOpt.png")
ImageFeedback = ImageTk.PhotoImage(feedbackImage)

groundImage = Image.open("C:Images\\ground.png")
imageGround = ImageTk.PhotoImage(groundImage)

logoImage = Image.open("C:Images\\logonp.png")
resizedLogo = logoImage.resize((120, 120))
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

userFeedbackImage = Image.open("C:Images\\otherFeedsOpt.png")
imagefeedbackUser = ImageTk.PhotoImage(userFeedbackImage)

imagePlayerpos = Image.open("C:Images\\playerPositionOpt.png")
resizePosimage = imagePlayerpos.resize((260, 150))
playerposImage = ImageTk.PhotoImage(resizePosimage)

searchentry = Image.open("C:Images\\searchEntryOpt.png")
resizeSearch = searchentry.resize((244, 38))
entrySearch = ImageTk.PhotoImage(resizeSearch)

searchButton = Image.open("C:Images\\searchButtonOpt.png")
resizeSearchButton = searchButton.resize((24, 24))
buttonSearch = ImageTk.PhotoImage(resizeSearchButton)

pwdChange = Image.open("C:Images\\pwdChange.png")
resizepwdChange = pwdChange.resize((280, 350))
changePwd = ImageTk.PhotoImage(resizepwdChange)

pwdChangeButton= Image.open("C:Images\\buttonChange.png")
resizepwdChangeButton= pwdChangeButton.resize((100, 50))
changePwdButton= ImageTk.PhotoImage(resizepwdChangeButton)

dltEntry= Image.open("C:Images\\dltEntry.png")
resizeEntry = dltEntry.resize((240, 40))
entryDlt = ImageTk.PhotoImage(resizeEntry)

accDltButton= Image.open("C:Images\\buttonDlt.png")
resizeaccDltButton= accDltButton.resize((78, 48))
dltAccButton= ImageTk.PhotoImage(resizeaccDltButton)

ConDeleteButton= Image.open("C:Images\\cDlt.png")
resizeConDeleteButton= ConDeleteButton.resize((70, 40))
buttonConDelete= ImageTk.PhotoImage(resizeConDeleteButton)

CancelDltButton= Image.open("C:Images\\cancelDlt.png")
resizeCancelDltButton= CancelDltButton.resize((70, 40))
buttonCancelDlt= ImageTk.PhotoImage(resizeCancelDltButton)

accDltImage= Image.open("C:Images\\deleteAcc.png")
resizeaccDltImage= accDltImage.resize((60, 60))
dltAccImage= ImageTk.PhotoImage(resizeaccDltImage)

frameBack= Image.open("C:Images\\frameBackOpt.png")
frameBackImage = ImageTk.PhotoImage(frameBack)

live1Back= Image.open("C:Images\\live12.png")
live1BackImage = ImageTk.PhotoImage(live1Back)

live2Back= Image.open("C:Images\\live22.png")
live2BackImage = ImageTk.PhotoImage(live2Back)

scores = Image.open("C:Images\\scoresOpt.png")
scoresImage = ImageTk.PhotoImage(scores)

Club1Logo = Image.open("C:Images\\club1Logo.png")
logoClub1 = ImageTk.PhotoImage(Club1Logo)

Club2Logo = Image.open("C:Images\\club2Logo.png")
logoClub2 = ImageTk.PhotoImage(Club2Logo)

Club3Logo = Image.open("C:Images\\club3Logo.jpg")
logoClub3 = ImageTk.PhotoImage(Club3Logo)

Club4Logo = Image.open("C:Images\\club4Logo.png")
logoClub4 = ImageTk.PhotoImage(Club4Logo)

Club5Logo = Image.open("C:Images\\club5Logo.png")
logoClub5 = ImageTk.PhotoImage(Club5Logo)

Club6Logo = Image.open("C:Images\\club6Logo.png")
logoClub6 = ImageTk.PhotoImage(Club6Logo)

userLabelImage = Image.open("C:Images\\userLabel.png")
resizeUserImage = userLabelImage.resize((240, 120))
imageUserLabel = ImageTk.PhotoImage(resizeUserImage)

editButtonImg = Image.open("C:Images\\editButton.png")
resizeEditImg = editButtonImg.resize((100, 30))
imageEditButton = ImageTk.PhotoImage(resizeEditImg)

saveButtonImg = Image.open("C:Images\\saveButton.png")
resizesaveImg = saveButtonImg.resize((100, 30))
imageSaveButton = ImageTk.PhotoImage(resizesaveImg)


DeleteButtonImg = Image.open("C:Images\\cancelButton.png")
resizeDeleteImg = DeleteButtonImg.resize((100, 30))
imageDeleteButton = ImageTk.PhotoImage(resizeDeleteImg)

userLabelImage1 = Image.open("C:Images\\highlightPos.png")
resizeUserImage1 = userLabelImage1.resize((240, 120))
imageUserLabel1 = ImageTk.PhotoImage(resizeUserImage1)

ClubImage1 = Image.open("C:Images\\Club1.png")
resizeClubImage1 = ClubImage1.resize((260, 120))
imageClub1 = ImageTk.PhotoImage(resizeClubImage1)


ClubImage2 = Image.open("C:Images\\Club2.png")
resizeClubImage2 = ClubImage2.resize((220, 40))
imageClub2 = ImageTk.PhotoImage(resizeClubImage2)

ClubImage3 = Image.open("C:Images\\Club3.png")
resizeClubImage3 = ClubImage3.resize((630, 44))
imageClub3 = ImageTk.PhotoImage(resizeClubImage3)

ClubListImage1 = Image.open("C:Images\\Club1List.png")
resizeClubListImage1 = ClubListImage1.resize((260, 360))
imageClubList1 = ImageTk.PhotoImage(resizeClubListImage1)

# Styling the speparator
style = ttk.Style()
style.configure("Separator.TSeparator", background="black")

#Creating the frames
leftFrame = Frame(app, width=300, height=700, bg="#f2f2f2", border=1)
leftFrame.place(x=-4, y=0)
rightFrame = Frame(app, width=1070, height=700, bg="#f2f2f2", border=1)
rightFrame.place(x=298, y=0)
lowerFrame = Frame(app, width=1366, height=46, bg="#f2f2f2")
lowerFrame.place(x=0, y=702)

hoverFrame = Frame(height = 40, width = 3, bg = "red")
hoverFrame.place(x = 2, y = 212)

def on_enter_userLabel(e):
    userLabel.config(image = imageUserLabel1, bg= "#f2f2f2")
def on_leave_userLabel(e):
    userLabel.config(image = imageUserLabel, bg = "#f2f2f2")
    
userLabel = Label(leftFrame, image = imageUserLabel, bg = "#f2f2f2")
userLabel.bind("<Enter>", on_enter_userLabel)
userLabel.bind("<Leave>", on_leave_userLabel)
userLabel.place(x = 27, y = 42)


def on_button_click_with_section(func, button):
    func()
    on_button_click(button)

homeButton = Button(leftFrame, text = "   Home", border = 0, cursor = "hand2", width = 408, image = iconHome, compound = LEFT, height = 0, font = ("League Spartan", 14), bg = "#f2f2f2", justify = LEFT, fg = "red", command=lambda: on_button_click_with_section(home_section, homeButton))
homeButton.place(x = -108, y = 209)

liveButton = Button(leftFrame, text = "   Live", border = 0, compound = LEFT, width = 416, cursor = "hand2", image = iconLive, height = 0, font = ("League Spartan", 14), bg = "#f2f2f2", justify = LEFT, command=lambda: on_button_click_with_section(live_section, liveButton))
liveButton.place(x = -118, y = 282)

overviewButton = Button(leftFrame, text = "   Overview", cursor = "hand2", image = iconOverview, compound = LEFT, border = 0, width = 372, height = 0, font = ("League Spartan", 14), bg = "#f2f2f2", justify = LEFT, command=lambda: on_button_click_with_section(overview_section, overviewButton))
overviewButton.place(x = -76, y = 348)

matchButton = Button(leftFrame, text = "   Matches", border = 0, cursor = "hand2", width = 390, image = iconMatch, compound = LEFT, height = 0, font = ("League Spartan", 14), bg = "#f2f2f2", justify = LEFT, command=lambda: on_button_click_with_section(matches_section, matchButton))
matchButton.place(x = -90, y = 414)

standingsButton = Button(leftFrame, text = "   Standings", cursor = "hand2", image = iconStandings, compound=LEFT, border = 0, width = 390, height = 0, font = ("League Spartan", 14), bg = "#f2f2f2", justify = LEFT, command=lambda: on_button_click_with_section(standing_section, standingsButton))
standingsButton.place(x = -85, y = 480)

personalizeButton = Button(leftFrame, text = "   Personalization", cursor = "hand2", border = 0, image = iconPersonalize, compound = LEFT, width = 326, height = 0, font = ("League Spartan", 14), bg = "#f2f2f2", justify = LEFT, command=lambda: on_button_click_with_section(personalization_section, personalizeButton))
personalizeButton.place(x = -32, y = 546)

feedbackButton = Button(leftFrame, text = "   Feedback & Support", cursor = "hand2", image = iconFeedback, compound = LEFT, border = 0, width = 300, height = 0, font = ("League Spartan", 14), bg = "#f2f2f2", justify = LEFT, command=lambda: on_button_click_with_section(feedback_section, feedbackButton))
feedbackButton.place(x = 0, y = 612)

photo_references = []


def select_image():
    global image
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        with open(file_path, "rb") as image_file:
            image = Image.open(file_path)
            image = resize_image(image, (70, 70))  # Resize the image to 70x70
            image = make_round_image(image, (70, 70))
            save_image_to_mongodb(image)
            photo = ImageTk.PhotoImage(image)
            profile_image_label.config(image=photo)
            profile_image_label.image = photo
            
    
def display_image(image):
    global img_label
    photo = ImageTk.PhotoImage(image)
    img_label = Label(app, image=photo, bg = "#FFF")
    img_label.place(x = 45, y = 56)

    img_label.image = photo
    photo_references.append(photo)


profile_image_label = Label(app, bg = "#FFF")
profile_image_label.place(x=46,y=68) 

select_button = Button(app, text="Select Image", command=select_image, cursor = "hand2", bg="#FFF", border = 0)
select_button.place(x = 140, y = 112)
profile_picture = fetch_image_from_mongodb()

profile_picture1 = fetch_image_from_mongodb()
pp = profile_picture1.resize((160, 160))

photo = ImageTk.PhotoImage(profile_picture)
profile_image_label.config(image=photo)
profile_image_label.image = photo


def on_button_click(button):
    # Reset the hoverFrame position for all buttons
    hoverFrame.place_forget()

    # Position the hoverFrame based on the clicked button
    if button == homeButton:
        hoverFrame.place(x=2, y=212)
    elif button == liveButton:
        hoverFrame.place(x=2, y=286)
    elif button == overviewButton:
        hoverFrame.place(x=2, y=352)
    elif button == matchButton:
        hoverFrame.place(x=2, y=418)
    elif button == standingsButton:
        hoverFrame.place(x=2, y=484)
    elif button == personalizeButton:
        hoverFrame.place(x=2, y=550)
    elif button == feedbackButton:
        hoverFrame.place(x=2, y=616)

home_section()

app.mainloop()