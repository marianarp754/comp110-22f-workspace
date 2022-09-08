"""EX02 - One-Shot Wordle."""

__author__ = "730576205"

secret_word: str = "python"
guess_word: str = input("What is your 6-letter guess? ")

white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"

i: int = 0
emoji_boxes: str = ""

while len(guess_word) != len(secret_word): 
    guess_word = input("That was not 6 letters! Try again: ")

if len(guess_word) == len(secret_word):
    if guess_word == secret_word:
        print(green_box + green_box + green_box + green_box + green_box + green_box)
        print("Woo! You got it!")
    else: 
        while i < len(secret_word):
            if guess_word[i] == secret_word[i]: 
                emoji_boxes = emoji_boxes + green_box
            else:
                b_var: bool = False
                idx: int = 0
                while not b_var and idx < len(secret_word): 
                    if guess_word[i] == secret_word[idx]:
                        b_var = True
                    idx = idx + 1
                if b_var is True: 
                    emoji_boxes = emoji_boxes + yellow_box
                else:
                    emoji_boxes = emoji_boxes + white_box
            i = i + 1
        print(emoji_boxes)
        print("Not quite. Play again soon!")