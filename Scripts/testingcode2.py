import tkinter as tk
import pymongo
from bson.binary import Binary
from PIL import Image, ImageTk
from io import BytesIO

# Connect to MongoDB
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['football_database']
feedCollection = db['feedBacks']

def submit_feedback():
    # Retrieve all images from the database
    all_feedback = feedCollection.find()

    images_frame.pack_forget()  # Clear the previous images frame
    images_frame.pack()  # Repack the frame

    for feedback in all_feedback:
        image_data = feedback['image_data']
        image = Image.open(BytesIO(image_data))
        photo = ImageTk.PhotoImage(image)

        image_label = tk.Label(images_frame, image=photo)
        image_label.image = photo
        image_label.pack(pady=0)

root = tk.Tk()
root.title("Feedback App")

submit_button = tk.Button(root, text="Submit", command=submit_feedback)
submit_button.pack(pady=10)

images_frame = tk.Frame(root)
images_frame.pack(pady=10)

root.mainloop()
