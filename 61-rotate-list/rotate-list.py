# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        if not head or not head.next or k == 0:
            return head

        size = 0
        tail = head
        while tail:
            size += 1
            if not tail.next:
                break
            tail = tail.next

        k = k % size
        if k == 0:
            return head

        slow = head
        fast = head

        for _ in range(k):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        new_head = slow.next
        slow.next = None
        fast.next = head

        return new_head