class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        H_length, N_length = len(haystack), len(needle)

        for i in range(H_length - N_length + 1):
            if haystack[i: i+N_length] == needle:
                return i 

        return -1


class Solution2:

    def strStr(self, haystack: str, needle: str) -> int:
        H_length, N_length = len(haystack), len(needle)

        if N_length == 0:
            return 0

        h_idx = 0
        while h_idx < H_length - N_length + 1:

            while (h_idx < H_length - N_length + 1) and (haystack[h_idx] != needle[0]):
                h_idx += 1

            match_length = 0 
            n_idx = 0 
            while n_idx < N_length and h_idx < H_length and haystack[h_idx] == needle[n_idx]:
                h_idx += 1 
                n_idx += 1 
                match_length += 1 

            if match_length == N_length:
                return h_idx - match_length

            h_idx -= (match_length - 1)

        return -1


if __name__ == '__main__':
    haystack = "hello"
    needle = "ll"
    idx = Solution2().strStr(haystack, needle)
    print(idx)
