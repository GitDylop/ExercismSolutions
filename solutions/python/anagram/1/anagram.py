def find_anagrams(word, candidates):
    anagrams = []
    word_sorted = sorted(word.lower())
    
    for candidate in candidates:
        if candidate.lower() != word.lower() and sorted(candidate.lower()) == word_sorted:
            anagrams.append(candidate)
            
    return anagrams