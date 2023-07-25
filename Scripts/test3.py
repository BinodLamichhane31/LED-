import tkinter as tk

def create_paragraph_label(root, text):
    label = tk.Label(root, text=text, wraplength=400, justify="left", font=("Arial", 12))
    label.pack(padx=10, pady=10)  # You can also use grid() instead of pack() if you prefer.

def main():
    # Step 2: Create the main application window
    root = tk.Tk()
    root.title("Paragraph Label Example")

    # Step 3: Create and display the paragraph label
    paragraph_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed quis justo eu odio rhoncus euismod non in metus. Fusce hendrerit nunc a nisl congue facilisis. Nulla facilisi. Proin ut neque at est venenatis interdum. Nam scelerisque purus eu ligula dignissim tempus. Nullam luctus ac nisi et congue. Vestibulum rhoncus blandit mi, sit amet ullamcorper felis tincidunt at. Nulla facilisi. Sed laoreet volutpat turpis. Nulla facilisi."

    create_paragraph_label(root, paragraph_text)

    # Step 4: Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
