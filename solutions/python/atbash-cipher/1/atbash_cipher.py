plain = "abcdefghijklmnopqrstuvwxyz"
cipher = "zyxwvutsrqponmlkjihgfedcba"

def encode(plain_text):
    encoded_text = ""
    group_size = 0
    
    for symbol in plain_text:
        index = plain.find(symbol.lower())

        if symbol.isalpha() or symbol.isdigit():
            if group_size == 5:
                group_size = 1
                encoded_text += " "
            else:
                group_size += 1
            
        if index > -1:
            encoded_text += cipher[index]
        elif symbol.isdigit():
            encoded_text += symbol

    return encoded_text

def decode(ciphered_text):
    decoded_text = ""
    
    for symbol in ciphered_text:
        if symbol == " ":
            continue
            
        index = cipher.find(symbol.lower())
        
        if index > -1:
            decoded_text += plain[index]
        else:
            decoded_text += symbol

    return decoded_text
