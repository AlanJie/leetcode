# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        slow = fast = head

        while slow and fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 

            if slow == fast:
                ptr = head 
                while ptr != slow:
                    ptr = ptr.next 
                    slow = slow.next
                return ptr 

        return None
