from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def dfs(nums, size, used, cur_depth, cur_path, res):
            if cur_depth == size:
                # 当前节点数等于元素个数
                res.append(cur_path.copy())
                return 

            for i in range(size):
                if not used[i]:  # 该节点还没有使用
                    cur_path.append(nums[i])
                    used[i] = True 
                    
                    dfs(nums, size, used, cur_depth + 1, cur_path, res)
                    cur_path.pop()  # 这里 pop 的是当前path的最后一个元素，而不是完整path的最后一个元素
                    used[i] = False
                    # 这里没有使用 cur_depth += 1, 而是直接在迭代中传入 cur_depth + 1，是为了回溯方便，否则这里还要加一句 cur_depth -= 1
        
        size = len(nums)
        if size == 0:
            return []

        res = []  # 存储结果
        used = [False] * size 
        dfs(nums, size, used, 0, [], res)

        return res 


if __name__ == '__main__':
    nums = [1,2,3]
    res = Solution().permute(nums)
    print(res)
