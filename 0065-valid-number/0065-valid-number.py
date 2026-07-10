class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit=False
        seen_dot=False
        seen_exp=False
        for idx,ch in enumerate(s):
            if ch.isdigit():
                seen_digit=True
            elif ch in "+-":
                if idx !=0 and s[idx-1] not in "Ee":
                    return False 
            elif ch in "Ee":
                if seen_exp or not seen_digit:
                    return False
                seen_exp=True
                seen_digit=False
            elif ch in ".":
                if seen_dot or  seen_exp :
                    return False
                seen_dot=True
            else:
                return False
        return seen_digit
        

