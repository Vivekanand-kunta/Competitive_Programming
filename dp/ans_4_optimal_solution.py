class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp=[[0 for i in range(len(grid[0]))] for i in range(len(grid))]

        def rec(i,j):
            if i==len(grid)-1:
                if j==len(grid[0])-1:
                    dp[i][j]=grid[i][j]
                    return dp[i][j]
                else:
                    if dp[i][j]>0:
                        return dp[i][j]
                    dp[i][j]=grid[i][j]+rec(i,j+1)
                    return dp[i][j]
            elif j==len(grid[0])-1:
                if dp[i][j]>0:
                    return dp[i][j]
                dp[i][j]=grid[i][j]+rec(i+1,j)
                return dp[i][j]
                
            if dp[i][j]>0:
                return dp[i][j]
            l1=rec(i+1,j)
            l2=rec(i,j+1)
            dp[i][j]=grid[i][j]+min(l1,l2)
            return dp[i][j]
        return rec(0,0)
        
