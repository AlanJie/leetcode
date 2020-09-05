class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        # return len(s.strip().split(' ')[-1])
        
        length = len(s)
        if length == 0:
            return 0
        count = 0

        for idx in range(length, 0, -1):
            if s[idx - 1] == ' ':
                if count == 0:
                    continue
                break 
            count += 1
                
        return count 


if __name__ == '__main__':
    s = "hello world"
    print(Solution().lengthOfLastWord(s))
