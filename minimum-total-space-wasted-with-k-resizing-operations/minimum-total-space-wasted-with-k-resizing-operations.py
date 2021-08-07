from functools import lru_cache

class Solution:
    
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        
        grid = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
        
        for i in range(len(nums)):
            grid[i][i] = nums[i]
            for j in range(i + 1, len(nums)):
                grid[i][j] = max(grid[i][j-1], nums[j])
                
        @lru_cache(None)
        def helper(idx, k):
            if k == 0:
                return grid[idx][-1] * (len(nums) - idx)
            
            rtn = float('inf')
            for i in range(idx, len(nums) - k):
                tmp = grid[idx][i] * (i - idx + 1) + helper(i + 1, k - 1)
                rtn = min(rtn, tmp)
            
            return rtn
        
        return helper(0, k) - sum(nums)