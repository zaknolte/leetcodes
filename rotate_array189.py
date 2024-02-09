from typing import List
def rotate(nums: List[int], k: int) -> None:
    while k > 0:
        num = nums.pop(-1)
        nums.insert(0, num)
        k -= 1
            
print(rotate(nums = [1,2,3,4,5,6,7], k=3))