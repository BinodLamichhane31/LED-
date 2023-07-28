import tkinter as tk

def on_focus_in(event):
    if event.widget.get() in ("Full Name", "Contact No.", "Email"):
        event.widget.delete(0, "end")
    if event.widget.get() in ("New Password", "Confirm New Password"):
        event.widget.delete(0, "end")
        event.widget.config(show="●")

def on_focus_out(event):
    if event.widget.get() == "":
        if event.widget == psw_entry or event.widget == confirm_entry:
            if psw_entry.get() == "New Password":
                event.widget.config(show="")
            else:
                event.widget.config(show="New Password")

            event.widget.insert(0, "New Password" if event.widget == psw_entry else "Confirm New Password")
        elif event.widget == uname_entry:
            event.widget.insert(0, "Full Name")
        elif event.widget == phone_entry:
            event.widget.insert(0, "Contact No.")
        elif event.widget == email_entry:
            event.widget.insert(0, "Email")

root = tk.Tk()
root.title("Entry Widget Example")

# Create entry widgets
uname_entry = tk.Entry(root, width=30)
phone_entry = tk.Entry(root, width=30)
email_entry = tk.Entry(root, width=30)
psw_entry = tk.Entry(root, width=30, show="●")
confirm_entry = tk.Entry(root, width=30, show="●")

# Set default placeholder texts
uname_entry.insert(0, "Full Name")
phone_entry.insert(0, "Contact No.")
email_entry.insert(0, "Email")
psw_entry.insert(0, "New Password")
confirm_entry.insert(0, "Confirm New Password")

# Bind focus events to the entry widgets
uname_entry.bind("<FocusIn>", on_focus_in)
phone_entry.bind("<FocusIn>", on_focus_in)
email_entry.bind("<FocusIn>", on_focus_in)
psw_entry.bind("<FocusIn>", on_focus_in)
confirm_entry.bind("<FocusIn>", on_focus_in)

uname_entry.bind("<FocusOut>", on_focus_out)
phone_entry.bind("<FocusOut>", on_focus_out)
email_entry.bind("<FocusOut>", on_focus_out)
psw_entry.bind("<FocusOut>", on_focus_out)
confirm_entry.bind("<FocusOut>", on_focus_out)

# Pack entry widgets and run the main event loop
uname_entry.pack(pady=5)
phone_entry.pack(pady=5)
email_entry.pack(pady=5)
psw_entry.pack(pady=5)
confirm_entry.pack(pady=5)

root.mainloop()
