def maxNumberOfBalloons(text: str) -> int:
    b = 0
    a = 0
    l = 0
    o = 0
    n = 0
    for char in text:
        if char == 'b':
            b += 1
        elif char == 'a':
            a += 1
        elif char == 'l':
            l += 1
        elif char == 'o':
            o += 1
        elif char == 'n':
            n += 1
    
    o = o // 2
    l = l // 2

    return min(b, a, l, o, n)
