#all bot logic 

#dummy test response. I will replace it with an API later to handle the user input.
def dummy_response(user_input): #defines a function that takes user input and answer vbased on that
    user_input = user_input.lower() #deals with upper cases 

    if "hello" in user_input:
        return "Hi there! I'm your digital buddy :)"
    elif "how are you" in user_input:
        return "I'm just pixels and code, but feeling pretty electric!"
    elif "bye" in user_input:
        return "See you later!"
    else:
        return None 
    
def get_bot_response(user_input):
    try:
        if not user_input.strip():
            return "[No input received.]" #deals with empty fields

#will be replace with API 
        response = dummy_response(user_input)
        return response if response else "[I didn't get that.]"

    except Exception as e: #in case API fails or error
        print("ERROR:", e)
        return "[Oops! Something broke.]"
    