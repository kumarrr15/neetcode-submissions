class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen_row = set()
            for i in range(len(row)):
                if row[i] == ".":
                    continue
                if row[i] not in seen_row:
                    seen_row.add(row[i])
                else:
                    return False
        for i in range(9):
            seen_col = set()
            for j in range(9):
                num = board[j][i]
                if num == ".":
                    continue
                if num not in seen_col:
                    seen_col.add(num)
                else:
                    return False
        seen_cell = []
        for i in range(9):
            seen_cell.append(set())
        for j in range(9):
            for i in range(9):    
                cell_id = (j // 3) * 3 + (i // 3)
                if board[j][i] == ".":
                    continue
                if board[j][i] not in seen_cell[cell_id]:
                    seen_cell[cell_id].add(board[j][i])
                else:    
                    return False
        return True

