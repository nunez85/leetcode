def maxArea(height: list[int]) -> int:
    maximumArea = float('-inf')
    left = 0
    right = len(height) - 1

    while left < right:
        area = (right - left) * min(height[left], height[right])
        maximumArea = max(area, maximumArea)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return int(maximumArea)
