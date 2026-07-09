class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """  

        mp={}
        st=0
        e=0
        substr=""
        for i in range(len(s)):
            if s[i] in mp and st<mp[s[i]]+1:
                st=mp[s[i]]+1
                
            else:
                e=max(e,i-st+1)
                
                
            mp[s[i]]=i
            
        return e

                
                
        














        
        
        
        
 