class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d={0:-1}
        
        sum=0
        res=0
        for idx,val in enumerate(nums):
            if val==0:
                sum-=1
            elif val==1:
                sum+=1
            if sum in d:
                res=max(res,idx-d[sum])
            else:
                d[sum]=idx
        return res







