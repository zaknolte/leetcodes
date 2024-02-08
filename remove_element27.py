from typing import List
def removeElement(nums: List[int], val: int) -> int:
    k = 0
    index = len(nums) - 1 
    for num in nums[::-1]:
        if num == val:
            nums.pop(index)
            k += 1
        index -= 1
    print(k, nums)
        
removeElement(nums = [3,2,2,3], val = 3)