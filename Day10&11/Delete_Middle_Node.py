# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        curr = head
        s = head
        f = head
        prev = None

        while f and f.next:
            prev = s
            s = s.next
            f = f.next.next

        prev.next = prev.next.next
        return head
        