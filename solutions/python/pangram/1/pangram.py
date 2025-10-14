def is_pangram(sentence):
    letters = {ch.lower() for ch in sentence if ch.isalpha()}
    return len(letters) == 26
