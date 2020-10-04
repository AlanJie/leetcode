from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = dict()
        for i, num in enumerate(nums):
            if target - num in visited:
                return [visited[target - num], i]
            visited[num] = i 
        
        return []


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution2().twoSum(nums, target))
