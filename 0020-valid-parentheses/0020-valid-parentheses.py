class Solution(object):
    def isValid(self, s):
        d={"(":")","{":"}","[":"]"}
        stack=[]
        for i in s:
            if i in "({[":
                stack.append(i)
                continue
                
            elif i==")":
                if stack and stack[-1]=="(":
                    stack.pop()
                else:
                    return False
                    
            elif i=="]":
                if stack and stack[-1]=="[":
                    stack.pop()
                else:
                    return False
                    
            elif i=="}":
                if stack and stack[-1]=="{":
                    stack.pop()
                else:
                    return False
                    
        return len(stack)==0
            
        