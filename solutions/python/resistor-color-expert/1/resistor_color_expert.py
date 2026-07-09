def clean_number(num):
    if num == int(num):
        return int(num)
    return num

def resistor_label(colors):
    color_values = [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white"
    ]

    tolerance = {
        "grey": 0.05,
        "violet": 0.1,
        "blue": 0.25,
        "green": 0.5,
        "brown": 1,
        "red": 2,
        "gold": 5,
        "silver": 10
    }
    
    if len(colors) == 1:
        return f"{color_values.index(colors[0])} ohms"
    elif len(colors) == 4:
        value = ((color_values.index(colors[0]) * 10) + color_values.index(colors[1])) * (10 ** color_values.index(colors[2]))

        if value >= 1000000000:
            return f"{clean_number(value/1000000000)} gigaohms ±{tolerance[colors[3]]}%"
        elif value >= 1000000:
            return f"{clean_number(value/1000000)} megaohms ±{tolerance[colors[3]]}%"
        elif value >= 1000:
            return f"{clean_number(value/1000)} kiloohms ±{tolerance[colors[3]]}%"
        else:
            return f"{value} ohms ±{tolerance[colors[3]]}%"
    elif len(colors) == 5:
        value = ((color_values.index(colors[0]) * 100) + (color_values.index(colors[1]) * 10) + color_values.index(colors[2])) * (10 ** color_values.index(colors[3]))

        if value >= 1000000000:
            return f"{clean_number(value/1000000000)} gigaohms ±{tolerance[colors[4]]}%"
        elif value >= 1000000:
            return f"{clean_number(value/1000000)} megaohms ±{tolerance[colors[4]]}%"
        elif value >= 1000:
            return f"{clean_number(value/1000)} kiloohms ±{tolerance[colors[4]]}%"
        else:
            return f"{value} ohms ±{tolerance[colors[4]]}%"