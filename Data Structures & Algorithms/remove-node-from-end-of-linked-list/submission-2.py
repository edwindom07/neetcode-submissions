# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        point = cur = head
        while cur:
            cur = cur.next
            if n < 0:
                point = point.next
            n -= 1
        
        if n == 0:
            return head.next
        
        point.next = point.next.next
        return head

        """
        n = 2
        1, 2
        cur = 1
        point = 1

        n = 1
        1, 2
        cur = 1
        point = 2

        done



        n = 2
        1, 2, 3, 4
        cur = 1
        point = 1

        n = 1
        1, 2, 3, 4
        cur = 1
        point = 2

        n = 0
        1, 2, 3, 4
        cur = 1
        point = 3

        n = -1
        1, 2, 3, 4
        cur = 2
        point = 4

        done
        remove afer point
        """