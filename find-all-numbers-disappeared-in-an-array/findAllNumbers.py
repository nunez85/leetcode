def findDisappearedNumbers(nums: list[int]) -> list[int]:
    res = [False] * len(nums)
    res.append(False)
    for n in nums:
        res[n] = True
    
    print(res)
    return [x for x in range(1, len(res)) if res[x] == False]
