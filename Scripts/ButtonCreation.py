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
        per_img_label = Label(frame_personaliztion, image=personalization_image, border=0, bg="#FFFACD")
        per_img_label.image = personalization_image
        per_img_label.place(x=x, y=y)
        per_btn = Button(frame_personaliztion, text=text, height=0, border=0, bg="#FFFACD", font=('Segoe Print', '12', 'bold'), width=20, anchor='w', command=cmd)
        per_btn.place(x=x + 30, y=y - 10)
        return per_btn
def create_font_buttons(setting_window,text,text_font,x,y):
      font_btns = Button(setting_window,text,font=(text_font, '12', ''),height=0, border=0, bg="#FFFACD")
      font_btns.place(x=x,y=y)
      return font_btns

    