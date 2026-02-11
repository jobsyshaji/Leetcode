# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head

        group_prev = dummy
        current = head

        while True:
            check = current
            count = 0

            while check and count < k:
                check = check.next
                count += 1

            if count < k:
                break

            prev = None
            group_start = current


            for _ in range(k):
                nxt = current.next
                current.next = prev
                prev = current
                current = nxt

            group_prev.next = prev
            group_start.next = current

            group_prev = group_start

        return dummy.next
        