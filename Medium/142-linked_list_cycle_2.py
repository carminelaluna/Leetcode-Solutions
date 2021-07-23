# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        pt1 = head
        pt2 = head
        while  pt2 and pt2.next:
            pt1 = pt1.next
            pt2 = pt2.next.next
            if pt1 == pt2:
                pt1 = head
                while pt1:
                    if pt1 == pt2:
                        return pt2
                    pt1 = pt1.next
                    pt2 = pt2.next
        return None
            
