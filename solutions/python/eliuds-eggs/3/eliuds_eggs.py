def egg_count(display_value):
    eggs = 0
    value = display_value
    for slot in range(31, -1, -1):
        if value >= 2**slot:
            value -= 2**slot
            eggs += 1

    return eggs