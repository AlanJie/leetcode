from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return nums
            
        i = 1
        for j in range(1, len(nums)):
            if nums[j] != nums[j - 1]:
                nums[i] = nums[j]
                i += 1
        nums[:] = nums[:i]
        return 

if __name__ == '__main__':
    test = [0,0,1,1,1,2,2,3,3,4]
    Solution().removeDuplicates(test)
    print(test)

    a = test[:2]
    print(a)
    a[1] = 12 
    print(a)
    print(test)