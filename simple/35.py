from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1 

        while l <= r:
            mid = (l + r) // 2 
            if target == nums[mid]:
                return mid 
            elif target > nums[mid]:
                l = mid + 1 
            else:
                r = mid - 1 

        return l 

    
if __name__ == '__main__':
    nums = [1,3,5,6]
    target = 5
    print(Solution().searchInsert(nums, target))
