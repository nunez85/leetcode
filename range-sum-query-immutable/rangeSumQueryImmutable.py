class NumArray:

    def __init__(self, nums: list[int]):
        self.left = []
        count = 0
        for n in nums:
            count += n
            self.left.append(count)
        print(self.left)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.left[right]
        return self.left[right] - self.left[left-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)