from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t=Counter(t)
        need=len(count_t)
        have=0
        minlen=float("inf")
        window={}
        res=""
        start=0
        for end , val in enumerate(s):
            window[val]=window.get(val,0)+1
            if window[val]==count_t[val]:
                have+=1
            while (have==need):
                if minlen>end-start+1:
                    minlen=end-start+1
                    res=s[start:end+1]
                window[s[start]]-=1
                if window[s[start]]<count_t[s[start]]:
                    have-=1
                start+=1
        return res