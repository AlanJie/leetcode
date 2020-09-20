from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        for i in range(1 << n):
            temp = []
            for j in range(n):
                if i & (1 << j):
                    temp.append(nums[j])
            res.append(temp)

        return res 


class Solution2:

    def subsets(self, nums: List[int]) -> List[List[int]]:

        def dfs(cur, nums, t, res):
            if cur == len(nums):
                res.append(t.copy())
                return 

            t.append(nums[cur])
            # 包含自己在内
            dfs(cur + 1, nums, t, res)
            t.pop(-1)
            # 不包含自己
            dfs(cur + 1, nums, t, res)
        
        res = []
        dfs(0, nums, [], res)

        return res 

if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution2().subsets(nums))
