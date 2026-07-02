class Solution:
    def isValid(self, row:List[int]) -> bool:
        digits = [False] * 9 
        for num in row:
            if num == ".":
                continue
            val = int(num) - 1
            if digits[val]:
                return False
            digits[val] = True
        return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [[] for _ in range(9)]
        boxes = [[] for _ in range(9)]
        for i,row in enumerate(board):
            if not self.isValid(row):
                return False
            for j, num in enumerate(row):
                if num != ".":
                    cols[j].append(num)
                    box_idx = (i // 3) * 3 + (j // 3)
                    boxes[box_idx].append(num)
        for col in cols:
            if not self.isValid(col):
                return False
        for box in boxes:
            if not self.isValid(box):
                return False
        return True
        
        


        