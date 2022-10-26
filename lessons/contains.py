"""Example implementing a list utility function."""

#function name: contains
#we will have 2 parameters: needle(str), haystack (list[str])
#return type bool
def contains(needle: str, haystack: (list[str])) -> bool:
#gameplan:
    #1. start with the first index
    i: int = 0
    #2. loop through every index
    while i < len(haystack):
       #2. a.Test if item at idex equal to needle
        if haystack[i] == needle:
           #2. a.True return true! we found it!
            return True
        i = i + 1
    #3. return false
    return False