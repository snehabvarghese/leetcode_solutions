class Solution(object):
    def characterReplacement(self, s, k):
        mp={}
        
        res=0
        left=0
        for right in range(len(s)):
            mp[s[right]]=mp.get(s[right],0)+1
            while (right-left+1)-max(mp.values())>k:
                mp[s[left]]-=1
                left+=1
                
            res=max(res,right-left+1)
        return res
        