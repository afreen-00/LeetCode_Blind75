"""
Problem: Two Sum
Link: https://leetcode.com/problems/two-sum/

Clarification Questions:
1. Can nums contain negative numbers? -> Yes
2. Can nums be empty? -> Yes, return []
3. What to return if there is no answer? -> Return []
4. Can there be multiple answers? -> Return any one valid pair
5. Are indices 0-based? -> Yes

Approaches Covered:
1. Brute Force (O(n^2) time, O(1) space)
2. Hash Map Optimized (O(n) time, O(n) space)
"""

from typing import List

class Solution:
    def twoSum_bruteforce(self, nums: List[int], target: int) -> List[int]:
        """
        Brute Force:
        - Check every pair using nested loops
        - Time Complexity: O(n^2)
        - Space Complexity: O(1)
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    def twoSum_hashmap(self, nums: List[int], target: int) -> List[int]:
        """
        Optimized using Hash Map:
        - Store visited numbers in a dictionary {value: index}
        - For each number, check if target - num exists in dictionary
        - Time Complexity: O(n)
        - Space Complexity: O(n)
        """
        hashmap = {}
        for index, num in enumerate(nums):
            remaining = target - num
            if remaining in hashmap:
                return [index, hashmap[remaining]]
            hashmap[num] = index
        return []

# Example usage
if __name__ == "__main__":
    sol = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print("Brute Force:", sol.twoSum_bruteforce(nums, target))  # Output: [0, 1] or [1, 0]
    print("Hash Map:", sol.twoSum_hashmap(nums, target))        # Output: [0, 1] or [1,0]

