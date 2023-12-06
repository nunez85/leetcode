def twoSum(self, numbers: list[int], target: int) -> list[int]:
    left = 0
    right = len(numbers) - 1
    while left < right:
        summation = numbers[left] + numbers[right] 
        if summation == target:
            return [left+1, right+1]
        elif summation < target:
            left += 1
        elif summation > target:
            right -= 1
        
    return [-1, -1]