# Importing all the required libraries
from tkinter import *
from PIL import Image, ImageDraw
from pymongo import MongoClient
from base64 import *
import io

    # Connecting to the database
football_client = MongoClient('mongodb://localhost:27017/')
football_database = football_client['football_database']
picture_collection = football_database['picture']

with open("Scripts\\phone_number.txt", "r") as file:
    phone = file.read().strip()
    user_data = picture_collection.find_one({"phone":phone})
   
def resize_image(image, size):
    _image = image.resize(size, Image.BILINEAR)
    return _image

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
    picture_collection.delete_many({"user_phone":phone})  # Clear any existing profile pictures (optional)
    picture_collection.insert_one({"user_phone":phone,"profile_image": image_binary})

def fetch_image_from_mongodb():
    data = picture_collection.find_one({"user_phone":phone})
    if data and "profile_image" in data:
        return Image.open(io.BytesIO(data["profile_image"]))

    # If no profile picture is found, return a default image 
    default_pic = Image.open("Images\\user.png")
    default_pic=default_pic.resize((70,70))
    return default_pic

