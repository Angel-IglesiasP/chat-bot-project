import os      # For working with file paths
import sys     # To detect if we're running as a PyInstaller executable
import random  # For selecting random sprites by mood


# === Load all sprite image paths into a dictionary ===
def load_sprite_variants():
    # Determine base path depending on execution context (script vs. .exe)
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS  # Path for PyInstaller bundled app
    else:
        base_path = os.path.abspath(".")

    sprite_folder = os.path.join(base_path, "assets", "sprites")
    sprite_dict = {}

    # Loop through files in the sprites folder
    for filename in os.listdir(sprite_folder):
        if filename.endswith((".png", ".gif", ".jpg")):
            sprite_name = os.path.splitext(filename)[0]  # e.g., "happy1"
            sprite_path = os.path.join(sprite_folder, filename)
            sprite_dict[sprite_name] = sprite_path

    return sprite_dict


# === Return a sprite path based on detected mood ===
def get_sprite_for_mood(mood, sprite_dict):
    # Find all sprite entries that match the mood prefix (e.g., "happy1", "happy2", etc.)
    matching_sprites = [
        path for name, path in sprite_dict.items()
        if name.startswith(mood)
    ]

    if matching_sprites:
        return random.choice(matching_sprites)
    else:
        # Fallback to error sprite if no match is found
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, "assets", "sprites", "error.png")
