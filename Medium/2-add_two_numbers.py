# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = l3 = ListNode(0)
        off = 0
        while l1 is not None or l2 is not None or off:
            temp = (l1.val if l1 else 0) + off + (l2.val if l2 else 0)
            off = 0
            print(temp)
            if temp > 9:
                off = 1
                temp -= 10
            l3.next = ListNode(temp)
            l3 = l3.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            
        return head.next# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = l3 = ListNode(0)
        off = 0
        while l1 is not None or l2 is not None or off:
            temp = (l1.val if l1 else 0) + off + (l2.val if l2 else 0)
            off = 0
            print(temp)
            if temp > 9:
                off = 1
                temp -= 10
            l3.next = ListNode(temp)
            l3 = l3.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            
        return head.next
