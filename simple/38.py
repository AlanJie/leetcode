class Solution:
    """
    双指针
    """
    def countAndSay(self, n: int) -> str:

        res = ['1']
        r = 1  # 用来记录是第几个外观数组
        
        while r < n:
            r += 1 
            p, q = 0, 1  # p q 用来遍历当前外观数组

            # res 要参与下面的遍历操作，暂时不能修改，所以额外定义一个 tmp 变量存储当前循环的外观数组，此轮循环结束后再将值赋给 res
            tmp = []
            while q <= len(res):  # 这里取等号的原因是 q 需要在字符串最后一个索引的基础上加 1 才可以得出正确的长度
                if q == len(res):
                    # 这时 q 已经超界，但只有这样才能保证此时 q-p 能得到正确的长度
                    tmp.extend([str(q-p), res[p]])
                elif res[q] != res[p]:
                    # 此时 res[q] 已经指向下一个与 res[p] 不同的字符，此时 extend 应该添加的是 res[p] 指向的字符
                    tmp.extend([str(q-p), res[p]])
                    # 将 p 指向 q 的位置，即下一个字符的起点
                    p = q

                q += 1
            # 将此轮得到的外观数组赋值给 res，tmp在下一轮循环中会被清空，重新存储下一个循环的外观数组
            res = tmp  

        return ''.join(res)


class Solution2:
    """
    递归
    """
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        res = self.countAndSay(n-1)
        p, q = 0, 1
        tmp = []
        while q <= len(res):
            if q == len(res):
                tmp.extend([str(q - p), res[p]])
            elif res[q] != res[p]:
                tmp.extend([str(q - p), res[p]])
                p = q
            q += 1
        return ''.join(tmp)


class Solution3:
    def countAndSay(self, n: int) -> str:
        res = ['1']
        for _ in range(n - 1):
            p, q = 0, 1
            tmp = []
            while q <= len(res):
                if q == len(res):
                    tmp.extend([str(q - p), res[p]])
                elif res[q] != res[p]:
                    tmp.extend([str(q - p), res[p]])
                    p = q
                q += 1
            res = tmp

        return ''.join(res)


if __name__ == '__main__':
    print(Solution3().countAndSay(5))
