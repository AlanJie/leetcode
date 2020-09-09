class Solution:

    def climbStairs(self, n: int) -> int:
        # 时间复杂度: O(n)
        # 空间复杂度: O(n)
        if n == 1:
            return 1 
        if n == 2:
            return 2 

        steps = [1, 2]
        for i in range(2, n):
            steps.append(steps[i-1] + steps[i-2])

        return steps[-1]

    def climbStairs2(self, n: int) -> int:
        if n == 1:
            return 1 

        if n == 2:
            return 2

        first = 1
        second = 2 
        for i in range(2, n):
            temp = first + second 
            first = second 
            second = temp 

        return second

    def climbStairs3(self, n: int) -> int:
        first, second, temp = 0, 0, 1 

        for i in range(n):  # 或者 for i in range(1, n+1)
            first = second 
            second = temp 
            temp = first + second

        return temp


if __name__ == '__main__':
    print(Solution().climbStairs3(5)) 