import tkinter as tk
from PIL import Image, ImageTk

def send():
    user_input = user_entry.get()
    chat_history.insert(tk.END, "You: " + user_input + "\n")
    user_entry.delete(0, tk.END)
    bot_response(user_input)

def bot_response(user_input):
    response = ""
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        response = "Hello! What's your name?"
    elif "my name is" in user_input:
        name = user_input.split("is")[-1].strip()
        response = f"Nice to meet you, {name}! How can I assist you today?"
    elif "how are you" in user_input:
        response = "I'm just a bot, but I'm here to help you!"
    elif "name" in user_input:
        response = "I am a simple chatbot created to demonstrate basic functionality."
    elif "bye" in user_input:
        response = "Goodbye! Have a great day!"
    elif "weather" in user_input:
        response = "I don't have real-time data, but you can check the weather on various weather websites!"
    elif "joke" in user_input:
        response = "Why don't scientists trust atoms? Because they make up everything!"
    elif "best movies" in user_input:
        response = "Here are some top movies you might enjoy:\n1. The Shawshank Redemption\n2. The Godfather\n3. The Dark Knight\n4. Forrest Gump\n5. Inception\n6. Spider-Man: Into the Spider-Verse(2018)\n7. The Trial of the Chicago 7 "
    elif "tourist places" in user_input:
        response = "Here are some top tourist places to visit:\n1. Paris, France\n2. Rome, Italy\n3. Kyoto, Japan\n4. New York, USA\n5. Sydney, Australia\n6. Cape Town, South Africa\n7. Barcelona, Spain"
    elif "books for class" in user_input:
        class_number = user_input.split("class")[-1].strip()
        if class_number.isdigit():
            response = f"Here are some recommended books for Class {class_number}:\n1. NCERT Textbooks\n2. Subject-specific guidebooks\n3. Reference books by R.D. Sharma and H.C. Verma"
        else:
            response = "Please specify the class number to get book recommendations."
    elif "exam preparation" in user_input:
        response = "Here are some recommended books for exam preparation:\n1. 'Objective General English' by S.P. Bakshi\n2. 'Quantitative Aptitude for Competitive Examinations' by R.S. Aggarwal\n3. 'General Knowledge 2024' by Manohar Pandey"
    elif "favorite food" in user_input or "food" in user_input:
        response = "I don't eat, but I can suggest some delicious dishes! How about trying pizza, sushi, or a fresh salad?"
    elif "hobby" in user_input or "hobbies" in user_input:
        response = "Hobbies are a great way to relax and enjoy your free time. Some popular hobbies include reading, painting, gardening, and cycling."
    elif "daily routine" in user_input or "routine" in user_input:
        response = "A good daily routine can help you stay organized and productive. Try starting your day with a healthy breakfast, some exercise, and a to-do list."
    elif "fitness tips" in user_input or "fitness" in user_input:
        response = "Fitness is important for a healthy life. Regular exercise, a balanced diet, and staying hydrated are key. Try to include both cardio and strength training in your routine."
    else:
        response = "I'm sorry, I don't understand that. Can you please rephrase?"

    chat_history.insert(tk.END, "Bot: " + response + "\n")

# Setting up the main window
root = tk.Tk()
root.title("Enhanced Chatbot")

# Centering the window on the screen
window_width = 500
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

# Adding a background image
background_image = Image.open("image.png")
background_image = background_image.resize((screen_width, screen_height))
background_photo = ImageTk.PhotoImage(background_image)

background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Creating a frame for better organization
frame = tk.Frame(root, bg="#282c34", bd=5)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Creating the chat history area with styling
chat_history = tk.Text(frame, bg="#1e1e1e", fg="#ffffff", width=70, height=30, wrap=tk.WORD, padx=20, pady=20, bd=2, relief="groove", font=("Arial", 12))
chat_history.pack(pady=20)

# Creating the user input area with styling
user_entry = tk.Entry(frame, bg="#1e1e1e", fg="#ffffff", width=50, insertbackground="#ffffff", bd=2, relief="groove", font=("Arial", 12))
user_entry.pack(side=tk.LEFT, padx=20)

# Creating the send button with styling
send_button = tk.Button(frame, text="Send", command=send, bg="#61afef", fg="#282c34", activebackground="#98c379", activeforeground="#282c34", bd=2, relief="raised", font=("Arial", 12))
send_button.pack(side=tk.LEFT, padx=20)

# Running the main loop
root.mainloop()
