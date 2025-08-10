class Solution:
    def uniquePathsWithObstacles(self, arr: List[List[int]]) -> int:
        dp=[[0 for i in range(len(arr[0]))] for i in range(len(arr))]
        
        def rec(i,j):
            if i==len(arr) or j==len(arr[0]):
                return 0
            if i==len(arr)-1 and j==len(arr[0])-1 and arr[i][j]==0:
                return 1 
            if dp[i][j]>0:
                return dp[i][j]
            if arr[i][j]==1:
                return 0
            else:
                right=rec(i,j+1)
                bottom=rec(i+1,j)
                dp[i][j]=(right+bottom)
                return dp[i][j]
        
        return rec(0,0)

        
        
