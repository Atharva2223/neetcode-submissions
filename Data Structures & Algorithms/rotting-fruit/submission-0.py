class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:        

        row = len(grid)
        col = len(grid[0])

        grid_copy = deepcopy(grid)
        freshcnt = 0

        queue = deque()

        for r in range(row):
            for c in range(col):
                if grid_copy[r][c] == 2:
                    queue.append((r,c))
                if grid_copy[r][c] == 1:
                    freshcnt += 1
        minutes = 0

        while len(queue) != 0 and freshcnt>0:

            minutes+=1
            total_rotten = len(queue)

            for _ in range(total_rotten):
                i,j = queue.popleft()

                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:

                    new_i,new_j = i+dx,j+dy
                    if new_i <0 or new_i == row or new_j < 0 or new_j == col:
                        continue
                    if grid_copy[new_i][new_j] == 0 or  grid_copy[new_i][new_j] == 2:
                        continue
                    freshcnt-=1
                    grid_copy[new_i][new_j] = 2
                    queue.append((new_i,new_j))
        if freshcnt>0:
            return -1
        return minutes
