import tkinter as tk
from tkinter import filedialog
from PIL import Image as PILImage, ImageDraw, ImageTk

app = tk.Tk()
app.geometry("300x300")

def create_rounded_profile_picture(input_path, output_path, size=(60, 60)):
    # Step 1: Load the user's selected profile picture
    profile_image = PILImage.open(input_path)

    # Step 2: Resize the image to the desired dimensions
    profile_image = profile_image.resize(size)

    # Step 3: Create a circular mask
    mask = PILImage.new("L", profile_image.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, profile_image.size[0], profile_image.size[1]), fill=255)  # Change fill value to 255

    # Step 4: Apply the mask to the profile image
    rounded_image = PILImage.new("RGBA", profile_image.size, (255, 255, 255, 0))
    rounded_image.paste(profile_image, (0, 0), mask=mask)

    # Step 5: Save the rounded image
    rounded_image.save(output_path)

def get_profile_picture_path():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select Profile Picture", filetypes=[("Image files", "*.jpg;*.png;*.jpeg")])
    return file_path

def display_rounded_profile_picture():
    input_path = get_profile_picture_path()
    if input_path:
        output_path = "rounded_profile_picture.png"
        create_rounded_profile_picture(input_path, output_path)

        # Create a PhotoImage object from the rounded profile picture
        rounded_profile_image = ImageTk.PhotoImage(file=output_path)

        # Create a button with the rounded profile picture as the image
        profile_button = tk.Button(app, image=rounded_profile_image, border = 0, background="#fff", command=profile_button_clicked)
        profile_button.image = rounded_profile_image  # Keep a reference to the image
        profile_button.place(x=180, y=80)

def profile_button_clicked():
    # Replace this function with the desired action when the button is clicked
    print("Profile button clicked!")
    create_rounded_profile_picture() 
display_button = tk.Button(app, text="Select Profile Picture", command=display_rounded_profile_picture)
display_button.pack(pady=20)

app.mainloop()
