class Solution(object):
    def threeSum(self, nums):
        nums=sorted(nums)
        ans=set()
        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            while(j<k):
                s=nums[i]+nums[j]+nums[k]
                if s>0:
                    k-=1
                if s<0:
                    j+=1
                elif s==0:
                    ans.add(tuple([nums[i],nums[j],nums[k]]))
                    j+=1
                    k-=1
                    while(j<k and nums[j]==nums[j-1]):
                        j+=1
                    while(j<k and nums[k]==nums[k+1]):
                        k-=1
        return [list(x) for x in ans]


