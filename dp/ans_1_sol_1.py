class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[[-1 for i in range(n+1)] for j in range(n)]

        def rec(i,j):
            if i ==n:
                return 0
            if dp[i][j+1]>=0:
                return dp[i][j+1]
            l1=0
            l2=0
            if j<0 or nums[i]>nums[j]:
                l1=1+rec(i+1,i)
            l2=rec(i+1,j)
            dp[i][j+1]=max(l1,l2)
            return dp[i][j+1]
        
        return rec(0,-1)

        
