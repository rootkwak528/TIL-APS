from functools import lru_cache


class Solution:
    def maxProduct(self, s: str) -> int:
        
        @lru_cache(None)
        def rec(i, l, r):
            if i == len(s):
                if l and r and l == l[::-1] and r == r[::-1]:
                    return len(l) * len(r)
                return 0
            
            return max(rec(i+1, l, r), rec(i+1, l+s[i], r), rec(i+1, l, r+s[i]))
        
        return rec(0, '', '')