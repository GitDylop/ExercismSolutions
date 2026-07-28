def egg_count(display_value):
    eggs = 0
    value = display_value
    for i in range(31, -1, -1):
        if (value >= 2**i):
            value -= 2**i
            eggs += 1

    return eggs