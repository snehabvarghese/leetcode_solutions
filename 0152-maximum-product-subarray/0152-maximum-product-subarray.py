class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_pro=min_pro=ans=nums[0]
        for i in nums[1:]:
            if i<0:
                max_pro,min_pro=min_pro,max_pro
            max_pro=max(i,i*max_pro)
            min_pro=min(i,i*min_pro)
            ans=max(ans,max_pro)
        return ans
        