class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        first = target = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                target.next = l1
                l1 = l1.next
            else:
                target.next = l2
                l2 = l2.next
            target = target.next
        if l1:
            target.next = l1
        if l2:
            target.next = l2
        return first.next


if __name__ == '__main__':
    s1 = ListNode(1)
    s2 = ListNode(2)
    s3 = ListNode(4)
    s2.next = s3
    s1.next = s2
    t1 = ListNode(1)
    t2 = ListNode(3)
    t3 = ListNode(4)
    t2.next = t3
    t1.next = t2
    result = Solution().mergeTwoLists(s1, t1)
    print(result)
