from dotenv import load_dotenv
import os
import google.generativeai as genai
from prompt_utils import clean_prompt

# Load .env variables
load_dotenv()
with open("log.txt", "a") as f:
    f.write("Loaded GEMINI_API_KEY: " + str(os.getenv("GEMINI_API_KEY")) + "\n")
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")


#all bot logic 

def get_bot_response(user_input):
    try:
        prompt = clean_prompt(user_input)
        with open("log.txt", "a") as f:
            f.write("[DEBUG] Final Prompt: " + prompt + "\n")
        response = model.generate_content(prompt)
        if response and hasattr(response, "text"):
            return response.text if response.text.strip() else "[I didn't get that.]"
        else:
            return "[I didn't get that.]"
    except Exception as e:
        with open("log.txt", "a") as f:
            f.write("[ERROR] " + str(e) + "\n")
        return "[Oops! Something broke.]"
