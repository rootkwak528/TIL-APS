class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        
        arr = []
        for row in mat:
            arr = sorted(set(arr))
            print(arr)
            idx = bisect.bisect_right(arr, target)
            arr = arr[:idx+1]
            
            tmp = []
            for num in row:
                tmp += [a + num for a in arr] if arr else [num]
            arr = tmp
        
        
        arr = sorted(set(arr))
        idx = bisect.bisect_right(arr, target)
        
        ans = float('inf')
        for x in (-1, 0, 1):
            if idx + x < len(arr):
                ans = min(ans, abs(arr[idx+x] - target))
                
        return ans