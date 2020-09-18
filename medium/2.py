# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 使用 dummy 可以减少对开头结点的特殊操作
        dummy = ListNode(0)
        # 初始化进位为0
        carry = 0 

        cur = dummy

        while l1 or l2:
            # 如果 l1 还没有结束，就使用 l1 的值，否则为 0 
            p = l1.val if l1 else 0 
            # 如果 l2 还没有结束，就使用 l2 的值，否则为 0 
            q = l2.val if l2 else 0 
            # 当前位的和 = 当前位上的数字之和 + 进位
            s = p + q + carry 
            # 进位 = 当前和 //(整除) 10
            carry = s // 10 

            # 构建当前节点的下一个节点： 用当前和对10取余数，即去除进位后剩余的数字
            cur.next = ListNode(s % 10)
            # 移动cur的指向
            cur = cur.next 

            if l1:  # 如果 l1 还未结束，则移动到下一位
                l1 = l1.next 
            if l2:  # 如果 l2 还未结束，则移动到下一位
                l2 = l2.next 

        if carry != 0:
            # 如果最后一位的和存在进位，把进位加上去
            cur.next = ListNode(carry)
        
        return dummy.next


def printListNode(l: ListNode):
    s = f'{l.val}'
    while l.next:
        l = l.next
        s += f' --> {l.val}'

    print(s)


if __name__ == '__main__':
    node1_3 = ListNode(3)
    node1_2 = ListNode(4, node1_3)
    node1_1 = ListNode(2, node1_2)

    node2_3 = ListNode(4)
    node2_2 = ListNode(6, node2_3)
    node2_1 = ListNode(5, node2_2)
    
    res = Solution().addTwoNumbers(node1_1, node2_1)
    printListNode(res)
