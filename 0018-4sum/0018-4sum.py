class Solution(object):
    def fourSum(self, nums, target):
        nums=sorted(nums)
        ans=set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                k=j+1
                m=len(nums)-1
                while(k<m):
                    s=nums[i]+nums[j]+nums[k]+nums[m]
                    if s<target:
                        k+=1
                    if s>target:
                        m-=1
                    
                    elif s==target:
                        ans.add(tuple([nums[i],nums[j],nums[k],nums[m]]))
                        k+=1
                        m-=1
                        while(k<m and nums[k]==nums[k-1]):
                            k+=1
                        while(k<m and nums[m]==nums[m+1]):
                            m-=1
        return [list(x) for x in ans ]
        