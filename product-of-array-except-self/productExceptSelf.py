# Given an integer array nums, return an array answer such that answer[i] is
# equal to the product of all the elements of nums except nums[i].
# Input   [1,  2,  3,  4]
# prefix  [1,  2,  6,  24]
# postfix [24, 24, 12, 4]
# Output  [24, 12, 8,  6]
def productExceptSelfBruteForce(nums: list[int]) -> list[int]:
    x = 0
    y = 0
    ans = []
    length = len(nums)
    while(x < length):
        product = 1
        while(y < length):
            if x == y:
                y += 1
                continue
            product *= nums[y]
            y += 1
        ans.append(product)
        y = 0
        x += 1
    return ans

def productExceptSelf(nums: list[int]) -> list[int]:
    products = [1 for _ in range(len(nums))]
    prefix = 1
    for i in range(len(nums)):
        products[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        products[i] *= postfix
        postfix *= nums[i]
    
    return products


input = [1, 2, 3, 4]
output = productExceptSelf(input)
print(input)
print(output)
