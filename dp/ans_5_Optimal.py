class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
        req = s // 2
        dp = {}  

        def rec(i: int, target: int) -> bool:
            if target == 0:
                return True
            if i == len(nums) or target < 0:
                return False
            if (i, target) in dp:
                return dp[i, target]
            
            dp[i, target] = rec(i + 1, target - nums[i]) or rec(i + 1, target)
            return dp[i, target]
        
        return rec(0, req)
