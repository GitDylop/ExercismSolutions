def encode(numbers):
    encoded_bytes = []
    for number in numbers:
        if number == 0:
            encoded_bytes.append(0)
            continue
        
        temp_bytes = []
        while number > 0:
            temp_bytes.append(number & 0x7F)
            number >>= 7
            
        for i in range(1, len(temp_bytes)):
            temp_bytes[i] |= 0x80
            
        encoded_bytes.extend(reversed(temp_bytes))
        
    return encoded_bytes


def decode(bytes_):
    decoded_numbers = []
    current_number = 0
    
    for i, byte in enumerate(bytes_):
        current_number = (current_number << 7) | (byte & 0x7F)
        
        if (byte & 0x80) == 0:
            decoded_numbers.append(current_number)
            current_number = 0
        elif i == len(bytes_) - 1:
            raise ValueError("incomplete sequence")
            
    return decoded_numbers