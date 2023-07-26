import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw
import io
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB connection string
db = client["your_database_name"]  # Replace with your database name
collection = db["profile_pictures"]  # Replace with your collection name

def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path:
        image = Image.open(file_path)
        image = resize_image(image, (80, 80))  # Resize the image to 80x80
        image = make_round_image(image, (80, 80))

        # Save the selected image to MongoDB
        save_image_to_mongodb(image)

        photo = ImageTk.PhotoImage(image)
        profile_image_label.config(image=photo)
        profile_image_label.image = photo

def resize_image(image, size):
    return image.resize(size, Image.BILINEAR)

def make_round_image(image, size):
    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size[0], size[1]), fill=255)
    result = Image.new("RGBA", size, (255, 255, 255, 0))
    result.paste(image, (0, 0), mask)
    return result

def save_image_to_mongodb(image):
    image_byte_array = io.BytesIO()
    image.save(image_byte_array, format='PNG')
    image_binary = image_byte_array.getvalue()
    collection.delete_many({})  # Clear any existing profile pictures (optional)
    collection.insert_one({"profile_image": image_binary})

def fetch_image_from_mongodb():
    data = collection.find_one({})
    if data and "profile_image" in data:
        return Image.open(io.BytesIO(data["profile_image"]))

    # If no profile picture is found, return a default image (optional)
    return Image.open("Images\\loginicon.png")

# Create the main application window
app = tk.Tk()
app.title("Profile Picture Selector")

# Create a label to display the profile image
profile_image_label = tk.Label(app)
profile_image_label.pack(pady=10)

# Create a button to open the file dialog for image selection
select_button = tk.Button(app, text="Select Image", command=select_image)
select_button.pack(pady=5)

# Fetch the profile picture from MongoDB and display it on app startup
profile_picture = fetch_image_from_mongodb()
photo = ImageTk.PhotoImage(profile_picture)
profile_image_label.config(image=photo)
profile_image_label.image = photo

# Run the main event loop
app.mainloop()
