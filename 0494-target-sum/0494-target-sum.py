class Solution:
    def findTargetSumWays(self, nums, target):
        memo={}
        def dp(i,n):
            if i==len(nums):
                return 1 if n==target else  0
            if (i,n) in memo:
                return memo[(i,n)]
            memo[(i,n)]= dp(i+1,n+nums[i])+dp(i+1,n-nums[i])
            return memo[(i,n)]
        return dp(0,0)
                
           
        