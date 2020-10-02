class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:

        res = 0 

        if not len(J) or not len(S):
            return res 

        for stone in S:
            if stone in J:
                res += 1 

        return res 


class Solution2:

    def numJewelsInStones(self, J: str, S: str) -> int:
        res = 0 

        if not len(J) or not len(S):
            return res 

        J = set(J)
        
        return sum(s in J for s in S)


if __name__ == '__main__':
    J = "aA"
    S = "aAAbbbb"
    print(Solution2().numJewelsInStones(J, S))