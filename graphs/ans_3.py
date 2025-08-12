class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        arr = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        sol = 0

        def rec(i, j):
            if i < 0 or i >= len(arr) or j < 0 or j >= len(arr[0]):
                return False
            if grid[i][j] == '0' or arr[i][j]:
                return False

            arr[i][j] = True
            
            rec(i-1,j)
            rec(i+1,j)
            rec(i,j+1)
            rec(i,j-1)

            return True

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if rec(i, j):
                    sol += 1
                

        return sol
