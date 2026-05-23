# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        queue = deque()

        res = []

        if root is None:
            return res

        queue.append(root)

        while len(queue)!= 0:

            levelSize = len(queue)

            for i in range(levelSize):

                node = queue.popleft()
                if i == levelSize-1:
                    res.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res

        