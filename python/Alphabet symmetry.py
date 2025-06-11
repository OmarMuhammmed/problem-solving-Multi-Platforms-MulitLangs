# https://www.codewars.com/kata/59d9ff9f7905dfeed50000b0/train/python


def solve(strings: list[str]) -> list[int]:
    result = []

    for word in strings:
        counter = 0
        for i, char in enumerate(word):
            if ord(char.lower()) - ord('a') == i:
                counter += 1
        result.append(counter)

    return result
