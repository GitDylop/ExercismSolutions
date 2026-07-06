import string

def answer(question):
    punctuation = string.punctuation.replace("-", "")
    tokens = [token.strip(punctuation) for token in question.split()]

    if len(tokens) < 3:
        raise ValueError("syntax error")

    try:
        answer = int(tokens[2])
    except (ValueError, IndexError):
        raise ValueError("syntax error")

    current_token = 3
    while current_token < len(tokens):
        op = tokens[current_token]

        if op not in ['plus', 'minus', 'multiplied', 'divided']:
            if op.lstrip('-').isdigit():
                raise ValueError("syntax error")
            raise ValueError("unknown operation")

        current_token += 1

        if current_token < len(tokens) and tokens[current_token] == 'by':
            current_token += 1

        try:
            next_num = int(tokens[current_token])
        except (ValueError, IndexError):
            raise ValueError("syntax error")

        if op == 'plus':
            answer += next_num
        elif op == 'minus':
            answer -= next_num
        elif op == 'multiplied':
            answer *= next_num
        elif op == 'divided':
            answer /= next_num

        current_token += 1

    return answer
