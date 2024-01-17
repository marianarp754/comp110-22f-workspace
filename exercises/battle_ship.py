"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730576205"

input_one: int = input("Pick a secret boat location between 1 and 4: ")
if input_one < 1:
    print("Error!" + input_one + "too low!")
    exit()
if input_one > 4:
    print("Error!" + input_one + "too high!")
    exit()

input_two: int = input("Guess a number between 1 and 4: ")
if input_two < 1:
    print("Error!" + input_two + "too low!")
    exit()
if input_two > 4:
    print("Error!" + input_two + "too high!")
    exit()

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
emoji_boxes: str = ""
result: str = ""

if input_one != input_two:
    result = result + WHITE_BOX
    if input_two == 1:
        emoji_boxes = emoji_boxes + result + BLUE_BOX + BLUE_BOX + BLUE_BOX
        print(emoji_boxes)
    if input_two == 2:
        emoji_boxes = emoji_boxes + BLUE_BOX + result + BLUE_BOX + BLUE_BOX
        print(emoji_boxes)
    if input_two == 3:
        emoji_boxes = emoji_boxes + BLUE_BOX + BLUE_BOX + result + BLUE_BOX
        print(emoji_boxes)
    if input_two == 4:
        emoji_boxes = emoji_boxes + BLUE_BOX + BLUE_BOX + BLUE_BOX + result
        print(emoji_boxes)


    print("Incorrect! You missed the ship.")
    exit()
else:
    result = result + RED_BOX
    if input_two == 1:
        emoji_boxes = emoji_boxes + result + BLUE_BOX + BLUE_BOX + BLUE_BOX
        print(emoji_boxes)
    if input_two == 2:
        emoji_boxes = emoji_boxes + BLUE_BOX + result + BLUE_BOX + BLUE_BOX
        print(emoji_boxes)
    if input_two == 3:
        emoji_boxes = emoji_boxes + BLUE_BOX + BLUE_BOX + result + BLUE_BOX
        print(emoji_boxes)
    if input_two == 4:
        emoji_boxes = emoji_boxes + BLUE_BOX + BLUE_BOX + BLUE_BOX + result
        print(emoji_boxes)
    print("Correct! You hit the ship!")
    exit()