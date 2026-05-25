class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(numCourses)]
        in_degree = [0 for _ in range(numCourses)]

        for u,v in prerequisites:
            adj_list[v].append(u)
            in_degree[u]+=1

        queue = deque()
        result = []
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        while len(queue) != 0:
            currNode = queue.popleft()
            result.append(currNode)

            for adjNode in adj_list[currNode]:
                in_degree[adjNode]-=1
                if in_degree[adjNode]==0:
                    queue.append(adjNode)

        if len(result) == numCourses:
            return result
        return []

        