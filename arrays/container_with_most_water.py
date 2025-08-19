"""
Problem: Container With Most Water
Link: https://leetcode.com/problems/container-with-most-water/

Clarification Questions:
1) What if the array is empty? -> Return 0
2) What if it has only one line? -> Cannot form a container, return 0
3) Are heights non-negative integers? -> Yes
4) Any constraints on input size? -> LeetCode version: 2 <= n <= 10^5

Approaches:

1) Brute Force
   - Consider all pairs of vertical lines (i, j)
   - Compute water = min(height[i], height[j]) * (j - i)
   - Track maximum
   - Time:  O(n^2)
   - Space: O(1)

2) Two Pointers (Optimized)
   - Place two pointers at ends (left=0, right=n-1)
   - Compute area
   - Move the pointer with smaller height inward
   - Track maximum
   - Time:  O(n)
   - Space: O(1)
"""

from typing import List

class Solution:
    # ---------- Approach 1: Brute Force ----------
    def maxArea_bruteforce(self, height: List[int]) -> int:
        n = len(height)
        max_area = 0
        for i in range(n):
            for j in range(i + 1, n):
                area = min(height[i], height[j]) * (j - i)
                max_area = max(max_area, area)
        return max_area

    # ---------- Approach 2: Two Pointers ----------
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n - 1
        max_area = 0

        while left < right:
            length = min(height[left], height[right])
            width = right - left
            area = length * width
            max_area = max(max_area, area)

            # move the smaller height pointer
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_area


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxArea([1,8,6,2,5,4,8,3,7]))  # Expected 49

