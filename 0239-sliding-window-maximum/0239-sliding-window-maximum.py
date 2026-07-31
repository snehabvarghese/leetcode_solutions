from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        if len(nums)==1:
            return nums
        
        l,r=0,0
        res=[]
        q=deque()
        while r<len(nums):
            while q and nums[q[-1]]<nums[r]:
                q.pop()
            q.append(r)
            if l>q[0]:
                q.popleft()
            if (r+1)>=k:
                res.append(nums[q[0]])
                l+=1
            r+=1
        return res

        
        
        
        