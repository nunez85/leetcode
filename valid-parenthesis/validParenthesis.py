def isValid(s: str) -> bool:
    if len(s) == 1:
        return False 

    closingToOpen = {'}': '{',
                    ')': '(',
                    ']': '['}
    stack = []
    for c in s:
        if c in closingToOpen:
            if stack and stack[-1] == closingToOpen[c]:
                stack.pop()
            else:
                return False
            
        else:
            stack.append(c)

    return len(stack) == 0

input = "()[]{}}"
output = isValid(input)
print(output)