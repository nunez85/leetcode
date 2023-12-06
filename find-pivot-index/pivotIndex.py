def pivotIndex(self, nums: list[int]) -> int:
    left = []
    count = 0
    for n in nums:
        count += n
        left.append(count)
    
    right = [0] * len(nums)

    count = 0
    for i in range(len(nums)-1, -1, -1):
        count += nums[i]
        right[i] = count
        
    for i, (l, r) in enumerate(zip(left, right)):
        if l == r:
            return i
        i += 1

    return -1