def reverse_multiply(a_list: list[int]) -> list[int]:
    result: list[int] = []
    i: int = 1
    idx: int = 0
    while idx < len(a_list):
        result.append(a_list[len(a_list) - i] * 2)
        i = i + 1
        idx = idx + 1
    return result

#print(reverse_multiply([1, 2, 3]))

def free_biscuits(a_dict: dict[str, list[int]]) -> dict[str, bool]:
    result: dict[str, bool] = {}
    for key in a_dict:
        i: int = 0
        sum: int = 0
        while i < len(a_dict[key]):
            sum = sum + a_dict[key][i]
            i = i + 1
        if sum >= 100:
            result[key] = True
        else:
            result[key] = False
    return result

#print(free_biscuits({"UNCvsDuke": [38, 20, 42], "UNCvsState": [9, 51, 16, 23]}))

def multiples(a_list: list[int]) -> list[bool]:
    result: list[bool] = []
    i: int = 0
    if a_list[i] % a_list[len(a_list) - 1] == 0:
        result.append(True)
    else:
        result.append(False)
    idx: int = 1
    while idx < len(a_list):
        if a_list[idx] % a_list[i] == 0:
            result.append(True)
        else:
            result.append(False)
        idx = idx + 1
        i = i + 1
    return result

#print(multiples([2, 3, 4, 8, 16, 2, 4, 2]))

def merge_lists(list_str: list[str], list_int: list[int]) -> dict[str, int]:
    result: dict[str, int] = {}
    if len(list_int) != len(list_str):
        return result
    else:
        i: int = 0
        while i < len(list_str):
            result[list_str[i]] = list_int[i]
            i = i + 1
        return result

#print(merge_lists(["blue", "yellow", "red"], [5, 2, 4]))

def reverse_string(word: str) -> str:
    result: str = ""
    a_list: list[str] = []
    for letter in word:
        a_list.append(letter)
    i: int = 1
    idx: int = 0
    while idx < len(a_list):
        result = result + a_list[len(a_list) - i]
        i = i + 1
        idx = idx + 1
    return result

#print(reverse_string("mariana"))

def factorial(num: int) -> int:
    if num == 1:
        return num
    else:
        return(num * factorial(num - 1))

#print(factorial(5))

def main() -> None:
    print(points)

points: int = 0
main()