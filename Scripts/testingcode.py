import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw

def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path:
        image = Image.open(file_path)
        image = resize_image(image, (80, 80))  # Resize the image to 80x80
        image = make_round_image(image, (80, 80))
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

# Create the main application window
app = tk.Tk()
app.title("Profile Picture Selector")

# Create a label to display the profile image
profile_image_label = tk.Label(app)
profile_image_label.pack(pady=10)

# Create a button to open the file dialog for image selection
select_button = tk.Button(app, text="Select Image", command=select_image)
select_button.pack(pady=5)

# Run the main event loop
app.mainloop()
