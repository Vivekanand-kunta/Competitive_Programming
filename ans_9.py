class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minp = nums[0]
        maxp = nums[0]
        sol = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                minp, maxp = maxp, minp  
            maxp = max(nums[i], maxp * nums[i])
            minp = min(nums[i], minp * nums[i])
            sol = max(sol, maxp)

        return sol
