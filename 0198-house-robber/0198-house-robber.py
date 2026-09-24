class Solution:
    def rob(self, nums: list[int]) -> int:
        dp=[0]*len(nums)
        dp[0]=nums[0]
        for i in range(1,len(nums)):
            pick=nums[i]
            if i>1:
                pick+=dp[i-2]
            not_pick=dp[i-1]
            dp[i]=max(pick,not_pick)
        return dp[-1]