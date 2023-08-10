from tkinter import *

def on_mousewheel(event):
    """
    Adjust the vertical scrolling of the canvas widget based on mousewheel movement.
    """
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

# Create a root frame
root_frame = Frame()
root_frame.place(x = 580, y = 48)

# Create a canvas
canvas = Canvas(root_frame, background="#F2F2F2", width=740, height=600)
canvas.pack(side=LEFT, fill=BOTH, expand=True)

# Create a scrollbar
scrollbar = Scrollbar(root_frame, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)
canvas.configure(yscrollcommand=scrollbar.set)

# Bind the mousewheel event to the canvas
canvas.bind_all("<MouseWheel>", on_mousewheel)

# Create a frame inside the canvas to hold the content
content_frame = Frame(canvas, background="#F2F2F2", width=700, height=600)
content_frame.pack()

# Add the block of information with proper styling and headings
title_label = Label(content_frame, text="Introducing the ultimate A Division Football League App", wraplength=800, font=("Tahoma", 16, "bold"), bg="#F2F2F2")
title_label.pack(pady=10, padx=40, anchor="w")

description_label1 = Label(content_frame, text="Your go-to companion for all things related to the thrilling world of A Division football.", wraplength=800, font=("Default", 12), bg="#F2F2F2")
description_label1.pack(pady=10, padx=40, anchor="w")

description_label2 = Label(content_frame, text="This innovative and user-friendly application is designed to provide fans, players, and enthusiasts\nwith a comprehensive  platform to stay updated, engaged, and  connected to their favorite  teams\nand matches.", wraplength=800, justify="left",font=("Default", 12), bg="#F2F2F2")
description_label2.pack(pady=10, padx=40, anchor="w")

description_label3 = Label(content_frame, text="With our A Division Football League App, you can access real-time match scores, standings, and \nstatistics, ensuring you never miss a moment of the action.", wraplength=800, justify="left",font=("Default", 12), bg="#F2F2F2")
description_label3.pack(pady=10, padx=40, anchor="w")

features_label = Label(content_frame, text="Key Features", font=("Tahoma", 14, "bold"), bg="#F2F2F2")
features_label.pack(pady=10, padx=40, anchor="w")

feature1_label = Label(content_frame, text="• Real-time match scores, standings, and statistics", font=("Default", 12), bg="#F2F2F2")
feature1_label.pack(anchor="w", padx=40)

feature2_label = Label(content_frame, text="• Upcoming fixtures and match schedules", font=("Default", 12), bg="#F2F2F2")
feature2_label.pack(anchor="w", padx=40)

feature3_label = Label(content_frame, text="• Personalized notifications for favorite teams", font=("Default", 12), bg="#F2F2F2")
feature3_label.pack(anchor="w", padx=40)

commentary_label = Label(content_frame, text="Live Commentary", font=("Tahoma", 14, "bold"), bg="#F2F2F2")
commentary_label.pack(pady=10, padx=40, anchor="w")

commentary_desc_label = Label(content_frame, text="Experience the excitement firsthand  with our in-app live commentary feature, providing you with \nminute-by-minute updates, key player performances, and crucial match moments.",justify="left" ,font=("Default", 12), bg="#F2F2F2")
commentary_desc_label.pack(anchor="w", padx=40)

multimedia_label = Label(content_frame, text="Immersive Multimedia Content", font=("Tahoma", 14, "bold"), bg="#F2F2F2")
multimedia_label.pack(pady=10, padx=40, anchor="w")

multimedia_desc_label = Label(content_frame, text="Dive into the heart of the game through our immersive multimedia content. Watch match highlights,\nenjoy player interviews, and get exclusive behind-the-scenes footage.",justify="left" ,font=("Default", 12), bg="#F2F2F2")
multimedia_desc_label.pack(anchor="w", padx=40)

community_label = Label(content_frame, text="Vibrant Community", font=("Tahoma", 14, "bold"), bg="#F2F2F2")
community_label.pack(pady=10, anchor="w", padx=40)

community_desc_label = Label(content_frame, text="Share your thoughts, celebrate victories, and stay connected with the A Division football community.\nEngage in lively discussions with fellow fans through the integrated chat feature. ", justify=LEFT,font=("Default", 12), bg="#F2F2F2")
community_desc_label.pack(anchor="w", padx=40)

data_label = Label(content_frame, text="Historical Data and Profiles", font=("Tahoma", 14, "bold"), bg="#F2F2F2")
data_label.pack(pady=10, anchor="w", padx=40)

data_desc_label = Label(content_frame, text="Explore a  treasure trove  of historical data,  club profiles, player profiles, and  fascinating trivia to\nenhance your knowledge of A Division football.",justify='left' ,font=("Default", 12), bg="#F2F2F2")
data_desc_label.pack(anchor="w", padx=40)

def goto_login_page():
    '''
    Destroys the about us frame i.e. root_frame and opens the login page.
    '''
    root_frame.destroy()

goto_login_page_button = Button(root_frame,text='x',font=("Default", 12), bg="#F2F2F2",relief= SUNKEN,  highlightthickness= 2, border = 0, command=goto_login_page)
goto_login_page_button.place(x=720,y=1)
# Create a window into the canvas
canvas.create_window((0, 0), window=content_frame, anchor="nw")

# Update the scrollable region when the window size changes
def on_configure(event):
    '''
    Adjust the scrollable region
    '''
    canvas.configure(scrollregion=canvas.bbox("all"))

canvas.bind("<Configure>", on_configure)

root_frame.mainloop()
