# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s = f = head
        while f and f.next:
            f = f.next.next
            s = s.next

        st1 = []
        st2 = []

        f = s
        s =  head

        while f:
            st1.append(f.val)
            st2.append(s.val)
            f = f.next
            s = s.next

        st2.reverse()
        return st1 == st2
        