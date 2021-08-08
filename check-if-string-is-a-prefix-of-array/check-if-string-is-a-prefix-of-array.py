class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        
        si = wi = 0
        while si < len(s):
            if wi == len(words):
                return False
            
            if s[si:].startswith(words[wi]):
                si += len(words[wi])
                wi += 1
                
            else:
                return False
            
        return True