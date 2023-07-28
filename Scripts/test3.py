import tkinter as tk
import platform

def save_device_info(username, device_info):
    with open("device_info.txt", "a") as f:
        f.write(f"Username: {username}\n")
        f.write(f"Device Information:\n")
        for key, value in device_info.items():
            f.write(f"{key}: {value}\n")
        f.write("-" * 30 + "\n")

def login():
    # Get the entered username and password
    username = username_entry.get()
    password = password_entry.get()

    # Dummy authentication check (Replace this with your actual authentication logic)
    if username == "example" and password == "password":
        # Get device information
        device_info = {
            "System": platform.system(),
            "Node Name": platform.node(),
            "Release": platform.release(),
            "Version": platform.version(),
            "Machine": platform.machine(),
            "Processor": platform.processor()
        }

        # Save device information
        save_device_info(username, device_info)
        status_label.config(text="Login successful! Device information saved.")
    else:
        status_label.config(text="Invalid username or password.")

# Create the Tkinter window
root = tk.Tk()
root.title("Login Page")

# Create widgets
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

login_button = tk.Button(root, text="Login", command=login)
login_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()