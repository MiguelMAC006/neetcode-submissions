class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()
        maxArea = 0

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))
            area = 1

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    if (r in range(ROWS) and
                    c in range(COLS) and
                    grid[r][c] == 1 and
                    (r, c) not in visited):
                        q.append((r, c))
                        visited.add((r, c))
                        area += 1
            
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    maxArea = max(bfs(r, c), maxArea)
        
        return maxArea