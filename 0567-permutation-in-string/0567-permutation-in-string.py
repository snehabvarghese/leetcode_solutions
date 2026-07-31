
class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1)>len(s2):
            return False
        d1={}
        for i in s1:
            if i in d1:
                d1[i]+=1
            else:
                d1[i]=1
        left=0
        d2={}
        for i in range(len(s1)):
            d2[s2[i]]=d2.get(s2[i],0)+1
            if d1==d2:
                return True
            left=0
        for right in range(len(s1),len(s2)):
            d2[s2[right]]=d2.get(s2[right],0)+1
            
            d2[s2[left]]-=1
            if d2[s2[left]]==0:
                del d2[s2[left]]
            left+=1
            if d1==d2:
                return True
        return False

            
                
           