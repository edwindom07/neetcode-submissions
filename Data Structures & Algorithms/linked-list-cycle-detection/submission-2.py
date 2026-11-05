# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # two pointer, first goes 2 steps, second goes 1 step
        if not head or not head.next:
            return False
        
        one = head
        two = head.next

        while two and two.next:
            if one == two:
                return True
            one = one.next
            two = two.next.next
        return False