# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        cur_node = head 

        while cur_node is not None and cur_node.next is not None:
            if cur_node.val == cur_node.next.val:
                cur_node.next = cur_node.next.next
            else:
                cur_node = cur_node.next 

        return head 


def print_listnode(head: ListNode):
    if head is None:
        return ''
    node_str = str(head.val)
    node = head.next
    while node is not None:
        node_str += f'->{node.val}'
        node = node.next

    print(node_str)


if __name__ == '__main__':
    # 1->1->2->3->3
    node5 = ListNode(3, None)
    node4 = ListNode(3, node5)
    node3 = ListNode(2, node4)
    node2 = ListNode(1, node3)
    node1 = ListNode(1, node2)

    # 1->1->1
    # node3 = ListNode(1, None)
    # node2 = ListNode(1, node3)
    # node1 = ListNode(1, node2)

    listnode = Solution().deleteDuplicates(node1)
    print_listnode(node1)
