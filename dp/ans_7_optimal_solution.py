class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = [0] + sorted(cuts) + [n]
        m = len(cuts)
        dp = [[-1] * m for _ in range(m)]
        
        def rec(i: int, j: int) -> int:
            if j <= i + 1:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            k = float('inf')
            for p in range(i + 1, j):
                cost = (cuts[j] - cuts[i]) + rec(i, p) + rec(p, j)
                k = min(k, cost)
            dp[i][j] =k
            return k

        return rec(0, m - 1)                

                
