#imports all functions from all other files
from chatbot_logic import get_bot_response
from mood_detector import detect_mood
from sprite_manager import load_sprite_variants, get_sprite_for_mood

# Load all the sprits into a dictionary before starting 
sprite_dict = load_sprite_variants()

# chat loop
while True:
    # ask for input
    user = input("You: ")
    
    # check if the user wants to exit
    if user.lower() in ["exit", "quit"]:
        break

    # get bot response from logic file
    response = get_bot_response(user)

    # get mood from mood detector file
    mood = detect_mood(user)

    # get sprite from the sprote file
    sprite_path = get_sprite_for_mood(mood, sprite_dict)

    # output the results
    print("Bot:", response)
    print("Mood Detected:", mood)  # for testing DELETE
    print("Sprite Path:", sprite_path)  # for testing DELETE
