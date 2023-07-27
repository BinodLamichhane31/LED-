from tkinter import *
import time
# import sports

teams = ["churchboys", "newroad"]
current_team = None
team_data = {
    
    "churchboys": [
        {
            "name": "Ananta Tamang (captain)",
            "essay": "Ananta Tamang (Nepali: अनन्त तामाङ; born 14 January 1998) is a Nepalese professional footballer who plays as a defender for Nepal Super League club church boys united[3] and the Nepal national team. He was vice-captain of Nepal under-19 football team which went on to win the 2015 SAFF U-19 Championship. Tamang made his senior national team debut on 31 August 2015 in a friendly against India.[4]",
            "description": "Church Boys United (formally known as Church Boys FC) is a Nepali football team from balkumari neighborhood of Lalitpur that competes in the Martyr's Memorial A-Division League. The team was first promoted to Martyr's Memorial A-Division League in 2022, having won the 2022 Martyr's Memorial B-Division League."
        },
        {
            "name": "Kamal Shrestha",
            "essay": "Kamal Shrestha (Nepali: कमल श्रेष्ठ; born 10 July 1997) is a Nepalese professional footballer who plays as a defender for Church boys united and the Nepal national team.",
            "description": "The club was founded in 2009, but only participated in local tournaments. In 2019, they qualified for the Martyr's Memorial C-Division League which was their fifth attempt in C-Division League Qualifier (previously known as Martyr's Memorial 'D' Division League)[citation needed] and were promoted to the top-level Martyr's Memorial A-Division League within two seasons, in what The Kathmandu Post highlighted as a 'remarkable journey'."
        },
        {
            "name": "Arik Bista",
            "essay": "Arik Bista (born 17 March 2000) is a Nepalese professional footballer who plays as a midfielder for Martyr's Memorial A-Division League club New Road Team (NRT) and the Nepal national team His schooling was done in Bhanubhakta Memorial Higher Secondary School, Panipokhari, Kathmandu. Arik hails from a locality named Bansbari, where the whole locality is a avid football fan. Arik supports Liverpool in EPL. He made his international national debut against Bangladesh on 13 November 2020 in Dhaka.",
            "description": ""
        },
        {
            "name": "Suvas Gurung",
            "essay": "Suvash Gurung (born 7 September 1991) also known as Subash Gurung, is a Nepalese professional footballer who plays as a midfielder for Martyr's Memorial A-Division League club Sankata Boys S.C. and the Nepal national team.[1][2][3][4] He made his international debut against Kuwait on 19 November 2019 in FIFA World Cup qualification match held in Thimphu.[5]",
            "description": ""   
        },
        {
           "name": "Ashish Chaudhary",
           "essay": "Ashish Chaudhary (born 21 July 1978) is an Indian actor who has acted in many Hindi films and television productions. He is best known for portraying Boman in the comedy films Dhamaal and Double Dhamaal, winning Fear Factor: Khatron Ke Khiladi 6, participating in Jhalak Dikhhla Jaa 8 and playing Mrityunjay Roy in the romantic thriller TV series Beyhadh 2.",
           "description": ""  
        }
    ],
    "newroad": [
        {
            "name": "John Doe",
            "essay": "John Doe is a skilled defender...",
            "description": ""
        },
        {
            "name": "Jane Doe",
            "essay": "Jane Doe is a versatile midfielder...",
            "description": ""
        },
        {
            "name": "Michael Smith",
            "essay": "Michael Smith is a goal-scoring forward...",
            "description": ""
        }
    ]
    
}

def type_with_effect(text, tag="typing"):
    terminal.config(state=NORMAL)  # Enable the widget for inserting text
    for char in text:
        terminal.insert(END, char, tag)
        terminal.see(END)  # Auto-scroll to the bottom
        terminal.update()
        time.sleep(0.03)
    terminal.config(state=DISABLED)  # Disable the widget again

def on_search(event=None):
    query = search_entry.get().lower()
    search_entry.delete(3, END)
    global current_team

    if not query.startswith("fc"):
        type_with_effect("Invalid command.", "error")
        type_with_effect("\n\n", "typing")
        search_entry.delete(3, END)  # Maintain a gap between responses
        return

    command = query[3:].strip()
    if not command.endswith(";"):
        type_with_effect("Invalid command.", "error")
        type_with_effect("\n\n", "typing")
        search_entry.delete(3, END)  # Maintain a gap between responses
        return

    command = command[:-1].strip()

    if command == "exit":
        if current_team:
            type_with_effect("\nCommand passed: fc ", "output")
            type_with_effect("exit;", "command")
            type_with_effect("\n\n", "typing")  # Maintain a gap between responses
            type_with_effect(f"You have exited the {current_team} team.", "content")
            type_with_effect("\n\n", "typing")
            search_entry.delete(3, END)  # Maintain a gap between responses
            current_team = None
        else:
            type_with_effect("\nCommand passed: fc ", "output")
            type_with_effect("exit;", "command")
            type_with_effect("\n\n", "typing")  # Maintain a gap between responses
            type_with_effect("You are not currently in any team.", "content")
            type_with_effect("\n\n", "typing")
            search_entry.delete(3, END)  # Maintain a gap between responses
    elif command == "showdata":
        if current_team:
            team_desc = team_data[current_team][0]['description']
            team_desc1 = team_data[current_team][1]['description']
            type_with_effect("\nCommand passed: fc ", "output")
            type_with_effect("showdata;", "command")
            type_with_effect("\n\n", "typing")  # Maintain a gap between responses
            type_with_effect(team_desc + "\n", "content")
            type_with_effect(team_desc1 + "\n", "content")
            type_with_effect("Data for ", "heading")
            type_with_effect(current_team, "heading")
            type_with_effect(" team:\n", "content")
            players_data = team_data[current_team]
            for i, player in enumerate(players_data, start=1):
                type_with_effect(f"{i}. {player['name']}\n", "table_data")
            type_with_effect("\n\n", "typing")
            search_entry.delete(3, END)  # Maintain a gap between responses
        else:
            type_with_effect("\nCommand passed: fc ", "output")
            type_with_effect("showdata;", "command")
            type_with_effect("\n\n", "typing")  # Maintain a gap between responses
            type_with_effect("Please enter a team using 'fc {teamname};' first.", "content")
            type_with_effect("\n\n", "typing")
            search_entry.delete(3, END) # Maintain a gap between responses
    elif command in teams:
        current_team = command
        type_with_effect("\nCommand passed: fc ", "output")
        type_with_effect(f"{command};", "command")
        type_with_effect("\n\n", "typing")  # Maintain a gap between responses
        type_with_effect(f"You entered {command} team.", "content")
        type_with_effect("\n\n", "typing")
        search_entry.delete(3, END)  # Maintain a gap between responses
    elif command == "clear":
        terminal.config(state=NORMAL)
        terminal.delete("2.0", END)
        terminal.config(state=DISABLED)
        search_entry.delete(3, END)
      # Remove the command "clear;" from the entry
    elif command.islower():
        player_data = [p for p in team_data[current_team] if p['name'].lower().startswith(command)]
        if player_data:
            type_with_effect("\nCommand passed: fc ", "output")
            type_with_effect(command + ";", "command")
            type_with_effect("\n\n", "typing")  # Maintain a gap between responses
            type_with_effect("Player data:\n", "heading")
            type_with_effect(player_data[0]['name'] + "\n", "table_data")
            type_with_effect(player_data[0]['essay'] + "\n", "content")
            type_with_effect("\n\n", "typing")  # Maintain a gap between responses
        else:
            type_with_effect("\nCommand passed: fc ", "output")
            type_with_effect(command + ";", "command")
            type_with_effect("\n\n", "typing")  # Maintain a gap between responses
            type_with_effect("Player not found.", "error")
            type_with_effect("\n\n", "typing")  # Maintain a gap between responses
        search_entry.delete(3, END)
    else:
        type_with_effect("Invalid command.", "error")
        type_with_effect("\n\n", "typing")  # Maintain a gap between responses
        search_entry.delete(3, END)


terminal_window = Tk()
terminal_window.title("FootBot Terminal")
terminal_window.configure(bg="#f2f2f2")

window_width = 720
window_height = 320
screen_width = 1366
screen_height = 768
x = ((screen_width - window_width) // 2) + 60
y = ((screen_height - window_height) // 2) - 108

terminal_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

terminal_frame = Frame(terminal_window, bg="#f2f2f2")
terminal_frame.pack(fill=BOTH, expand=True)

search_entry = Entry(terminal_frame, font=("Tahoma", 12), bg="#f2f2f2", fg="black", insertbackground="black")
search_entry.pack(side=BOTTOM, padx=10, pady=10, fill=X, expand=True)
search_entry.bind("<Return>", on_search)
search_entry.insert(0, "fc ")

terminal = Text(terminal_frame, font=("Tahoma", 12), bg="#f2f2f2", fg="blue", wrap=WORD, state=DISABLED)
terminal.pack(padx=10, pady=10, fill=BOTH, expand=True)
terminal.tag_configure("typing", foreground="#333333", font = ("Tahoma", 12))
terminal.tag_configure("heading", foreground="#800020", font = ("Nunito", 12, "bold"))
terminal.tag_configure("table_data", foreground="green")
terminal.tag_configure("content", foreground="#545454")
terminal.tag_configure("error", foreground="red")
terminal.tag_configure("command", foreground="#800080")
terminal.tag_configure("output", foreground="#006400")

type_with_effect("Welcome to the FootBot Terminal!\n", "content")
type_with_effect("\nWhere you can view information of Teams and Players using some FootBot commands.\n", "content")
type_with_effect("\nFOOTBOT COMMANDS:\n", "content")
type_with_effect("\nCommand 1 : fc teamname;\n", "content")
type_with_effect("\nExample : fc churchboys;\n", "content")
type_with_effect("\n• This command can be used to get into a team for further exploration.\n", "content")
type_with_effect("\nCommand 2 : fc showdata;\n", "content")
type_with_effect("\nExample : fc showdata;\n", "content")
type_with_effect("\n• This command allows you to view all the information related to that sepcific team.\n", "content")
type_with_effect("\nCommand 3 : fc player name;\n", "content")
type_with_effect("\nExample : fc ananta;\n", "content")
type_with_effect("\n• This command allows you to view the personal details realted to that specific person.\n", "content")
type_with_effect("\nCommand 4 : fc clear;\n", "content")
type_with_effect("\n• This command allows you to clear the terminal if you find it overwhelming.\n", "content")



terminal_window.mainloop()
