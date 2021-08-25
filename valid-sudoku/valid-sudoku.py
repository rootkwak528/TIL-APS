class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def is_valid(row):
            dot_cnt = row.count('.')
            num_cnt = len(set(row)) - (dot_cnt > 0)
            return dot_cnt + num_cnt == 9
        
        for row in board:
            if not is_valid(row):
                return False
        
        for col in zip(*board):
            if not is_valid(col):
                return False
            
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                line = [board[i][j], board[i][j+1], board[i][j+2]]
                line += [board[i+1][j], board[i+1][j+1], board[i+1][j+2]]
                line += [board[i+2][j], board[i+2][j+1], board[i+2][j+2]]
                if not is_valid(line):
                    return False
                
        return True