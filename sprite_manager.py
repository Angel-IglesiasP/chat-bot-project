import os #gives me access to read the image folder for the sprites
import random #I will use this to select a random sprite from all the images i made

#load all the sprites files from the path folder 
def load_sprite_variants(path="assets/sprites"):
    sprite_dict = {} #empty diccionary to store all the sprites 

#go thru the path to get each file in the folder
    for filename in os.listdir(path):           #-------------NEED TO CONNECT PATH ONCE I HAVE ALL THE IMAGES-------------
        if filename.endswith(".png", ".gif"):
            mood = ''.join(filter(str.isalpha, filename))   #basically filters all images by name (happy1, happy2, happy3, etc) takes the number and the file extension out and match it with the emotion with the same name

            #hust in case to handle other mood that I might create later.
            if mood not in sprite_dict:
                sprite_dict[mood] = []

            #dd the full file path of this sprite to the moods list
            sprite_dict[mood].append(os.path.join(path, filename))          #-------------NEED TO CONNECT PATH ONCE I HAVE ALL THE IMAGES-------------

    #returns the mood sprite diccionary
    return sprite_dict

#check the dictionary and return a matching sprite
def get_sprite_for_mood(mood, sprite_dict):
    #if we have this emotion, choose one ramdonly 
    if mood in sprite_dict:
        return random.choice(sprite_dict[mood])
    else:
        return "assets/sprites/error.png" #handles erros. if emotion not found display error image