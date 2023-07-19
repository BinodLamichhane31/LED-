import tkinter as tk
from pymongo import MongoClient
from PIL import ImageTk, Image
import io
import tkinter.filedialog as filedialog


# MongoDB connection
client = MongoClient('mongodb://localhost:27017')
db = client['image_db']
collection = db['images']

# Global variables
current_image_index = 0
image_list = []
image_labels = []
# Fetch images from MongoDB
def fetch_images():
    global image_list
    image_list = list(collection.find({}, {'_id': 0, 'image': 1}))

# Event handlers for left and right buttons
def move_left():
    global current_image_index
    if current_image_index > 0:
        current_image_index -= 1
    focus_image()

def move_right():
    global current_image_index, image_list
    if current_image_index < len(image_list) - 1:
        current_image_index += 1
    focus_image()



# Select and store image in MongoDB
def select_and_store_image():
    filename = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if filename:
        with open(filename, 'rb') as image_file:
            image_data = image_file.read()
            collection.insert_one({'image': image_data})
        update_image()
        fetch_images()


root = tk.Tk()
root.title("Image Viewer")

# Configure grid layout
root.grid_columnconfigure(0, weight=1)

for i in range(len(image_list)):
    label = tk.Label(root, height=100, width=100, relief="flat")
    label.grid(row=0, column=i, padx=5, pady=5)
    image_labels.append(label)

# Update the `update_image()` function to display images on the labels
def update_image():
    global current_image_index, image_list
    if image_list and 0 <= current_image_index < len(image_list):
        image_data = image_list[current_image_index]['image']
        image = Image.open(io.BytesIO(image_data))
        image = image.resize((100, 100), Image.BILINEAR)
        photo = ImageTk.PhotoImage(image)
        image_label.configure(image=photo)
        image_label.image = photo

        for i in range(len(image_labels)):
            if i < len(image_list):
                image_data = image_list[i]['image']
                image = Image.open(io.BytesIO(image_data))
                image = image.resize((100, 100), Image.BILINEAR)
                photo = ImageTk.PhotoImage(image)
                image_labels[i].configure(image=photo)
                image_labels[i].image = photo
            else:
                # Clear any additional labels
                image_labels[i].configure(image=None)

# Add image labels to the gri
for i in range(len(image_list)):
    label = tk.Label(root, height=100, width=100, relief="flat")
    label.grid(row=0, column=i, padx=5, pady=5)
    image_labels.append(label)

# Update the `focus_image()` function to apply focus on the selected image
def focus_image():
    global current_image_index, image_labels
    if image_list and 0 <= current_image_index < len(image_list):
        # Reset all labels
        for label in image_labels:
            label.configure(relief="flat")

        # Apply focus on the selected image
        image_labels[current_image_index].configure(relief="solid")


# Add image labels to the grid
for i in range(len(image_list)):
    label = tk.Label(root, height=100, width=100, relief="flat")
    label.grid(row=0, column=i, padx=5, pady=5)
    image_labels.append(label)

# Add the image label for the focused image
image_label = tk.Label(root, height=500, width=500, relief="solid")
image_label.grid(row=1, column=0, columnspan=max(len(image_list), 1), padx=5, pady=5)



# Rest of the code remains unchanged

left_button = tk.Button(root, text="Left", command=move_left)
left_button.grid(row=2, column=0, padx=5, pady=5)

right_button = tk.Button(root, text="Right", command=move_right)
right_button.grid(row=2, column=1, padx=5, pady=5)

select_button = tk.Button(root, text="Select and Store Image", command=select_and_store_image)
select_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)


# Fetch images from MongoDB on startup
fetch_images()

# Display the first image
update_image()

# Start the Tkinter event loop
root.mainloop()
