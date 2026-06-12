from collections import deque

class Solution:

    def bfs(self, visited, grid, r, c):
        rows = len(grid)
        cols = len(grid[0])

        area = 1
        queue = deque()
        queue.append((r, c))
        visited[r][c] = 1

        while queue:
            i, j = queue.popleft()

            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                new_x, new_y = i + dx, j + dy

                if new_x < 0 or new_x >= rows or new_y < 0 or new_y >= cols:
                    continue

                if grid[new_x][new_y] == 0:
                    continue

                if visited[new_x][new_y]:
                    continue

                visited[new_x][new_y] = 1
                area += 1
                queue.append((new_x, new_y))

        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = [[0] * cols for _ in range(rows)]
        max_area = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and not visited[i][j]:
                    area = self.bfs(visited, grid, i, j)
                    max_area = max(max_area, area)

        return max_area