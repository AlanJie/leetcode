from typing import List
from collections import Counter


class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        dic = Counter(nums)  # 对每个数字出现的次数进行统计
        arr = sorted(dic.keys())  # 排序键值
        for i, a in enumerate(arr):
            dic[a] -= 1  # a 用掉一次，而且 a 的位置之后不会再遍历到了，不需要加回
            for j, b in enumerate(arr[i:]):  # 从 arr[i] 开始找b的值
                if dic[b] < 1:  # b 可能等于 a, 判断一下，如果 dic[b] 不够一个，则跳过这次循环
                    continue
                dic[b] -= 1 
                for c in arr[i + j:]:  # 从 arr[i+j] 开始找 c 的值，注意上一层循环枚举 j 以后，需要再加最外层的i
                    if dic[c] < 1:  # 同上层循环 b 的判断
                        continue
                    d = target - (a + b + c)
                    
                    if d < c:  # 因为是非递减顺序，如果 d 小于 c，就直接跳出，这样可以避免重复
                        break 

                    if (d == c and dic[d] > 1) or (d > c and dic[d] > 0):
                        res.append([a, b, c, d])
                dic[b] += 1  # b 现在所处的位置，之后 a 还会遍历到，因此需要加回1
        return res


if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    print(Solution().fourSum(nums, target))
