
def getLines(fileName):
    with open(fileName) as f:
        return f.read().splitlines()


def main():
    lines = getLines('input.in')

    M = len(lines)
    N = len(lines[0])
    word = "XMAS"
    res = [0]

    def dfs(r, c, index, visited, dir):
        if not (0 <= r < M and 0 <= c < N):
            return
        if (r, c) in visited:
            return

        if lines[r][c] != word[index]:
            return

        if index == 3:
            res[0] += 1
            return

        visited.add((r, c))

        dfs(r+dir[0], c+dir[1], index+1, visited, dir)
        visited.remove((r, c))

    for bR in range(M):
        for bC in range(N):
            for dR in range(-1, 2):
                for dC in range(-1, 2):
                    if (dR, dC) != (0, 0):
                        dfs(bR, bC, 0, set(), (dR, dC))

    print(res[0])


if __name__ == '__main__':
    main()
