class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0]=="0":
            return 0
        dp=[1,1]
        for idx,val in enumerate(s[1:],2):
            ways=0
            if val!="0":
                ways+=dp[idx-1]
            if 10<=int(s[idx-2] + val)<=26:
                ways+=dp[idx-2]
            dp.append(ways)
        return dp[-1]
