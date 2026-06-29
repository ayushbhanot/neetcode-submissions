"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visit = {}

        def dfs(n):
            if not n:
                return

            if n not in visit:
                clone = Node(n.val)
                visit[n] = clone

            for neighbor in n.neighbors:
                if neighbor not in visit:
                    dfs(neighbor)
                visit[n].neighbors.append(visit[neighbor])
            return visit[n]

        return dfs(node)
        