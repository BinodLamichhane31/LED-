import tkinter as tk

def on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

# Create a root frame
root_frame = tk.Frame()
root_frame.pack()

# Create a canvas
canvas = tk.Canvas(root_frame, background="#FFFACD", width=740, height=600)
canvas.place(x = 140, y = 120)

# Create a scrollbar
scrollbar = tk.Scrollbar(root_frame, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.configure(yscrollcommand=scrollbar.set)

# Bind the mousewheel event to the canvas
canvas.bind_all("<MouseWheel>", on_mousewheel)

# Create a frame inside the canvas to hold the content
content_frame = tk.Frame(canvas, background="#FFFACD", width=700, height=600)
content_frame.pack()

# Add the block of information with proper styling and headings
title_label = tk.Label(content_frame, text="Introducing the ultimate A Division Football League App", wraplength=800, font=("Helvetica", 16, "bold"), bg="#FFFACD")
title_label.pack(pady=10, padx=40, anchor="w")

description_label1 = tk.Label(content_frame, text="Your go-to companion for all things related to the thrilling world of A Division football.", wraplength=800, font=("Helvetica", 12), bg="#FFFACD")
description_label1.pack(pady=10, padx=40, anchor="w")

description_label2 = tk.Label(content_frame, text="This innovative and user-friendly application is designed to provide fans, players, and enthusiasts with a comprehensive platform to stay updated, engaged, and connected to their favorite teams and matches.", wraplength=800, font=("Helvetica", 12), bg="#FFFACD")
description_label2.pack(pady=10, padx=40, anchor="w")

description_label3 = tk.Label(content_frame, text="With our A Division Football League App, you can access real-time match scores, standings, and statistics, ensuring you never miss a moment of the action.", wraplength=800, font=("Helvetica", 12), bg="#FFFACD")
description_label3.pack(pady=10, padx=40, anchor="w")

features_label = tk.Label(content_frame, text="Key Features", font=("Helvetica", 14, "bold"), bg="#FFFACD")
features_label.pack(pady=10, padx=40, anchor="w")

feature1_label = tk.Label(content_frame, text="• Real-time match scores, standings, and statistics", font=("Helvetica", 12), bg="#FFFACD")
feature1_label.pack(anchor="w", padx=40)

feature2_label = tk.Label(content_frame, text="• Upcoming fixtures and match schedules", font=("Helvetica", 12), bg="#FFFACD")
feature2_label.pack(anchor="w", padx=40)

feature3_label = tk.Label(content_frame, text="• Personalized notifications for favorite teams", font=("Helvetica", 12), bg="#FFFACD")
feature3_label.pack(anchor="w", padx=40)

commentary_label = tk.Label(content_frame, text="Live Commentary", font=("Helvetica", 14, "bold"), bg="#FFFACD")
commentary_label.pack(pady=10, padx=40, anchor="w")

commentary_desc_label = tk.Label(content_frame, text="Experience the excitement firsthand with our in-app live commentary feature, providing you with minute-by-minute updates, key player performances, and crucial match moments.", font=("Helvetica", 12), bg="#FFFACD")
commentary_desc_label.pack(anchor="w", padx=40)

multimedia_label = tk.Label(content_frame, text="Immersive Multimedia Content", font=("Helvetica", 14, "bold"), bg="#FFFACD")
multimedia_label.pack(pady=10, padx=40, anchor="w")

multimedia_desc_label = tk.Label(content_frame, text="Dive into the heart of the game through our immersive multimedia content. Watch match highlights, enjoy player interviews, and get exclusive behind-the-scenes footage.", font=("Helvetica", 12), bg="#FFFACD")
multimedia_desc_label.pack(anchor="w", padx=40)

community_label = tk.Label(content_frame, text="Vibrant Community", font=("Helvetica", 14, "bold"), bg="#FFFACD")
community_label.pack(pady=10, anchor="w", padx=40)

community_desc_label = tk.Label(content_frame, text="Engage in lively discussions with fellow fans through the integrated chat feature. Share your thoughts, celebrate victories, and stay connected with the A Division football community.", font=("Helvetica", 12), bg="#FFFACD")
community_desc_label.pack(anchor="w", padx=40)

data_label = tk.Label(content_frame, text="Historical Data and Profiles", font=("Helvetica", 14, "bold"), bg="#FFFACD")
data_label.pack(pady=10, anchor="w", padx=40)

data_desc_label = tk.Label(content_frame, text="Explore a treasure trove of historical data, club profiles, player profiles, and fascinating trivia to enhance your knowledge of A Division football.", font=("Helvetica", 12), bg="#FFFACD")
data_desc_label.pack(anchor="w", padx=40)

# Create a window into the canvas
canvas.create_window((0, 0), window=content_frame, anchor="nw")

# Update the scrollable region when the window size changes
def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

canvas.bind("<Configure>", on_configure)

root_frame.mainloop()
