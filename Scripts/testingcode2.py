import tkinter as tk
from PIL import Image, ImageTk, ImageSequence

def show_loading_animation():
    # Load the original GIF file
    gif_path = "C:\\Users\\shahi\\Downloads\\MartyrLeague\\Images\\searchgif-min.gif"
    original_gif = Image.open(gif_path)

    # Resize the GIF to 40x40 pixels
    resized_gif = original_gif.resize((2, 2), Image.BILINEAR)

    # Create PhotoImage from the resized GIF
    loading_gif_frame = ImageTk.PhotoImage(resized_gif)

    # Function to update the animation frame
    def update_animation(index):
        loading_label.config(image=loading_gif_frames[index])
        # Reduce the delay (increase speed) to update the animation frames
        root.after(50, update_animation, (index + 1) % len(loading_gif_frames))

    # Load the GIF frames and store them in a list
    loading_gif_frames = [ImageTk.PhotoImage(frame.copy()) for frame in ImageSequence.Iterator(original_gif)]

    # Start the animation
    update_animation(0)

# Create the main Tkinter window
root = tk.Tk()
root.title("Loading Animation Example")
root.geometry("400x400")

# Label to display the loading animation GIF
loading_label = tk.Label(root)
loading_label.pack()

# Button to trigger the loading animation
start_button = tk.Button(root, text="Start Loading", command=show_loading_animation)
start_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
