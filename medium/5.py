class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ''
        if n == 1:
            return s

        res = ''

        for i in range(n-1):  # [0123]  0
            pr = i + 1  # 1
            start_char = s[i]  # c
            while pr < n and s[pr] != s[i]:
                pr += 1

            temp = s[i:pr+1]
            for j in range(len(temp) // 2):
                if temp[j] != temp[-j-1]:
                    break
                if len(temp) > len(res):
                    res = temp

        if res == '':
            return s[0]
                
        return res


if __name__ == '__main__':
    s = "ac"
    print(Solution().longestPalindrome(s))
