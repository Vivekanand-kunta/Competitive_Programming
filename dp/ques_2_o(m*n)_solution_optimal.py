class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp=[[-1 for i in range(len(text2))] for i in range(len(text1))]

        def rec(i,j):
            if i==len(text1) or j==len(text2):
                return 0
            if dp[i][j]>=0:
                return dp[i][j]
            else:
                if text1[i]==text2[j]:
                    return 1+rec(i+1,j+1)
                else:
                    l1=rec(i,j+1)
                    l2=rec(i+1,j)
                    dp[i][j]=max(l1,l2)
                    return dp[i][j]
        
        return rec(0,0)
