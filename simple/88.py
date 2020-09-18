from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0 or n == 0:
            return 

        p1, p2 = 0, 0
        while p2 < n:
            if nums1[p1] < nums2[p2] and nums1[p1] != 0:
                p1 += 1 
            else:
                nums1.insert(p1, nums2[p2])
                p2 += 1 


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    Solution().merge(nums1, m, nums2, n)
    print(nums1)

