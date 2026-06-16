from typing import List
from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)

        
        for u, v, time in times:
            adj_list[u].append((v, time))

        
        min_heap = []
        heapq.heappush(min_heap, (0, k))

       
        visited = {}

        while min_heap:
            curr_time, node = heapq.heappop(min_heap)

            
            if node in visited:
                continue

            
            visited[node] = curr_time

            
            for adjnode, edge_time in adj_list[node]:
                if adjnode not in visited:
                    new_time = curr_time + edge_time
                    heapq.heappush(min_heap, (new_time, adjnode))

        
        if len(visited) != n:
            return -1

        
        return max(visited.values())