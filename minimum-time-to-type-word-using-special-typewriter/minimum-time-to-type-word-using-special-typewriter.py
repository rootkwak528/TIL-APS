class Solution:
    def minTimeToType(self, word: str) -> int:
        
        prev = 'a'
        answer = 0
        for ch in word:
            diff = abs(ord(ch) - ord(prev))
            tmp = min(diff, 26-diff) + 1
            prev = ch
            answer += tmp
        
        return answer