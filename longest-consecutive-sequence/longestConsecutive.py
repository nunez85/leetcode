from collections import defaultdict


def longestConsecutive(nums: list[int]) -> int:
    longest = 0
    s = set(nums)
    for n in nums:
        if n-1 in s:
            continue
        
        count = 1
        i = n + 1
        while i in s:
            count += 1
            i += 1

        longest = max(count, longest)
    return  longest

input = [100, 4, 200, 1, 2, 3]
output = longestConsecutive(input)
print(output)