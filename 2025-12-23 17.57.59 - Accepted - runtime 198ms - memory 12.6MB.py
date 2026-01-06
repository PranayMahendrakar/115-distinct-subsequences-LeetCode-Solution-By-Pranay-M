class Solution(object):
    def numDistinct(self, s, t):
        m, n = len(s), len(t)
        
        # dp[j] = number of ways to form t[0:j] using s[0:i]
        dp = [0] * (n + 1)
        dp[0] = 1  # Empty string can be formed 1 way
        
        for i in range(1, m + 1):
            # Traverse backwards to avoid using updated values
            for j in range(min(i, n), 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]
        
        return dp[n]