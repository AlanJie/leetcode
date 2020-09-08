from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        tmp = 0

        for i, num in enumerate(digits[::-1]):
            tmp += num * 10 ** i 

        tmp += 1
        res = [int(s) for s in str(tmp)]

        return res


if __name__ == '__main__':
    digits = [4, 3, 2, 1]
    print(Solution().plusOne(digits))

