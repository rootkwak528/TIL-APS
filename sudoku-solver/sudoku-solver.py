class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows, cols, sqrs = [], [], []
        base = set(map(str, range(1, 10)))
        
        for row in board:
            rows.append(base - set(row))
        
        for col in zip(*board):
            cols.append(base - set(col))
            
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                sqr = board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3]
                sqrs.append(base - set(sqr))
        
        flag = [False]
        cands = [[None] * 9 for _ in range(9)]       
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    cands[i][j] = rows[i] & cols[j] & sqrs[(i//3)*3+j//3]
        
        
        def dfs(i, j):
            if flag[0]:
                return
            
            new_i, new_j = (i, j+1) if j < 8 else (i+1, 0)
            flag[0] = new_i == 9
            
            if board[i][j] == '.':
                k = (i//3)*3+j//3
                candidates = rows[i] & cols[j] & sqrs[k]
                
                for num in candidates:
                    
                    board[i][j] = str(num)
                    rows[i].remove(num)
                    cols[j].remove(num)
                    sqrs[k].remove(num)
                    
                    dfs(new_i, new_j)
                    
                    if flag[0]:
                        return
                    
                    board[i][j] = '.'
                    rows[i].add(num)
                    cols[j].add(num)
                    sqrs[k].add(num)

            else:
                dfs(new_i, new_j)
                
                
        dfs(0, 0)