# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        queue = [root]
        idx = 0
        
        target = set()
        while idx < len(queue):
            cur = queue[idx]
            if cur.val in target:
                return True
            
            target.add(k - cur.val)
            
            queue += [cur.left] if cur.left else []
            queue += [cur.right] if cur.right else []
                
            idx += 1
            
        return False