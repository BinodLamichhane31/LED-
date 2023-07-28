# Importing all the required libraries
from tkinter import *
from PIL import Image, ImageTk

def create_personalization_btns(frame_personaliztion, image_path1, text, x, y, cmd):
        '''
        Create the buttons in personalization frame with icon.

        Args:
            frame_personalization:  The frame to place the buttons and icons.
            image_path1: The path to the icon images.
            text: The text for the button.
            x: x-coordinate for the button.
            y: y-coordinate for the button.
            cmd: The command to be executed when button is clicked.
        Returns:
            The created button with icon.

        '''
        personalization_icon = Image.open(image_path1)
        personalization_icon = personalization_icon.resize((20, 20))
        personalization_image = ImageTk.PhotoImage(personalization_icon)
        per_img_label = Label(frame_personaliztion, image=personalization_image, border=0, bg="#f2f2f2")
        per_img_label.image = personalization_image
        per_img_label.place(x=x, y=y)
        per_btn = Button(frame_personaliztion, text="    "+text,cursor='hand2' ,image=personalization_image,height=0, border=0, bg="#f2f2f2",compound=LEFT,width = 326,font=('Tahoma', '12'), anchor='w', command=cmd)
        per_btn.place(x=x, y=y)
        return per_btn


    