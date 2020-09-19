class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)

        if n == 0:
            return 0 

        if n == 1:
            return 1

        seen = {s[0]}
        pr = 1
        res = 0

        for i in range(n):

            if i != 0:
                seen.remove(s[i - 1])

            while pr < n and s[pr] not in seen:
                seen.add(s[pr])
                pr += 1

            res = max(pr - i, res)

        return res


if __name__ == '__main__':
    s = "abcabcdbb"
    print(Solution().lengthOfLongestSubstring(s))
