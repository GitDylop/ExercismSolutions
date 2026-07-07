def rows(letter):
    alphabeth = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    diamond = []
    row = ""

    letter_index = alphabeth.index(letter)

    # First row
    for _ in range(letter_index):
        row += " "

    row += alphabeth[0]

    for _ in range(letter_index):
        row += " "

    diamond.append(row)
    row = ""


    # Start
    for row_idx in range(letter_index):
        for _ in range(letter_index - 1 - row_idx):
            row += " "
    
        row += alphabeth[row_idx + 1]
    
        for _ in range(row_idx*2 + 1):
            row += " "
    
        row += alphabeth[row_idx + 1]
    
        for _ in range(letter_index - 1 - row_idx):
            row += " "
    
        diamond.append(row)
        row = ""

    # End
    for row_idx in range(letter_index - 1):
        for _ in range(row_idx + 1):
            row += " "
    
        row += alphabeth[letter_index - row_idx - 1]
    
        for _ in range((letter_index-1)*2 - row_idx*2 - 1):
            row += " "
    
        row += alphabeth[letter_index - row_idx - 1]
    
        for _ in range(row_idx + 1):
            row += " "
    
        diamond.append(row)
        row = ""
    
    # Last row
    if letter_index > 0:
        for _ in range(letter_index):
            row += " "

        row += alphabeth[0]

        for _ in range(letter_index):
            row += " "

        diamond.append(row)
        row = ""

    return diamond