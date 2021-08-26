class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        
        preorder = preorder.split(',')
        
        def dfs(x):
            if x >= len(preorder):
                return -1
            
            if preorder[x] == '#':
                return 1
            
            left = dfs(x+1)
            if left == -1:
                return -1
            
            right = dfs(x+left+1)
            if right == -1:
                return -1
            
            return left + right + 1
        
        return dfs(0) >= 0 and dfs(0) == len(preorder)
        