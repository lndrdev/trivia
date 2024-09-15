import os
import time
import random
import json
import Levenshtein

black = "\033[1;30m"
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"
purple = "\033[1;35m"
cyan = "\033[1;36m"
white = "\033[1;37m"

def load_questions():
    with open('fragen.json', 'r', encoding='utf-8') as file:
        return json.load(file)

fragen = load_questions()

def color_code(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

gradient = [
    (255, 0, 0),   # Rot
    (255, 127, 0), # Orange
    (255, 255, 0)  # Gelb (optional)
]

banner_lines = [
    "_____._.______  .___ .___     .___ .______  ",
    "\\__ _:|: __   \\ : __|:   |___ : __|:      \\ ",
    "  |  :||  \\____|| : ||   |   || : ||   .   |",
    "  |   ||   :  \\ |   ||   :   ||   ||   :   |",
    "  |   ||   |___\\|   | \\      ||   ||___|   |",
    "  |___||___|    |___|  \\____/ |___|    |___|",
    "  Bist du wirklich so schlau, wie du denkst?   "
]

banner = ""
for i, line in enumerate(banner_lines):
    r = gradient[0][0] + (gradient[1][0] - gradient[0][0]) * (i / (len(banner_lines) - 1))
    g = gradient[0][1] + (gradient[1][1] - gradient[0][1]) * (i / (len(banner_lines) - 1))
    b = gradient[0][2] + (gradient[1][2] - gradient[0][2]) * (i / (len(banner_lines) - 1))
    
    banner += color_code(int(r), int(g), int(b)) + line + "\033[0m\n"

def get_mixed_questions():
    keys = list(fragen.keys())
    random.shuffle(keys)
    return keys

def main():
    mixed_questions = get_mixed_questions()
    for frage in mixed_questions:
        antwort = fragen[frage]
        os.system("cls")
        print(banner)
        print(f"{yellow}> {frage}{white}")

        x = input("--> ")
        distanz = Levenshtein.distance(x.lower(), antwort.lower())

        if x == "-":
            print(antwort)
        elif x.lower() == antwort.lower():
            print(f"\n{green}Das ist richtig! {white}🎉")
        elif distanz <= 3:
            print(f"\nDas ist nah genug dran! 👍\nRichtige Antwort: {antwort}")
        else:
            print(f"\n{red}Das ist leider falsch. :/{white}\nRichtige Antwort: {antwort}")

        time.sleep(5)

os.system("cls")
print("Hier kannst du testen, wie smart du bist!\nNein: Es gibt kein Subway Surfers Gameplay...")
time.sleep(3)
while True:
    main()