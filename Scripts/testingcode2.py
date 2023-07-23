import tkinter as tk
from tkinter import PhotoImage

def custom_button_click():
    print("Custom button clicked!")

# Create the Tkinter window and set its properties
root = tk.Tk()
root.title("Custom Round Button Example")
root.geometry("300x200")

# Create a transparent image for the button
button_image = PhotoImage(width=1, height=1)

# Store the PhotoImage in a persistent attribute of the root to prevent garbage collection
root.custom_button_image = button_image

# Create a custom button by using the label widget
custom_button = tk.Label(root, image=root.custom_button_image, bg="#FFA500", bd=0, relief=tk.FLAT, cursor="hand2")
custom_button.pack(pady=20)

# Bind the custom_button_click function to the button's click event
custom_button.bind("<Button-1>", lambda event: custom_button_click())

# Start the Tkinter event loop
root.mainloop()
