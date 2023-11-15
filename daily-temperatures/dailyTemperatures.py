def dailyTemperaturesBruteForce(temperatures: list[int]) -> list[int]:
    res = []
    for i in range(len(temperatures)):
        foundIndex = -1
        x = i + 1
        while x < len(temperatures):
            if temperatures[i] < temperatures[x]:
                foundIndex = x
                break
            x += 1

        if foundIndex != -1:
            res.append(foundIndex - i)
        else:
            res.append(0)

    return res

def dailyTemperatures(temperatures: list[int]) -> list[int]:
    res = [0] * len(temperatures)
    stack = []
    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            stackTemp, stackIndex = stack.pop()
            res[stackIndex] = i - stackIndex
        stack.append([t, i])

    return res
        

input = [73,74,75,71,69,72,76,73]
output = dailyTemperatures(input)
print(input)
print(output)