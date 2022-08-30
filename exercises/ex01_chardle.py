"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730576205"

word: str = input("Enter a 5-character word: ")
int_count: int = 0

if len(word) == 5: 
    letter: str = input("Enter a single letter: ")
    if len(letter) == 1: 
        print("Searching for " + letter + " in " + word)
        if letter == word[0]: 
            int_count = int_count + 1
            print(letter + " found at index 0")
        if letter == word[1]:
            int_count = int_count + 1
            print(letter + " found at index 1")
        if letter == word[2]: 
            int_count = int_count + 1
            print(letter + " found at index 2")
        if letter == word[3]:
            int_count = int_count + 1
            print(letter + " found at index 3")
        if letter == word[4]:
            int_count = int_count + 1
            print(letter + " found at index 4")
        if int_count == 0: 
            print("No instances of " + letter + " found in " + word)
        if int_count == 1: 
            print("1 instance of " + letter + " found in " + word)
        if int_count == 2: 
            print("2 instances of " + letter + " found in " + word)
        if int_count == 3: 
            print("3 instances of " + letter + " found in " + word)
        if int_count == 4: 
            print("4 instances of " + letter + " found in " + word)
        if int_count == 5: 
            print("5 instances of " + letter + " found in " + word)
    else: 
        print("Error: Character must be a single character.")
        exit()
else: 
    print("Error: Word must contain 5 characters")
    exit()