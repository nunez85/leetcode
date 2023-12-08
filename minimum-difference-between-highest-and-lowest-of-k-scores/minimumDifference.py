def minimumDifference(nums: list[int], k: int) -> int:
    if len(nums) <= 1:
        return 0

    nums.sort()
    left = len(nums) - k
    right = len(nums) - 1
    minimum = float("inf")

    while left >= 0:
        minimum = min(minimum, nums[right] - nums[left])
        left -= 1
        right -= 1

    return int(minimum)
