"""EX03 - Structured Wordle."""

__author__ = "730576205"


def contains_char(char_word: str, single_char: str) -> bool:
    """If single_char is found at any index of char_word."""
    assert len(single_char) == 1
    i: int = 0
    while i < len(char_word): 
        if char_word[i] == single_char:
            return True
        i = i + 1
    return False


def emojified(guess_word: str, secret_word: str) -> str:
    """Returning a string of emoji."""
    assert len(guess_word) == len(secret_word)
    white_box: str = "\U00002B1C"
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"
    emoji_boxes: str = ""
    idx: int = 0
    while idx < len(guess_word):
        if guess_word[idx] == secret_word[idx]:
            emoji_boxes = emoji_boxes + green_box
        else: 
            if contains_char(secret_word, guess_word[idx]) is True:
                emoji_boxes = emoji_boxes + yellow_box
            else:
                emoji_boxes = emoji_boxes + white_box
        idx = idx + 1
    return emoji_boxes


def input_guess(guess_word_length: int) -> str:
    """Prompting the user for a guess."""
    user_guess: str = input("Enter a " + str(guess_word_length) + " character word: ")
    while guess_word_length != len(user_guess):
        user_guess = input("That wasn't " + str(guess_word_length) + " chars! Try again: ")
    return user_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    the_secret_word: str = "codes" 
    turn_number: int = 1
    b_var: bool = False
    while not b_var and turn_number <= 6:
        print("=== Turn " + str(turn_number) + "/6 ===")
        the_guess_word: str = input_guess(5)
        the_emoji_boxes: str = emojified(the_guess_word, the_secret_word)
        if the_secret_word == the_guess_word:
            print(the_emoji_boxes)
            print("You won in " + str(turn_number) + "/6 turns!")
            b_var = True
        else:
            if turn_number == 6:
                print("X/6 - Sorry, try again tomorrow!")
            else:
                print(the_emoji_boxes)
        turn_number = turn_number + 1


if __name__ == "__main__":
    main()