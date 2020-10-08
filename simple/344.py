from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        if n == 0 or n == 1:
            return 

        l, r = 0, n - 1 

        while l < r:
            tmp = s[l]
            s[l] = s[r]
            s[r] = tmp 
        
            l += 1 
            r -= 1 


if __name__ == '__main__':
    s = ["H","a","n","a", "n","a","h"]
    Solution().reverseString(s)
    print(s)
