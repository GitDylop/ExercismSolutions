def gamestate(board):
    wins = 0
    # Rows
    for row in range(3):
        if board[row][0] == board[row][1] and board[row][1] == board[row][2] and board[row][0] != " ":
            wins += 1
            
    if wins > 1:
        raise ValueError("Impossible board: game should have ended after the game was won")
    elif wins > 0:
        return "win"

    wins = 0

    # Columns
    for column in range(3):
        if board[0][column] == board[1][column] and board[1][column] == board[2][column] and board[0][column] != " ":
            wins += 1

    if wins > 1:
        raise ValueError("Impossible board: game should have ended after the game was won")
    elif wins > 0:
        return "win"

    wins = 0

    # Diagonal
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != " ":
        wins += 1
    if board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] != " ":
        wins += 1

    if wins > 0:
        return "win"


    x = 0
    o = 0
    isongoing = False
    # Is game ongoing
    for row in board:
        for cell in row:
            if cell == "X":
                x += 1
            elif cell == "O":
                o += 1
            
            if cell == " ":
                isongoing = True

    if o > x:
        raise ValueError("Wrong turn order: O started")
    elif x > o + 1:
        raise ValueError("Wrong turn order: X went twice")

    if isongoing:
        return "ongoing"
    return "draw"
