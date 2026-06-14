class Solution:
    
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]


        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        def dfs_algo(node,  visited):
            visited.add(node)
            
            

        
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    dfs_algo(neighbor,visited)
                    
        components = 0
        visited =set()

        for node in range(n):
            if node not in visited:
                dfs_algo(node,visited)
                components+=1
        return components
        
        
        