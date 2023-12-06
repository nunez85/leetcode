def wordPattern(pattern: str, s: str) -> bool:

    if len(pattern) != len(s.split()):
        return False
        
    charToWord = dict()
    wordToChar = dict()
    for char, word in zip(pattern, s.split(' ')):
        
        if char in charToWord:
            if charToWord[char] != word:
                return False
        elif word in wordToChar:
            if wordToChar[word] != char:
                return False
        else:
            charToWord[char] = word
            wordToChar[word] = char

    return True

    