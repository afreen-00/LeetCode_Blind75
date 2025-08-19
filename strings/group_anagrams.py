"""
Problem: Group Anagrams
Link: https://leetcode.com/problems/group-anagrams/

Clarification Questions:
1) Can the input contain duplicates? -> Yes; keep duplicates in the same group.
2) Can the input contain empty strings? -> Yes; treat "" as a valid word (groups by itself or with other "").
3) Are strings lowercase? -> LeetCode version assumes lowercase a-z. If not, adapt the key accordingly.
4) Output order? -> Any order of groups and words is acceptable unless specified.

Approaches:

1) Sorting-Key HashMap
   Idea:
     - Sort characters of each word; use the sorted string as the key.
     - All anagrams share the same sorted form.
   Complexity:
     - Let n = number of strings, k = max length
     - Time:  O(n * k log k)  (sort each string)
     - Space: O(n * k)        (store keys and groups)

2) Character-Count Key (Optimized)
   Idea:
     - Build a 26-length frequency vector for each word (for 'a'..'z'); use tuple(freq) as key.
     - Avoids per-word sorting.
   Complexity:
     - Time:  O(n * k)        (count chars once per word)
     - Space: O(n * k)        (keys + groups)
"""

from typing import List
from collections import defaultdict

class Solution:
    # ---------- Approach 1: Sorting-Key HashMap ----------
    def groupAnagrams_sorted(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))  # e.g., "eat" -> "aet"
            groups[key].append(word)
        return list(groups.values())

    # ---------- Approach 2: Character-Count Key (Optimized) ----------
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Default to the optimized O(n*k) approach.
        """
        groups = defaultdict(list)
        for word in strs:
            freq = [0] * 26  # assumes lowercase 'a'..'z'
            for ch in word:
                freq[ord(ch) - ord('a')] += 1
            groups[tuple(freq)].append(word)  # tuple is hashable; list isn't
        return list(groups.values())


if __name__ == "__main__":
    sol = Solution()
    sample = ["eat", "tea", "tan", "ate", "nat", "bat", ""]
    # Either method works; order of groups/words may differ.
    print("Sorted-key: ", sol.groupAnagrams_sorted(sample))
    print("Count-key : ", sol.groupAnagrams(sample))

