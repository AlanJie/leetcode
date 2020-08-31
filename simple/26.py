from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 
        
        # ************************* method 1 *********************************
        # i = 1
        # for j in range(1, len(nums)):
        #     if nums[j] != nums[j - 1]:
        #         nums[i] = nums[j]
        #         i += 1
        # nums[:] = nums[:i]
        # return 
        # **********************************************************************

        nums[:] = list(sorted(set(nums)))

        return 

if __name__ == '__main__':
    nums = [0,0,1,1,1,2,2,3,3,4]
    Solution().removeDuplicates(nums)
    print(nums)
