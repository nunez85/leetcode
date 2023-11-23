
def removeElement(nums: list[int], val: int) -> int:
    counter = 0
    i = 0
    indexOfNotVal = 1
    while i < len(nums) or indexOfNotVal < len(nums):
        if nums[i] == val:
            
            # find an index such that nums[indexOfNotVal] != val to swap it in place
            while True:
                if indexOfNotVal >= len(nums):
                    return counter
                
                elif nums[indexOfNotVal] != val:
                    break

                else:
                    indexOfNotVal += 1

            nums[i], nums[indexOfNotVal] = nums[indexOfNotVal], nums[i]
            counter += 1
            indexOfNotVal += 1

        else:
            indexOfNotVal += 1
            counter += 1         
        
        i += 1
    
    return counter

    
if __name__ == "__main__":
    test1 = [3, 2, 2, 3]
    test2 = [0, 1, 2, 2, 3, 4, 0]

    print("--- test 1 ---")
    print(test1)
    expected1 = removeElement(test1, 3)
    print(test1)
    print(expected1)
    print("--- test 2 ---")
    print(test2)
    expected2 = removeElement(test2, 2)
    print(test2)
    print(expected2)