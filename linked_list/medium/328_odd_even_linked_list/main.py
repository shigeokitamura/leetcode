# https://leetcode.com/problems/odd-even-linked-list/?envType=study-plan-v2&envId=leetcode-75

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        odd = ListNode(0)
        odd_pointer = odd
        even = ListNode(0)
        even_pointer = even

        idx = 1
        while head != None:
            if idx % 2 == 0:
                even_pointer.next = head
                even_pointer = even_pointer.next
            else:
                odd_pointer.next = head
                odd_pointer = odd_pointer.next

            head = head.next
            idx += 1

        even_pointer.next = None
        odd_pointer.next = even.next

        return odd.next

if __name__ == "__main__":
    s = Solution()

    s.oddEvenList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
    s.oddEvenList(ListNode(1, ListNode(1, ListNode(3, ListNode(5, ListNode(6, ListNode(4, ListNode(7))))))))
