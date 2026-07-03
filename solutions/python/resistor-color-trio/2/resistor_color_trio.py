def label(colors):
    color_list = [
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

    ohms = int(str(color_list.index(colors[0])) + str(color_list.index(colors[1]))) * (10 ** color_list.index(colors[2]))

    if ohms > 1000000000:
        return f"{int(ohms / 1000000000)} gigaohms"
    elif ohms > 1000000:
        return f"{int(ohms / 1000000)} megaohms"
    elif ohms > 1000:
        return f"{int(ohms / 1000)} kiloohms"
    else:
        return f"{int(ohms)} ohms"
