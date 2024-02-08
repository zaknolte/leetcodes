from typing import List
def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:] = nums2
        else:
            temp_nums = []
            index_1 = 0
            index_2 = 0
            for i in range(m + n):
                if index_1 < m and index_2 < n:
                    if nums1[index_1] < nums2[index_2]:
                        temp_nums.append(nums1[index_1])
                        index_1 += 1
                    elif nums1[index_1] > nums2[index_2]:
                        temp_nums.append(nums2[index_2])
                        index_2 += 1
                    else:
                        temp_nums.append(nums1[index_1])
                        temp_nums.append(nums2[index_2])
                        index_1 += 1
                        index_2 += 1
                elif index_1 < m and index_2 >= n:
                    temp_nums.append(nums1[index_1])
                    index_1 += 1
                elif index_1 >= m and index_2 < n:
                    temp_nums.append(nums2[index_2])
                    index_2 += 1
            nums1[:] = temp_nums
        print(nums1)
        
merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)