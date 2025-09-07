def rotate(text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    newText = ""
    
    for l in text:
        if l.lower() in alphabet:
            idx = alphabet.index(l.lower())
            rotated = alphabet[(idx + key) % 26]
            newText += rotated.upper() if l.isupper() else rotated
        else:
            newText += l
    
    return newText