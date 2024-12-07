# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/?envType=study-plan-v2&envId=leetcode-75

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> Optional[ListNode]:
        max_value = 0
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        next_node = None
        prev = None

        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        while prev:
            max_value = max(max_value, head.val + prev.val)
            prev = prev.next
            head = head.next

        return max_value

if __name__ == "__main__":
    s = Solution()

    print(s.pairSum(ListNode(5, ListNode(4, ListNode(2, ListNode(1)))))) # 6
    print(s.pairSum(ListNode(4, ListNode(2, ListNode(2, ListNode(3)))))) # 7
    print(s.pairSum(ListNode(1, ListNode(100000)))) # 100001
