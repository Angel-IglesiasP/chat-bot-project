#imports all functions from all other files
from chatbot_logic import get_bot_response
from mood_detector import detect_mood
from sprite_manager import load_sprite_variants, get_sprite_for_mood
from PIL import Image, ImageTk
import tkinter as tk
from itertools import count
from PIL import ImageSequence
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


# Global variables to manage GIF animation
frames = []
frame_index = 0
after_id = None  # Track the current running animation loop

#new function to displays imags using Tkinter framework
def show_sprite(sprite_path):
    global frames, frame_index, after_id #keep track of the frames for GIFs

    # cancel previous animation if any
    if after_id is not None:
        sprite_window.after_cancel(after_id)
        after_id = None

    img = Image.open(sprite_path) #open path folder

    if getattr(img, "is_animated", False):  # Check if it is a GIF (it is pronounced GIF! )
        frames = [ImageTk.PhotoImage(frame.copy().resize((256, 256))) for frame in ImageSequence.Iterator(img)] #if it is, load and resize each frame of the GIF
        frame_index = 0 #starts with the first sprite in the gif animation

        def update_frame(): #function to keep updating the image frame to create the animation
            global frame_index, after_id # Shows the current frame
            image_label.config(image=frames[frame_index])
            image_label.image = frames[frame_index] # Keeps a reference so the image doesn't disappear
            frame_index = (frame_index + 1) % len(frames)  # moved to the next frame
            after_id = sprite_window.after(300, update_frame)  # adjust 100 for frame delay

        update_frame() # starts the animation

    else:
        img = img.resize((256, 256))  # resize if needed
        tk_img = ImageTk.PhotoImage(img)    # converts images to a format tkinter can use
        image_label.config(image=tk_img)# create a label to hold the image so it doesn't disapear 
        image_label.image = tk_img


#----------------------------------------------#
#function to process input and update images
def handle_input(user):
    if user.lower() in ["exit", "quit"]: #to get out of the application 
        show_sprite(special_sprites.get("goodbye", special_sprites["talking"]))
        sprite_window.destroy() #eliminates the sprites
        return False
    
    try:
        show_sprite(special_sprites["loading"]) # shows a gif loading
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
show_sprite(special_sprites["welcome"])
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