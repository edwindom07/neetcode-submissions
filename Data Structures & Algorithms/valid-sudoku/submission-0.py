class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        9x9, split into 9 boxes of 3x3
        check box, and line 

        Going across rows, we can check that row.
        Then we can store the 
        """
        for idx in range(9):
            row_set = set()
            col_set = set()
            box_set = set()
            for idy in range(9):
                row = board[idx][idy]
                col = board[idy][idx]
                # row = (row / 3) * 3 + (col / 3)
                # col = (col % 3) + (row % 3) * 3
                box = board[(idx // 3) * 3 + (idy // 3)][(idy % 3) + (idx % 3) * 3]
                if row in row_set or col in col_set or box in box_set:
                    return False
                if row != ".":
                    row_set.add(row)
                if col != ".":
                    col_set.add(col)
                if box != ".":
                    box_set.add(box)
        return True