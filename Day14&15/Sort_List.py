# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ls = []
        while head:
            ls.append(head.val)
            head = head.next
        ls.sort()
        node = ListNode(0)
        cur = node

        for n in ls:
            cur.next = ListNode(n)
            cur = cur.next
        return node.next 
        