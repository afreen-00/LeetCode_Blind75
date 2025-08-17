"""
Problem: Longest Palindromic Substring
Link: https://leetcode.com/problems/longest-palindromic-substring/

We include two approaches:

1) Brute Force
   - Enumerate all substrings s[i:j], check palindrome by reversing or two-pointers
   - Time:  O(n^3)   (n^2 substrings * O(n) check)
   - Space: O(1)

2) Dynamic Programming
   - Every single character is a palindrome, so set dp[i][i] = True
   - Handle length 2 substrings:
     If s[i] == s[i+1], then dp[i][i+1] = True and track the longest palindrome 
   - Fill DP for length ≥ 3 substrings: by increasing substring length so that dp[l+1][r-1] is already known
   - Keep track of best [l, r] while filling
   - Time:  O(n^2)
   - Space: O(n^2)
"""

class Solution:

    # ---------------- Brute Force ----------------
    def longestPalindrome_bruteforce(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        def is_pal(i: int, j: int) -> bool:
            # Two-pointer check, inclusive j
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        best_l, best_r = 0, 0
        for i in range(n):
            for j in range(i, n):
                if j - i > best_r - best_l and is_pal(i, j):
                    best_l, best_r = i, j
        return s[best_l:best_r+1]

    # ---------------- Dynamic Programming ----------------
    def longestPalindrome_dp(self, s: str) -> str:
        """
        Step-by-step DP plan:
          1) dp[l][r] means s[l..r] is a palindrome.
          2) Base case: length 1 → dp[i][i] = True for all i.
          3) Length 2: dp[i][i+1] = (s[i] == s[i+1]).
          4) Length >= 3:
             dp[l][r] = (s[l] == s[r]) AND dp[l+1][r-1]
             (We can also write: dp[l][r] = s[l]==s[r] and (r-l<3 or dp[l+1][r-1]))
          5) Iterate length L = 3..n so that dp[l+1][r-1] is already computed.
          6) Track best boundaries [best_l, best_r] as we go.
        """
        n = len(s)
        if n < 2:
            return s

        # dp table: False by default
        dp = [[False] * n for _ in range(n)]
        best_l, best_r = 0, 0  # default to any single char

        # 1) Length 1 substrings
        for i in range(n):
            dp[i][i] = True

        # 2) Length 2 substrings
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                best_l, best_r = i, i + 1

        # 3) Length >= 3
        for L in range(3, n + 1):         # current substring length
            for l in range(0, n - L + 1):
                r = l + L - 1             # inclusive right index
                if s[l] == s[r] and dp[l + 1][r - 1]:
                    dp[l][r] = True
                    # Update best if this palindrome is longer
                    if L > (best_r - best_l + 1):
                        best_l, best_r = l, r

        return s[best_l:best_r + 1]


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("babad", {"bab", "aba"}),
        ("cbbd", {"bb"}),
        ("a", {"a"}),
        ("ac", {"a", "c"}),
        ("forgeeksskeegfor", {"geeksskeeg"}),
        ("", {""}),
    ]

    for s, expected in tests:
        brute = sol.longestPalindrome_bruteforce(s)
        dp    = sol.longestPalindrome_dp(s)
        print(f"s='{s}'  brute='{brute}'  dp='{dp}'")

