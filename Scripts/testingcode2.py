import tkinter as tk

def update_cursor_position(event):
    custom_cursor.place(x=event.x, y=event.y)

root = tk.Tk()
root.geometry("400x400")

# Hide the default cursor
root.config(cursor='none')

# Load your custom cursor image
cursor_image = tk.PhotoImage(file='C:\\Users\\shahi\\Downloads\\MartyrLeague\\Images\\show.png')

# Create a Label widget to display the custom cursor image
custom_cursor = tk.Label(root, image=cursor_image, bd=0)

# Bind the custom cursor to the mouse movement
root.bind('<Motion>', update_cursor_position)

# Ensure the cursor image is always on top of other widgets
custom_cursor.lift()

root.mainloop()
