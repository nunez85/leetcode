def evalRPN(tokens: list[str]) -> int:
    stack = []
    operations = {'*', '-', '+', '/'}
    for token in tokens:
        if token in operations:
            right = str(stack.pop())
            left = str(stack.pop())
            expression = left + token +right
            stack.append(int(eval(expression)))

        else:
            stack.append(token)
    return stack.pop()

input = ['3', '4', '+', '4', '*']
output = evalRPN(input)
print(output)