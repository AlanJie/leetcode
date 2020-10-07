from typing import List 

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l, r = 0, n - 1
        i = 0 
        while i <= r:
            if nums[i] == 0:
                nums[i] = nums[l]
                nums[l] = 0 
                l += 1 
            if nums[i] == 2:
                nums[i] = nums[r]
                nums[r] = 2 
                r -= 1 
                i -= 1 

            i += 1


if __name__ == '__main__':
    nums = [2,0,1]
    Solution().sortColors(nums)

    print(nums)
