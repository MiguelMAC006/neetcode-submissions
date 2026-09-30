class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = set()
        count = 0

        def dfs(node):
            for nb in adj[node]:
                if nb not in visit:
                    visit.add(nb)
                    dfs(nb)
        
        for node in range(n):
            if node not in visit:
                visit.add(node)
                dfs(node)
                count += 1
        
        return count