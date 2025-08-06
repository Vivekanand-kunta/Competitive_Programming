class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp=[[-1 for i in range(len(word2))] for i in range(len(word1))]
        w1=len(word1)
        w2=len(word2)
        def rec(i,j):
            if i==w1:
                return w2-j
            elif j==w2:
                return w1-i
            if dp[i][j]>0:
                return dp[i][j]
            
            if word1[i]==word2[j]:
                return rec(i+1,j+1)
            else:
                l1=1+rec(i+1,j+1)
                l2=1+rec(i,j+1)
                l3=1+rec(i+1,j)
                dp[i][j]=min(l1,l2,l3)
                return dp[i][j]
        return rec(0,0)   
        
