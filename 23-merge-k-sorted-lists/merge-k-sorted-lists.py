class Solution:
    def mergeKLists(self, lists):

        values = []

        for head in lists:
            while head:
                values.append(head.val)
                head = head.next

        if not values:
            return None

        values.sort()

        dummy = ListNode(0)
        current = dummy

        for v in values:
            current.next = ListNode(v)
            current = current.next

        return dummy.next