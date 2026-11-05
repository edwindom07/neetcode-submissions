# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and list2:
            return list2
        if list1 and not list2:
            return list1
        if not list1 and not list2:
            return None
        
        res = None
        cur = None
        if list1.val <= list2.val:
            res = cur = list1
            list1 = list1.next
        else:
            res = cur = list2
            list2 = list2.next
        
        while True:
            if not list1:
                cur.next = list2
                break
            if not list2:
                cur.next = list1
                break
            if list1.val <= list2.val:
                cur.next = list1
                cur = list1
                list1 = list1.next
            else:
                cur.next = list2
                cur = list2
                list2 = list2.next
            
        return res
