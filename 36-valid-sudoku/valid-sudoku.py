class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for element in row:
                if element == ".": continue
                if element in seen: return False
                seen.add(element)

        for col in range(9):
            seen = set()
            for row in range(9):
                element = board[row][col]
                if element == ".": continue
                if element in seen: return False
                seen.add(element)

        
        
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                seen = set()
                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):
                        element = board[r][c]
                        if element == ".": continue
                        if element in seen: return False
                        seen.add(element)

        return True