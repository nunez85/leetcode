from itertools import permutations

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


def generateParentheisDumb(n: int) -> list[str]:
    all_parenthesis = '()' * n
    combinations = set()
    for p in permutations(all_parenthesis, n * 2):
        c = ''.join(p)
        if c not in combinations and isValid(p):
            combinations.add(c)
        
    return list(combinations)


def generateParenthesis(n: int) -> list[str]:
    stack = []
    res = []
    def backtracking(openN, closedN):
        if openN == closedN == n:
            res.append("".join(stack))
            return
        
        if openN < n:
            stack.append('(')
            backtracking(openN+1, closedN)
            stack.pop()

        if closedN < openN:
            stack.append(')')
            backtracking(openN, closedN+1)
            stack.pop()

    backtracking(0, 0)
    return res


input = 3
output = generateParenthesis(input)
print(output)

