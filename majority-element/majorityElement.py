# Boyer-Moore Voting Algorithm
def majorityElementBoyer(nums: List[int]) -> int:
    count = 0
    candidate = 0
    for num in nums:
        if count == 0:
            candidate = num

        count += (1 if num == candidate else -1)

    return candidate
from collections import Counter

def majorityElementCounterDict(nums: list[int]) -> int:
    count = Counter(nums)
    return max(count.items(), key=count.get)


def majorityElementCounterSort(nums: list[int]) -> int:
    return sorted(nums)[len(nums]//2]
  
