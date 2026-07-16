class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        arr=[[-1]*len(text2) for _ in range(len(text1))]
        def lcs(i,j):
            
            if i==len(text1) or j==len(text2):
                return 0
            if arr[i][j] !=-1:
                return arr[i][j]
            elif text1[i]==text2[j]:
                arr[i][j]= 1+lcs(i+1,j+1)
            else:
                arr[i][j]= max(lcs(i,j+1),lcs(i+1,j))
            return arr[i][j]
        return lcs(0,0)
            