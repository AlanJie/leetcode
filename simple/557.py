class Solution:
    # def reverseWords(self, s: str) -> str:
    #     str_list = s.split(' ')
    #     str_list = [s[::-1] for s in str_list]

    #     s = ' '.join(str_list)

    #     return s

    def reverseWords(self, s: str) -> str:
        return ' '.join(x[::-1] for x in s.split(' '))


if __name__ == '__main__':
    s = "Let's take LeetCode contest"
    s = Solution().reverseWords(s)

    print(s)
