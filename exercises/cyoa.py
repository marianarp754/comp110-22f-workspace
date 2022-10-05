"""EX06 - Choose Your Own Adventure."""

__author__ = "730576205"

from random import randint

points: int = 0
num_turns: int = 1
player: str = ''
the_number: int = randint(1, 20)
the_number_2: int = randint(21, 40)
the_number_3: int = randint(41, 60)


def main() -> None:
    """Entrance to function."""
    global points
    global num_turns
    global the_number
    global the_number_2
    global the_number_3
    greet()
    the_question: str = input("Do you want to guess a number between 1-20, 21-40, or 41-60? ")
    if the_question == "1-20":
        if points == 0:
            points = points + 1
        points = the_real_number(number_guess(), points)
    if the_question == "21-40":
        if points == 0:
            points = points + 1
        the_real_number_2(number_guess_2())
    if the_question == "41-60":
        if points == 0:
            points = points + 1
        the_real_number_3(number_guess_3())
    play_again: str = input("Do you want to play again? Yes or No. ")
    if play_again == "Yes":
        points = points + 1
        num_turns = 1
        the_number = randint(1, 20)
        the_number_2 = randint(21, 40)
        the_number_3 = randint(41, 60)
        main()
    else: 
        print(f"You played the game {points} times!")
        print("Thank you for playing! Bye!")


def greet() -> None:
    """Say hello."""
    global player
    print("Welcome to The Number Guessing Game.")
    player = input("What is your name? ")


def number_guess() -> int:
    """Take in guess."""
    print(f"=== Turn {num_turns}/20 ===")
    if num_turns == 1:
        the_guess: str = input(f"Hi {player}! Guess a number between 1-20. ")
    else:
        the_guess = input("Guess a number between 1-20. ")
    return int(the_guess)


def number_guess_2() -> int:
    """Take in guess."""
    print(f"=== Turn {num_turns}/20 ===")
    if num_turns == 1:
        the_guess_2: str = input(f"Hi {player}! Guess a number between 21-40. ")
    else:
        the_guess_2 = input("Guess a number between 21-40. ")
    return int(the_guess_2)


def number_guess_3() -> int:
    """Take in guess."""
    print(f"=== Turn {num_turns}/20 ===")
    if num_turns == 1:
        the_guess_3: str = input(f"Hi {player}! Guess a number between 41-60. ")
    else:
        the_guess_3 = input("Guess a number between 41-60. ")
    return int(the_guess_3)


def the_real_number(the_integer: int, point: int) -> int:
    """Check if guess is correct, otherwise try again."""
    global num_turns
    global the_number
    NAMED_CONSTANT_1: str = "\U0001F600"
    NAMED_CONSTANT_2: str = "\U0001F603"
    NAMED_CONSTANT_3: str = "\U0001F604"
    NAMED_CONSTANT_4: str = "\U0001F601"
    NAMED_CONSTANT_5: str = "\U0001F606"
    if the_integer == the_number:
        print(f"YOU GOT IT!!!!!{NAMED_CONSTANT_1}{NAMED_CONSTANT_2}{NAMED_CONSTANT_3}{NAMED_CONSTANT_4}{NAMED_CONSTANT_5}")
        print(f"Congrats, it took you {num_turns} tries until you guessed correctly!")
    else:
        if num_turns < 20:
            print("Sorry, try again.")
            num_turns = num_turns + 1
            return the_real_number(number_guess(), point)
        else:
            print("=== Turn X/20 ===")
            print("Sorry you have ran out of tries.")
    return point


def the_real_number_2(the_integer: int) -> None:
    """Check if guess is correct, otherwise try again."""
    global num_turns
    global the_number_2
    global points
    NAMED_CONSTANT_1: str = "\U0001F600"
    NAMED_CONSTANT_2: str = "\U0001F603"
    NAMED_CONSTANT_3: str = "\U0001F604"
    NAMED_CONSTANT_4: str = "\U0001F601"
    NAMED_CONSTANT_5: str = "\U0001F606"
    if the_integer == the_number_2:
        print(f"YOU GOT IT!!!!!{NAMED_CONSTANT_1}{NAMED_CONSTANT_2}{NAMED_CONSTANT_3}{NAMED_CONSTANT_4}{NAMED_CONSTANT_5}")
        print(f"Congrats, it took you {num_turns} tries until you guessed correctly!")
    else:
        if num_turns < 20:
            print("Sorry, try again.")
            num_turns = num_turns + 1
            return the_real_number_2(number_guess_2())
        else:
            print("=== Turn X/20 ===")
            print("Sorry you have ran out of tries.")


def the_real_number_3(the_integer: int) -> None:
    """Check if guess is correct, otherwise try again."""
    global num_turns
    global the_number_3
    global points
    NAMED_CONSTANT_1: str = "\U0001F600"
    NAMED_CONSTANT_2: str = "\U0001F603"
    NAMED_CONSTANT_3: str = "\U0001F604"
    NAMED_CONSTANT_4: str = "\U0001F601"
    NAMED_CONSTANT_5: str = "\U0001F606"
    if the_integer == the_number_3:
        print(f"YOU GOT IT!!!!!{NAMED_CONSTANT_1}{NAMED_CONSTANT_2}{NAMED_CONSTANT_3}{NAMED_CONSTANT_4}{NAMED_CONSTANT_5}")
        print(f"Congrats, it took you {num_turns} tries until you guessed correctly!")
    else:
        if num_turns < 20:
            print("Sorry, try again.")
            num_turns = num_turns + 1
            return the_real_number_3(number_guess_3())
        else:
            print("=== Turn X/20 ===")
            print("Sorry you have ran out of tries.")
            

if __name__ == "__main__":
    main()