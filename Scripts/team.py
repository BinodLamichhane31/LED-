from pymongo import MongoClient
from tkinter import *
from tkinter import messagebox, filedialog
from base64 import b64encode
import io,webbrowser
from PIL import Image, ImageTk


football_client = MongoClient('mongodb://localhost:27017/')
football_database = football_client['football_database']
team_collection = football_database['teams']


def submit():
    
    player_data = {
        'name': label_entry[0].get(),
        'founded': label_entry[1].get(),
        'location': label_entry[2].get(),
        'stadium': label_entry[3].get(),
        'president': label_entry[4].get(),
        'manager': label_entry[5].get(),
        'captain': label_entry[6].get(),
        'link': label_entry[7].get(),
        'image':encoded_image
    }
    team_collection.insert_one(player_data)
    for entry in label_entry:
        entry.delete(0, 'end')
    messagebox.showinfo('','Successfully stored.')

def picture():
    global encoded_image
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        with open(file_path, "rb") as image_file:
            encoded_image = b64encode(image_file.read())
def label_and_entry(player_window, label_text, x, y, x1, y1):
    global box_entry
    text_label = Label(player_window, text=label_text)
    text_label.place(x=x, y=y)
    box_entry = Entry(player_window)
    box_entry.place(x=x1, y=y1)
    return box_entry


player_window = Tk()
player_window.geometry("400x500")
label_entry = []
label_entry.append(label_and_entry(player_window,"Club Name:",10,20,100,20))
label_entry.append(label_and_entry(player_window,"Founded Year:",10,50,100,50))
label_entry.append(label_and_entry(player_window,"Location:",10,80,100,80))
label_entry.append(label_and_entry(player_window,"Stadium:",10,110,100,110))
label_entry.append(label_and_entry(player_window,"President:",10,140,100,140))
label_entry.append(label_and_entry(player_window,"Manager:",10,170,100,170))
label_entry.append(label_and_entry(player_window,"Captain:",10,200,100,200))
label_entry.append(label_and_entry(player_window,"Link:",10,230,100,230))
submit_btn = Button(player_window,text='Choose Photo',command=picture)
submit_btn.place(x=70,y=260)
submit_btn = Button(player_window,text='Submit',command=submit)
submit_btn.place(x=170,y=290)

player_window.mainloop()
