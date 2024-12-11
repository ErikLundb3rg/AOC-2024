def getLines(fileName):
    with open(fileName) as f:
        return f.read().splitlines()


def main():
    lines = getLines('input.in')

    grid = [[int(x) for x in line] for line in lines]

    M = len(grid)
    N = len(grid[0])

    def dfs(oR, oC, r, c, previous, visited):
        if not (0 <= r < M and 0 <= c < N):
            return 0
        if grid[r][c] != previous+1:
            return 0
        if (r, c) in visited:
            return 0
        visited.add((r, c))
        if grid[r][c] == 9:
            return 1

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        sm = 0
        for dR, dC in dirs:
            nR, nC = r+dR, c+dC
            sm += dfs(oR, oC, nR, nC, grid[r][c], visited)
        return sm

    res = 0
    for r in range(M):
        for c in range(N):
            if grid[r][c] == 0:
                res += dfs(r, c, r, c, -1, set())
    print(res)


if __name__ == '__main__':
    main()
