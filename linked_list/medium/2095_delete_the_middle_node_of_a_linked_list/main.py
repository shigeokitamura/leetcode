# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/?envType=study-plan-v2&envId=leetcode-75

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        prev = ListNode(0)
        prev.next = head
        slow = prev
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next

        return prev.next

if __name__ == "__main__":
    s = Solution()

    s.deleteMiddle(ListNode(1, ListNode(3, ListNode(4, ListNode(7, ListNode(1, ListNode(2, ListNode(6))))))))
    s.deleteMiddle(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
    s.deleteMiddle(ListNode(2, ListNode(1)))
