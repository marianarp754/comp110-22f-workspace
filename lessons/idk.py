def triangular(n: int) -> int:
    """Takes an integer, n, and returns the nth triangular number."""
    n = n * (n + 1) // 2
    return n


def sumupto(input: int) -> int:
    """Takes a positive integer, n, and returns the sum."""
    total: int = 0
    for number in range(1, input + 1):
        total = total + number
    return total


def sumpower(n: int, k: int) -> int:
    """Takes integers, n and k, and returns the sum of the kth powers of the first n positve integers."""
    i: int = 0
    for number in range(1, n + 1):
        i = i + number ** k
    return i


print("Problem #1")
n: int = 100
print(n)
print(triangular(n))
print(sumupto(n))

print("Problem #2")
# I have no idea what a conjecture is. I'm not sure what you're supposed to put here but I did notice that Sn and Tn return the same number 
# when they are given the same number for n and input. 

print("Problem #3")
print(triangular(20) + triangular(19))
# I did notice that in this problem of Tn + Tn-1 it will always equal the square of Tn

print("Problem #4")
print(sumpower(2016, 5))

print("Problem #5")
print(sumpower(100, -2))
print("This computes a number that is very similar to pi squared over six.")

print("Problem #6")
print(sumpower(500, -2))
print(sumpower(5000, -2))
print(sumpower(50000, -2))
print("It is reasonable guess that the work done above is equal to pi squared over six because as n gets infinitely large, it will always equal pi squared over six.")