class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        n = len(nums)
        
        arr = []
        for x in [str(bin(i)).split('b')[1] for i in range(17)]:
            if len(x) <= n:
                arr += ['0' * (n - len(x)) + x]
        
        for num in nums:
            if num in arr:
                arr.remove(num)
                
        return arr[0]