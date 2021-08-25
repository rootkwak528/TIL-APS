class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        for a in range(int(math.sqrt(c/2)) + 1):
            b = (c - a**2)**0.5
            if abs(b - int(b)) <= 1e-6:
                return True
        return False