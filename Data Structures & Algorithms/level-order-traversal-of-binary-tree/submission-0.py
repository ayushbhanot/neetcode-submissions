# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        level = 0
        queue.append(root)

        def BFS(root):
            res = []
            if not root:
                return res
            while len(queue) > 0:
                level_size = len(queue)
                level_val = []
                for i in range (level_size):
                    curr = queue.popleft()
                    level_val.append(curr.val)
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
                res.append(level_val) 
            return res
        return BFS(root)
        
    

                
                