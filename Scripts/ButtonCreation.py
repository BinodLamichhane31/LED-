from tkinter import *
from PIL import Image, ImageTk

def create_button_with_icon(frame, image_path, text, x, y,cmd):
    """
    Create a button with an icon.

    Args:
        frame: The parent frame to place the button and icon.
        image_path: The path to the icon image.
        text: The text label for the button.
        x: The x-coordinate of the button.
        y: The y-coordinate of the button.
        cmd: The command to be executed when the button is clicked.

    Returns:
        The created button.
    """
    icon = Image.open(image_path)
    icon = icon.resize((20, 20))
    image = ImageTk.PhotoImage(icon)
    img_label = Label(frame, image=image, border=0, bg="sky blue")
    img_label.image = image
    img_label.place(x=x, y=y)
    btn = Button(frame, text=text, border=0, bg="sky blue", font=('Segoe Print', '12', 'bold'), width=25, anchor='w',command=cmd)
    btn.place(x=x+30, y=y-10)
    return btn

def highlight_button(btn):
    """
    Change the color of the button text when the button is clicked.

    Args:
        btn: The button to highlight.
    """
    btn.config(bg="sky blue",fg="blue")

def reset_button(btn):
    """
    Reset the color of button text.

    Args:
        btn: The button to reset.
    """
    btn.config(bg="sky blue",fg="black")

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
        per_img_label = Label(frame_personaliztion, image=personalization_image, border=0, bg="sky blue")
        per_img_label.image = personalization_image
        per_img_label.place(x=x, y=y)
        per_btn = Button(frame_personaliztion, text=text, height=0, border=0, bg="sky blue", font=('Segoe Print', '12', 'bold'), width=20, anchor='w', command=cmd)
        per_btn.place(x=x + 30, y=y - 10)
        return per_btn
