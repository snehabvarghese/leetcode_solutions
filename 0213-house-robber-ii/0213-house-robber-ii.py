class Solution:
    def rob(self, nums: list[int]) -> int:
        def maximumsubsq(nums):
            dp={}
            def solve(idx):
                if idx in dp:
                    return dp[idx]
                if idx==0:
                    return nums[idx]
                if idx<0:
                    return 0
                pick=nums[idx]+solve(idx-2)
                not_pick=solve(idx-1)
                dp[idx]=max(pick,not_pick)
                return dp[idx]
            return solve(len(nums)-1)
        def robber(nums):
            temp1=[]
            temp2=[]
            if len(nums)==1:
                return nums[0]
            for i in range(len(nums)):
                if i!=0:
                    temp1.append(nums[i])
                if i!=len(nums)-1:
                    temp2.append(nums[i])
            return max(maximumsubsq(temp1),maximumsubsq(temp2))
        return robber(nums)