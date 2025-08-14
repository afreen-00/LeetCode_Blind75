"""
Problem: Merge Intervals
Link: https://leetcode.com/problems/merge-intervals/

Clarification Questions:
1) Can intervals be unsorted? -> Yes, assume unsorted.
2) Can intervals be empty? -> Yes, return [].
3) What about single-element intervals? -> Return as-is.
4) Are intervals closed ranges [start, end]? -> Yes.
5) Can there be fully contained intervals? -> Yes (e.g., [1,10] and [3,4]); merge keeps [1,10].

Approaches:
1) Sort + One Pass (Optimal)
   - Sort by start, merge in one linear sweep.
   Time: O(n log n), Space: O(n) for result

2) Brute Force (Educational)
   - Repeatedly scan and merge any overlapping pair until stable.
   Time: O(n^2) worst, Space: O(n)
"""

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Optimal: Sort + One Pass
        - Sort intervals by start time
        - Append or merge with the last interval in result.
        Time: O(n log n), Space: O(n)
        """
        if not intervals:
            return []

        # Sort by start
        intervals.sort(key=lambda x: x[0])

        merged = []
        for start, end in intervals:
            if not merged or merged[-1][1] < start:
                # No overlap -> push new
                merged.append([start, end])
            else:
                # Overlap -> extend the end
                merged[-1][1] = max(merged[-1][1], end)
        return merged

    def merge_bruteforce(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Brute Force:
        - Keep merging overlapping pairs until no change.
        Time: O(n^2), Space: O(n)
        """
        if not intervals:
            return []

        # Work on a copy to avoid mutating caller input
        ints = intervals[:]

        def overlaps(a: List[int], b: List[int]) -> bool:
            return not (a[1] < b[0] or b[1] < a[0])

        changed = True
        while changed:
            changed = False
            ints.sort(key=lambda x: x[0])
            result = []
            for interval in ints:
                if not result or not overlaps(result[-1], interval):
                    result.append(interval)
                else:
                    result[-1] = [result[-1][0], max(result[-1][1], interval[1])]
                    changed = True
            ints = result
        return ints


if __name__ == "__main__":
    sol = Solution()

    # Basic
    print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))      # [[1,6],[8,10],[15,18]]
    print(sol.merge([[1,4],[4,5]]))                     # [[1,5]]

    # Edge cases
    print(sol.merge([]))                                 # []
    print(sol.merge([[1,2]]))                            # [[1,2]]
    print(sol.merge([[1,10],[2,3],[4,8],[9,12]]))        # [[1,12]]

