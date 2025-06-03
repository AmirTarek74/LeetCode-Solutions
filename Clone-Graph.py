\\\
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
\\\

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        q = [node]
        clones = {node.val : Node(node.val, [])}

        while q:
            cur_node = q.pop(0)
            clone = clones[cur_node.val]
            for ngh in cur_node.neighbors:
                if ngh.val not in clones:
                    clones[ngh.val] = Node(ngh.val, [])
                    q.append(ngh)
                clone.neighbors.append(clones[ngh.val])
        return clones[node.val]