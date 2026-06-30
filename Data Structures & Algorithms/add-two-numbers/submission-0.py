# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        curry = 0
        while l1 or l2 or curry:
            if l1:
                v1 = l1.val
            else:
                v1 = 0
            if l2:
                v2 = l2.val
            else:
                v2 = 0
            total = v1 + v2 + curry
            curry = total // 10
            cur.next = ListNode(total%10)
            cur = cur.next
            if l1:
                l1 = l1.next
            else:
                None
            if l2:
                l2 = l2.next
            else:
                None
        return dummy.next
