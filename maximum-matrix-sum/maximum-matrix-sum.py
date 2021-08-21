class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        
        n = len(matrix)
        cnt = 0
        min_v = float('inf')
        ans = 0
        for row in matrix:
            for x in row:
                if x < 0:
                    cnt += 1
                    
                abs_x = abs(x)
                min_v = min(min_v, abs_x)
                ans += abs_x
                
        return ans if cnt % 2 == 0 else ans - min_v * 2