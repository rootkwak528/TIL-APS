import heapq

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        piles = [-x for x in piles]
        heapq.heapify(piles)
        
        for _ in range(k):
            p = heapq.heappop(piles)
            p = -p - (-p//2)
            heapq.heappush(piles, -p)
            
        return -sum(piles)