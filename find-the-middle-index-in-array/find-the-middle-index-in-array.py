class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        
        sums, rev_sums = [0], [0]
        
        for num in nums:
            sums += [sums[-1] + num]
            
        for num in nums[::-1]:
            rev_sums += [rev_sums[-1] + num]
        rev_sums = rev_sums[::-1]
        
        for i in range(len(nums)):
            if sums[i] == rev_sums[i+1]:
                return i
        
        return -1