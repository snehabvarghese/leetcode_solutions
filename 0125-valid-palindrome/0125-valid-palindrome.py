class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        res=""
        for i in s:
            if i.isalnum():
                res+=i

        if res== res[::-1]:
            return True
        else:
            return False