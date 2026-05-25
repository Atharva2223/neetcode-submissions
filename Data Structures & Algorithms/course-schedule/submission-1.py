class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj_list = [[] for _ in range(numCourses)]
        in_degree = [0 for _ in range(numCourses)]

        for u,v in prerequisites:
            adj_list[u].append(v)
            in_degree[v]+=1

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
            return True
        return False




        