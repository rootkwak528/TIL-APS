class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        sm, bg = min(nums), max(nums)
        
        ans = 1
        for i in range(2, sm+1):
            if sm % i == 0 and bg % i == 0:
                ans = i
                
        return ans