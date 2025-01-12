# https://leetcode.com/problems/kth-largest-element-in-an-array/description/?envType=study-plan-v2&envId=leetcode-75

import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = [] # Initialize a min-heap

        for num in nums:
            heapq.heappush(min_heap, num) # Push each number onto the heap
            if len(min_heap) > k: # If the heap size exceeds k
                heapq.heappop(min_heap) # Remove the smallest element

        return min_heap[0] # The smallest element in the heap is the kth largest


if __name__ == "__main__":
    s = Solution()

    print(s.findKthLargest([3,2,1,5,6,4], 2)) # 5
    print(s.findKthLargest([3,2,3,1,2,4,5,5,6], 4)) # 4
