"""
Problem: Best Time to Buy and Sell Stock
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Clarification Questions:
1. Can prices be empty? -> Yes, return 0
2. Can prices have negative values? -> No, stock prices are non-negative
3. What if no profit is possible? -> Return 0
4. Is only one transaction allowed? -> Yes, buy once and sell once

Approaches:
1. Brute Force (O(n^2) time, O(1) space)
2. Optimized (Track min price + max profit in one pass) – O(n) time, O(1) space
"""

from typing import List

class Solution:
    def maxProfit_optimized(self, prices: List[int]) -> int:
        """
        Optimized Approach:
        - Track the minimum price so far
        - At each day, calculate profit = price - min_price
        - Update max profit if higher
        Time: O(n), Space: O(1)
        """
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit

    def maxProfit_bruteforce(self, prices: List[int]) -> int:
        """
        Brute Force:
        - Check every possible buy/sell pair
        Time: O(n^2), Space: O(1)
        """
        max_profit = 0
        n = len(prices)
        for i in range(n - 1):
            for j in range(i + 1, n):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit
        return max_profit


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit_optimized([7,1,5,3,6,4]))  # Output: 5
    print(sol.maxProfit_optimized([7,6,4,3,1]))    # Output: 0

