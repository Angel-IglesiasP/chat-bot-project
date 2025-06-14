#import the mood detection library to help with slecting sprites.
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#creates and object class to analyzr text and return the right emotion
analyzer = SentimentIntensityAnalyzer()

#dictionary cointaining posibble emotion triggers to detect and find the right sprite to match the emotion
mood_keywords = {
    "happy": ["yay", "great", "awesome", "fun", "love", "cool", "this is good", "excited","maybe tomorrow", "i'll try", "one day", "i believe", "not giving up"],
    "sad": ["sad", "bad", "sorry", "hurt", "tired", "i guess", "maybe later", "i'll try again", "oh well", "meh", "sure", "ok", "fine", "idk", "i guess so", "doesn’t matter"],
    "angry": ["mad", "angry", "annoyed", "hate", "ugh", "whatever", "this sucks", "why bother"],
    "question": ["what", "why", "how", "when", "can you", "is it", "do you know"],
}

#function to read the line of text and returns the emotion category
def detect_mood(text):
    text = text.lower()
    mood_scores = {mood: 0 for mood in mood_keywords} #creates a dictionary to store how many keywords matches each emotion

    # simplle loop to count each emotion and match it the keywords in the text.
    for mood, phrases in mood_keywords.items():
        for phrase in phrases:
            if phrase in text:
                mood_scores[mood] += 1

    # Pick the highest scoring mood
    top_mood = max(mood_scores, key=mood_scores.get)

    # If no matches found, use vader to determine the most likely
    if mood_scores[top_mood] == 0:
        score = analyzer.polarity_scores(text)['compound'] # Compound score ranges from -1 (very negative) to +1 (very positive)

        # Decide mood based on the compound score
        if score >= 0.5:
            return "happy"
        elif score <= -0.5:
            return "sad"
        else:
            return "neutral" #in case emotion was not clear

 # Return the mood with the highest keyword match
    return top_mood