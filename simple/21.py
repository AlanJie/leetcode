class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next 


class Solution:

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2 
        if not l2:
            return l1 

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1 
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2 



if __name__ == '__main__':
    node1_3 = ListNode(4, None)
    node1_2 = ListNode(2, node1_3)
    node1_1 = ListNode(1, node1_2)

    node2_3 = ListNode(4, None)
    node2_2 = ListNode(3, node2_3)
    node2_1 = ListNode(1, node2_2)

    result = Solution().mergeTwoLists(node1_1, node2_1)

    eles = [str(result.val)]
    while result.next:
        result = result.next
        eles.append(str(result.val))

    print(' '.join(eles))

