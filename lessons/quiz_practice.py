"""Sam Coding Help."""


print("Question 1")
i: int = 1
while i < 21:
    square_root = i**2
    print(square_root)
    i = i + 1


print("Question 2")
i: int = 1
while i < 21:
    square_root = i**2
    if len(str(square_root)) == 1:
        print(square_root)
    else:
        print(str(square_root)[len(str(square_root)) - 1])
    i = i + 1


print("Question 4")
print("Beginning Verification...")
i: int = 1
for i in range(1,10000):
    square_root = i**2
    if len(str(square_root)) == 1:
        if square_root == 2:
            print("Conjecture is false!")
        if square_root == 3:
            print("Conjecture is false!")
        if square_root == 7:
            print("Conjecture is false!")
        if square_root == 8:
            print("Conjecture is false!")
    else:
        if str(square_root)[len(str(square_root)) - 1] == 2:
            print("Conjecture is false!")
        if str(square_root)[len(str(square_root)) - 1] == 3:
            print("Conjecture is false!")
        if str(square_root)[len(str(square_root)) - 1] == 7:
            print("Conjecture is false!")
        if str(square_root)[len(str(square_root)) - 1] == 8:
            print("Conjecture is false!")
    i = i + 1
print("Verification Complete.")