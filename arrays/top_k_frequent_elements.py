"""
Problem: Top K Frequent Elements
Link: https://leetcode.com/problems/top-k-frequent-elements/

Clarification Questions:
1) Can nums contain duplicates? -> Yes.
2) Should outputs be distinct? -> Yes, return the k most frequent *distinct* elements.
3) What if nums is empty? -> Return [].
4) What if k > number of distinct elements? -> Return all distinct elements (any order).

Approaches:

1) Heap (min-heap of size k) + Counter
   - Count frequencies, keep a min-heap of (freq, num) of size k.
   - Time:  O(n log k)
   - Space: O(n)

2) Bucket Sort + Counter (Linear)
   - Count frequencies, place numbers in buckets indexed by frequency.
   - Scan buckets from high to low and collect k elements.
   - Time:  O(n)
   - Space: O(n)
"""

from typing import List
from collections import Counter
import heapq


class Solution:
    # ---------- Approach 1: Heap (O(n log k)) ----------
    def topKFrequent_heap(self, nums: List[int], k: int) -> List[int]:
        if not nums or k <= 0:
            return []
        freq = Counter(nums)

        # If k >= distinct count, return all keys
        if k >= len(freq):
            return list(freq.keys())

        # min-heap of size k: (frequency, value)
        heap = []
        for val, f in freq.items():
            if len(heap) < k:
                heapq.heappush(heap, (f, val))
            else:
                # push and pop smallest in one op to keep size k
                heapq.heappushpop(heap, (f, val))

        # extract values
        return [val for _, val in heap]

    # ---------- Approach 2: Bucket Sort (O(n)) ----------
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Default to the bucket sort approach for linear time.
        """
        if not nums or k <= 0:
            return []

        freq = Counter(nums)
        if k >= len(freq):
            return list(freq.keys())

        # buckets[i] holds list of numbers appearing exactly i times
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, f in freq.items():
            buckets[f].append(num)

        ans = []
        # iterate from highest frequency to lowest
        for f in range(len(nums), 0, -1):
            if buckets[f]:
                ans.extend(buckets[f])
                if len(ans) >= k:
                    return ans[:k]
        return ans  # fallback (already covered)
        

if __name__ == "__main__":
    sol = Solution()
    print(sol.topKFrequent([1,1,1,2,2,3], 2))  # e.g., [1,2]
    print(sol.topKFrequent_heap([1], 1))       # [1]

