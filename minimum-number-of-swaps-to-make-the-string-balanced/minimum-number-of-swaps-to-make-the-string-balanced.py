class Solution:
    def minSwaps(self, s: str) -> int:
        
        cnt = mcnt = 0
        for ch in s:
            
            if ch == '[':
                cnt += 1
            
            else:
                cnt -= 1
                mcnt = min(mcnt, cnt)
        
        return 0 if mcnt == 0 else (-mcnt + 1)//2