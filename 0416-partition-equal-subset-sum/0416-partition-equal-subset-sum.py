class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total=0
        
        for i in nums:
            total+=i
        if total%2!=0:
            return False
        target=total//2
        dp=[False]*(target+1)
        dp[0]=True
        for num in nums:
            for i in range(target,num-1,-1):
                if dp[i] or dp[i-num]:
                    dp[i]=True
        return dp[-1]
        
        


        