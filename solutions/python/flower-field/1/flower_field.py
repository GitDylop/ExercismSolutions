def annotate(garden):
    marked_garden = []

    # Check if board is valid
    for row in garden:
        if len(row) != len(garden[0]):
            raise ValueError("The board is invalid with current input.")

        # Check for invalid characters
        for cell in row:
            if not(cell in [' ', '*']):
                raise ValueError("The board is invalid with current input.")

    # Look for flowers
    for row in range(len(garden)):
        new_row = ""
        for cell in range(len(garden[row])):
            if garden[row][cell] == ' ':
                flower_count = 0
                
                for r_offset in [-1, 0, 1]:
                    for c_offset in [-1, 0, 1]:
                        if r_offset == 0 and c_offset == 0:
                            continue
                            
                        r, c = row + r_offset, cell + c_offset
                        
                        if 0 <= r < len(garden) and 0 <= c < len(garden[row]):
                            if garden[r][c] == '*':
                                flower_count += 1
                                
                new_row += str(flower_count) if flower_count > 0 else " "
            else:
                new_row += garden[row][cell]
                
        marked_garden.append(new_row)

    return marked_garden