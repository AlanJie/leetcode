from typing import List


class Solution:

    def permuteUnique(self, nums: List[int]) -> List[int]:

        def dfs(nums, size, used, cur_depth, cur_path, res):
            
            if cur_depth == size:
                # 直接使用 res.append(path) 是浅拷贝，后续 path 发生变化时 res 也会跟着变化
                res.append(cur_path.copy())

                return 

            for i in range(size):
                if not used[i]:  # 如果当前节点没有使用
                    if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                        # 如果当前节点与上一个节点相同，且上一个节点还未使用，那么此次循环生成的结果一定与上一个节点相同
                        continue 
                    cur_path.append(nums[i])
                    used[i] = True  # 将当前节点标记为 已使用

                    dfs(nums, size, used, cur_depth+1, cur_path, res)
                    cur_path.pop()  # 这里 pop 的是当前path的最后一个元素，而不是完整path的最后一个元素
                    used[i] = False

        size = len(nums)
        if size == 0:
            return []

        nums.sort()  # 排序
        res = []  # 记录结果
        used = [False] * size  # 记录所有节点的使用情况

        dfs(nums, size, used, 0, [], res)

        return res



if __name__ == '__main__':
    nums = [1, 1, 2]
    res = Solution().permuteUnique(nums)
    print(res)
