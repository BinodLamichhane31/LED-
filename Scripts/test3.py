from tkinter import *

root = Tk()
root.state("zoomed")

frame1 = Frame(root, width=600, height=400, bg="#FFFACD") # assigning a frame named frame1 that can be accessed globally...

def on_enter_home(e): # creating function that will trigger the hover effect when we enter the button...

    frame1.place(x=e.widget.winfo_x(), y=(e.widget.winfo_y()+40)) # placing the widget(button) just below the main button Home..

    clear_frame() # clearing the frame before placing the buttons hello and hi...

    create_button(frame1, "hello", 50, 50) # passing the arguments to the parameter...

    create_button(frame1, "hi", 150, 50) # passing the arguments to the parameter...

def on_enter_destination(e): # creating function that will trigger the hover effect when we enter the button...

    frame1.place(x=e.widget.winfo_x(), y=(e.widget.winfo_y()+40))  # placing the widget(button) just below the main button destination..
    frame1.lift()

    clear_frame() # clearing the frame before placing the buttons Bye and See you...

    create_button(frame1, "Bye", 50, 50) # passing the arguments to the parameter...

    create_button(frame1, "See you", 150, 50) # passing the arguments to the parameter...

def on_enter_jpt(e): # creating function that will trigger the hover effect when we enter the button...

    frame1.place(x=e.widget.winfo_x(), y=(e.widget.winfo_y()+40))  # placing the widget(button) just below the main button destination..

    clear_frame()

def on_frame_leave(e):  # function to make the widget forget it's placement whenever we leave the frame...
    frame1.place_forget() 

def create_button(frame, text, x, y): # creating the sub button function using parameter
    button = Button(frame, text=text, font=("Tahoma", 14, "bold"), border=0, cursor="hand2", bg = "#FFFACD")
    button.place(x=x, y=y)
    return button

def create_main_button(frame, text, x, y, enter_callback):  # creation of main buttons...
    button = Button(frame, text=text, font=("Tahoma", 14, "bold"), border=0, cursor="hand2")
    button.place(x=x, y=y)
    button.bind("<Enter>", enter_callback)
    frame1.bind("<Leave>", on_frame_leave)
    return button

def clear_frame(): # Line 12 and 22 are the functionality provided by this function...
    for widget in frame1.winfo_children(): # fetches the information/name of buttons created in the frames...
        widget.destroy() # triggering the deletion of buttons that are already in there...

buttons = []
buttons.append(create_main_button(root, "Home", 592, 16, on_enter_home))
buttons.append(create_main_button(root, "Destination", 762, 16, on_enter_destination))
buttons.append(create_main_button(root, "JPT", 762, 420, on_enter_jpt))

root.mainloop()

