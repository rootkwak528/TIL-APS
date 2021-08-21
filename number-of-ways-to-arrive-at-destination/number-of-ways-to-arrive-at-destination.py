from collections import defaultdict

MOD = 1e9 + 7

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        
        rd = defaultdict(list)
        for u, v, t in roads:
            rd[u] += [(v, t)]
            rd[v] += [(u, t)]
        
        time = [float('inf')] * n
        time[0] = 0
        counts = [0] * n
        counts[0] = 1
        
        heap = [(0, 0)]
        while heap:
            T, u = heapq.heappop(heap)
            
            if time[u] < T:
                continue
            
            for v, t in rd[u]:
                if time[v] == time[u] + t:
                    counts[v] += counts[u]
                    counts[v] %= MOD
                elif time[v] > time[u] + t:
                    time[v] = time[u] + t
                    counts[v] = counts[u]
                    heapq.heappush(heap, (time[v], v))
                    
        return int(counts[n-1] % MOD)