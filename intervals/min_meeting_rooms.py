"""
Problem: Meeting Rooms II (Minimum number of meeting rooms required)
Link: https://leetcode.com/problems/meeting-rooms-ii/

Clarification:
- Intervals may be unsorted.
- A room can be reused if the previous meeting ends at or before the next start.

Approach (Two Pointers on sorted starts/ends):
1) Split starts and ends into separate arrays and sort both.
2) Walk starts with pointer i, ends with pointer j:
   - If starts[i] < ends[j]: we need a new room → used += 1, i += 1
   - Else: a meeting ended → free a room → used -= 1, j += 1
3) Track the maximum value of 'used' during the scan → that's the answer.

Time:  O(n log n)   (sorting dominates)
Space: O(n)         (the two arrays)
"""

from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Build sorted start and end timelines
        starts = sorted(iv[0] for iv in intervals)
        ends   = sorted(iv[1] for iv in intervals)

        i = j = 0
        used = 0
        max_rooms = 0
        n = len(intervals)

        # Sweep through all starts
        while i < n:
            if starts[i] < ends[j]:
                # Need a room for this new meeting
                used += 1
                max_rooms = max(max_rooms, used)
                i += 1
            else:
                # One meeting ended; free the room
                used -= 1
                j += 1

        return max_rooms


"""
Alternative (Min-Heap) — also O(n log n):
- Sort intervals by start.
- Use a min-heap of end times; pop when the earliest meeting ends before current starts.
- Push current end; heap size is rooms in use; track max size.
"""

