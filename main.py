#imports all functions from all other files
from chatbot_logic import get_bot_response
from mood_detector import detect_mood
from sprite_manager import load_sprite_variants, get_sprite_for_mood
from PIL import Image, ImageTk
import tkinter as tk
import os 

# Load all the sprits into a dictionary before starting 
sprite_dict = load_sprite_variants()
special_sprites = { #handles special images that are not associated with the emotions
    "welcome": "assets/sprites/talking.gif",
    "loading": "assets/sprites/loading.gif",
    "error": "assets/sprites/error.png"
}

#creates a window with tkinter
sprite_window = tk.Tk()
sprite_window.title("Bot Reaction")

# creates a label to hold the images
image_label = tk.Label(sprite_window)
image_label.pack()


#new function to displays imags using Tkinter framework
def show_sprite(sprite_path):

    # Open the image
    img = Image.open(sprite_path)
    img = img.resize((256, 256))  # resize if needed

    # converts images to a format tkinter can use
    tk_img = ImageTk.PhotoImage(img)

    # create a label to hold the image so it doesn't disapear 
    image_label.config(image=tk_img)
    image_label.image = tk_img

#----------------------------------------------#
#function to process input and update images
def handle_input(user):
    if user.lower() in ["exit", "quit"]: #to get out of the application 
        show_sprite(special_sprites.get("goodbye", special_sprites["talking"]))
        sprite_window.destroy() #eliminates the sprites
        return False
    show_sprite(special_sprites["loading"]) # shows a gif loading

    try:
        response = get_bot_response(user) #call all the funcitons from the other files to get bot response from API, detect the mood with Vader and get the sprites
        mood = detect_mood(user)
        sprite_path = get_sprite_for_mood(mood, sprite_dict)

        print("Bot:", response) #DELETE LATER TESTING
        print("Mood Detected:", mood) #DELETE LATER TESTING
        show_sprite(sprite_path)

    except Exception as e:
        print("ERROR:", e)
        show_sprite(special_sprites["error"])
    return True

#------------------------------------#
# chat loop
def chat_loop():
    while True:
        user = input("You: ")
        if not handle_input(user):
            break

# start the chatbot loop in a separate thread so Tkinter window stays open
import threading
threading.Thread(target=chat_loop, daemon=True).start()

# Sstart the GUI loo[]
sprite_window.mainloop()