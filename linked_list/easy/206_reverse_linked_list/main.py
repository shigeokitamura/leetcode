# https://leetcode.com/problems/odd-even-linked-list/?envType=study-plan-v2&envId=leetcode-75

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head

        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev

if __name__ == "__main__":
    s = Solution()

    s.reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
    s.reverseList(ListNode(1, ListNode(2)))
    s.reverseList(None)
