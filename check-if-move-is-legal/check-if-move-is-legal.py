class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        dd = [[1, -1], [1, 0], [1, 1], [0, -1], [0, 1], [-1, -1], [-1, 0], [-1, 1]]
        
        for dx, dy in dd:
            x, y = rMove, cMove
            isPass = False
            while 0 <= x + dx < 8 and 0 <= y + dy < 8:
                x += dx
                y += dy
                if board[x][y] == '.':
                    break
                if board[x][y] == color:
                    if isPass:
                        return True
                    else:
                        break
                else:
                    isPass = True
                    
        return False