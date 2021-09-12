class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        
        ratios = {}
        for w, h in rectangles:
            ratios[w/h] = ratios.get(w/h, 0) + 1
            
        answer = 0
        for v in ratios.values():
            answer += v * (v - 1) // 2
            
        return answer