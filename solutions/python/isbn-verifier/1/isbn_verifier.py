def is_valid(isbn):
    isbn = isbn.replace("-", "")
    
    if len(isbn) != 10:
        return False
    
    number = 0
    for i in range(9):
        if not isbn[i].isdigit():
            return False
        number += int(isbn[i]) * (10 - i)
    
    if isbn[9] == "X":
        number += 10
    elif isbn[9].isdigit():
        number += int(isbn[9])
    else:
        return False
    
    return number % 11 == 0