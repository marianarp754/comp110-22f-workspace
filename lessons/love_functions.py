"""Some tendering, loving functions."""

from tkinter import N


def love(subject: str) -> str:
    """Given a subject as a parameter, returns a loving string."""
    return f"I love you {subject}!"

def spread_love(to: str, n: int) -> str: 
    """Generates a str repating a loving message n times."""
    love_note: str = ""
    counter_var: int = 0
    while counter_var <  n: 
        love_note += love(to) + "/n"
        counter_var = counter_var + 1
    return love_note