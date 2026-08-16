class Solution:
    def checkTwoChessboards(self, cordinate1: str, cordinate2: str) -> bool:

        same1={"a","c","e","g"}
        same2={"b","d","f","h"}

        if (cordinate1[0] in same1 and cordinate2[0] in same1) or (cordinate1[0] in same2 and cordinate2[0] in same2):
            if (int(cordinate1[1])%2==0 and int(cordinate2[1])%2==0) or (int(cordinate1[1])%2!=0 and int(cordinate2[1])%2!=0):
                return True
        if (cordinate1[0] in same1 and cordinate2[0] in same2) or (cordinate1[0] in same2 and cordinate2[0] in same1):
            if (int(cordinate1[1])%2==0 and int(cordinate2[1])%2!=0) or (int(cordinate1[1])%2!=0 and int(cordinate2[1])%2==0):
                return True
        return False