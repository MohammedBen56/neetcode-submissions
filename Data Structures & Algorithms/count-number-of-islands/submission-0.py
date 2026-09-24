class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res=0

        q= deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    res+=1
                    q.append((i,j))
                while q:
                    a,b = q.pop()
                    if grid[a][b]=="1": grid[a][b]="0"
                    else: continue
                    if a != 0: q.append((a-1,b))
                    if a != len(grid)-1: q.append((a+1,b))
                    if b != 0: q.append((a,b-1))
                    if b != len(grid[0])-1: q.append((a,b+1))
        
        return res

        