# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        slow = fast = head

        while slow and fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 

            if slow == fast:
                return True 

        return False
