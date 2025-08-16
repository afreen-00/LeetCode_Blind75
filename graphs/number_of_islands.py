"""
Problem: Number of Islands
Link: https://leetcode.com/problems/number-of-islands/

Clarification Questions:
1. Can the grid be empty? -> Yes, return 0
2. Are inputs always '0' and '1' (string)? -> Yes
3. What defines an island? -> 1's connected vertically or horizontally (not diagonally)
4. Modifying grid in place allowed? -> Yes, safe for interview

Approach:
1. Iterate through each cell in the grid
2. If a cell is '1', it's a new island → start DFS/BFS from there
3. DFS/BFS marks all connected '1's as '0' (visited)
4. Repeat until entire grid is scanned
5. Return the count of islands

Time Complexity: O(m * n)
Space Complexity: O(m * n) in worst case recursion stack
"""

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])

        def dfs(r: int, c: int):
            # Base cases: out of bounds or water
            if (
                r < 0 or c < 0 or
                r >= m or c >= n or
                grid[r][c] != '1'
            ):
                return
            
            # Mark as visited
            grid[r][c] = '0'

            # Explore neighbors
            dfs(r-1, c)  # up
            dfs(r+1, c)  # down
            dfs(r, c-1)  # left
            dfs(r, c+1)  # right

        count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    dfs(r, c)
                    count += 1
        return count


if __name__ == "__main__":
    sol = Solution()
    grid1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    grid2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]

    print(sol.numIslands(grid1))  # Output: 1
    print(sol.numIslands(grid2))  # Output: 3

