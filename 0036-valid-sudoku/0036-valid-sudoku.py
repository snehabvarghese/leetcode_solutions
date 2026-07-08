# 5 3 . | . 7 . | . . .
# 6 . . | 1 9 5 | . . .
# . 9 8 | . . . | . 6 .
# rows = {}
# cols = {}
# boxes = {}

# cols =
# {
# 0:{'5','6'},
# 1:{'3','9'},
# 2:{'8'}
# }
# rows =
# {
# 0:{'5','3','7'},
# 1:{'6','1','9','5'},
# 2:{'9','8','6'}
# }
# boxes =
# {
# (0,0):{'5','3','6','9','8'},
# (0,1):{'7','1','9','5'},
# }
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=defaultdict(set)
        cols=defaultdict(set)
        box=defaultdict(set)
        for r in range(9):
            for c in range(9):
                num=board[r][c]
                if num==".":
                    continue
                if (num in rows[r] or num in cols[c] or num in box[(r//3,c//3)]):
                    return False
                rows[r].add(num)
                cols[c].add(num)
                box[(r//3,c//3)].add(num)
        return True










        