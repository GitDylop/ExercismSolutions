def is_isogram(string):
    upperString = string.upper()
    for i in range(len(upperString)):
        if upperString[i] in "- ":
            continue
        for j in range(len(upperString)):
            if upperString[j] in "- ":
                continue
            if upperString[j] == upperString[i] and j != i:
                return False
    return True

print(is_isogram("six-year-old"))