def on_focus_in(event):
    if event.widget.get() in ("Full Name", "Contact No.", "Email"):
        event.widget.delete(0, "end")
    if event.widget.get() in ("New Password", "Confirm New Password"):
        event.widget.delete(0, "end")
        event.widget.config(show="●")

def on_focus_out(event,entry):
    if event.widget.get() == "":
        if event.widget == entry or event.widget == entry:
            event.widget.config(show="●")
            event.widget.insert(0, "New Password" if event.widget == entry else "Confirm New Password")
        elif event.widget == entry:
            event.widget.insert(0, "Full Name")
        elif event.widget == entry:
            event.widget.insert(0, "Contact No.")
        elif event.widget == entry:
            event.widget.insert(0, "Email")