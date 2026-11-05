# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # space O(n)
        nodes = []

        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next
        
        cur = ListNode()
        l, r = 0, len(nodes) - 1

        while l <= r:
            if l == r:
                cur.next = nodes[r]
            else:
                cur.next = nodes[l]
                cur = cur.next
                cur.next = nodes[r]
                cur = cur.next
            l += 1
            r -= 1
        
        nodes[r+1].next = None
        return None