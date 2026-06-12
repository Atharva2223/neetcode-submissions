"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def clone(self,visited,node):
        if node in visited:
            return visited[node]
        cloned_node = Node(node.val)
        visited[node] = cloned_node
        for neighbor in node.neighbors:
            cloned_node.neighbors.append(self.clone(visited,neighbor))
        return cloned_node
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if node is None:
            return
        visited = {}
        return self.clone(visited,node)
        
        