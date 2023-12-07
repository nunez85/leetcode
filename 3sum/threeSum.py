def threeSum(nums: list[int]) -> list[list[int]]:
    if len(nums) < 3:
        return []
    res = []
    nums.sort()

    for i, a in enumerate(nums):
        if a > 0:
            break

        if i > 0 and nums[i - 1] == a:
            continue

        left = i+1
        right = len(nums)-1
        while left < right:
            summation = a + nums[left] + nums[right]

            if summation < 0:
                left += 1
            elif summation > 0:
                right -= 1
            else:
                res.append([a, nums[left], nums[right]])
                left += 1
                right -= 1

                while left < right and nums[left-1] == nums[left]:
                    left += 1

    return res
