class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(n)]

        queue = deque()

        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        visited = [0] * n
        visited[0] = 1

        queue.append((0,-1))

        while len(queue) != 0:
            node,parent = queue.popleft()

            for adjnode in adj_list[node]:

                if visited[adjnode] == 0:
                    visited[adjnode] = 1
                    queue.append((adjnode,node))
                else:
                    if adjnode != parent:
                        return False
        return sum(visited) == n



        