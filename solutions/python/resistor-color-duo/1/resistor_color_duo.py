def value(colors):
    colorList = [
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

    return int(str(colorList.index(colors[0])) + str(colorList.index(colors[1])))
