class Solution:
    def rob(self, nums: list[int]) -> int:
        dp={}
        def solve(idx):
            if idx in dp:
                return dp[idx]
            if idx==0:
                return nums[idx]
            if idx<0:
                return 0
            pick=nums[idx]+solve(idx-2)
            not_pick=0+solve(idx-1)
            dp[idx]= max(pick,not_pick)
            return dp[idx]
        return solve(len(nums)-1)