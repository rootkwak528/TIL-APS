class Solution(object):
    def makeFancyString(self, s):
        
        ans = []
        cnt = 1
        prev = s[0]
        
        for ch in s[1:]:
            if ch == prev:
                cnt += 1
            else:
                ans += [prev * min(2, cnt)]
                prev = ch
                cnt = 1
        
        ans += [prev * min(2, cnt)]
        return ''.join(ans)