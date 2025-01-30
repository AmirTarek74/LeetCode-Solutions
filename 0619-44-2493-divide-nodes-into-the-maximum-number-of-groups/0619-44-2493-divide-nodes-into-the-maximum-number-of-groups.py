class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]
        parent = [-1] * n
        depth = [0] * n

        for edge in edges:
            adj_list[edge[0]-1].append(edge[1]-1)
            adj_list[edge[1]-1].append(edge[0]-1)
            self._union(edge[0]-1, edge[1]-1, parent, depth)
        
        groups = {}

        for node in range(n):
            num_group = self._get_number_of_groups(adj_list, node, n)
            if num_group == -1:
                return -1
            root_node = self._find(node, parent)
            groups[root_node] = max(groups.get(root_node, 0), num_group)
        
        res = sum(groups.values())

        return res
    
    def _find(self, node, parent):
        while parent[node] != -1:
            node = parent[node]
        return node
    
    def _union(self, node1, node2, parent, depth):
        node1 = self._find(node1, parent)
        node2 = self._find(node2, parent)

        if node1 == node2:
            return
        
        if depth[node1] < depth[node2]:
            node1, node2 = node2, node1
        parent[node2] = node1
        if depth[node1] == depth[node2]:
            depth[node1] += 1
    
    def _get_number_of_groups(self, adj_list, src_node, n):
        nodes_queue = deque()
        layer_seen = [-1] * n
        nodes_queue.append(src_node)
        layer_seen[src_node] = 0
        deepest_layer = 0

        # Perform BFS to calculate the number of layers (groups)
        while nodes_queue:
            num_of_nodes_in_layer = len(nodes_queue)
            for _ in range(num_of_nodes_in_layer):
                current_node = nodes_queue.popleft()
                for neighbor in adj_list[current_node]:
                    # If neighbor hasn't been visited, assign it to the next layer
                    if layer_seen[neighbor] == -1:
                        layer_seen[neighbor] = deepest_layer + 1
                        nodes_queue.append(neighbor)
                    else:
                        # If the neighbor is already in the same layer, return -1 (invalid partition)
                        if layer_seen[neighbor] == deepest_layer:
                            return -1
            deepest_layer += 1
        return deepest_layer
        