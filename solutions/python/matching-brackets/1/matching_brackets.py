def is_paired(input_string):
    PARENTHESES = 0
    BRACKETS = 1
    BRACES = 2
    
    depth = []
    
    for i in input_string:
        if i == '(':
            depth.append(PARENTHESES)
            
        elif i == ')':
            if len(depth) == 0:
                return False
                
            if depth[-1] == PARENTHESES:
                depth.pop(-1)
            else:
                return False
            
        elif i == '[':
            depth.append(BRACKETS)
            
        elif i == ']':
            if len(depth) == 0:
                return False
            
            if depth[-1] == BRACKETS:
                depth.pop(-1)
            else:
                return False
            
        elif i == '{':
            depth.append(BRACES)
            
        elif i == '}':
            if len(depth) == 0:
                return False
                
            if depth[-1] == BRACES:
                depth.pop(-1)
            else:
                return False

    if depth == []:
        return True
    else:
        return False
