def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    elif output_base < 2:
        raise ValueError("output base must be >= 2")
    
    number = 0
    for i, digit in enumerate(digits):
        if digit < 0 or digit >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
        number += digit * (input_base ** (len(digits) - 1 - i))
        
    if number == 0:
        return [0]
        
    output = []
    while number > 0:
        output.append(number % output_base)
        number //= output_base
        
    return output[::-1]