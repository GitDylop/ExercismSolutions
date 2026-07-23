def convert(input_grid):
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    if len(input_grid[0]) % 3 != 0:
        raise ValueError("Number of input columns is not a multiple of three")

    output = ""

    numbers = [
        [
            " _ ",
            "| |",
            "|_|",
            "   "
        ],[
            "   ",
            "  |",
            "  |",
            "   "
        ],[
            " _ ",
            " _|",
            "|_ ",
            "   "
        ],[
            " _ ",
            " _|",
            " _|",
            "   "
        ],[
            "   ",
            "|_|",
            "  |",
            "   "
        ],[
            " _ ",
            "|_ ",
            " _|",
            "   "
        ],[
            " _ ",
            "|_ ",
            "|_|",
            "   "
        ],[
            " _ ",
            "  |",
            "  |",
            "   "
        ],[
            " _ ",
            "|_|",
            "|_|",
            "   "
        ],[
            " _ ",
            "|_|",
            " _|",
            "   "
        ],
    ]

    for j in range(int(len(input_grid) / 4)):
        if j > 0:
            output += ","
            
        for i in range(int(len(input_grid[0]) / 3)):
            number = []
            for row in range(4):
                number.append(input_grid[row+j*4][i*3:i*3+3])
    
            print(*number, sep="\n")
            if number in numbers:
                output += f"{numbers.index(number)}"
            else:
                output += "?"
            

    return output