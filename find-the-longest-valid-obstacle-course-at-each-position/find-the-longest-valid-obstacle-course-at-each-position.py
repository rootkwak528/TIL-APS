from bisect import bisect_right

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        
        ans = []
        arr = [float('inf')]
        
        for o in obstacles:
            idx = bisect_right(arr, o)
            
            if idx == len(arr):
                arr.append(o)
            elif arr[idx] > o:
                arr[idx] = o
                
            ans += [idx+1]
            
        return ans