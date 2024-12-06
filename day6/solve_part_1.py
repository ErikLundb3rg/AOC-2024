def getLines(fileName):
    with open(fileName) as f:
        return f.read().splitlines()


def main():
    lines = getLines('input.in')

    M = len(lines)
    N = len(lines[0])
    pos = None

    for r in range(M):
        for c in range(N):
            if lines[r][c] == '^':
                pos = (r, c)
                break
    # up right down left
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    r, c = pos
    dR, dC = dirs[0]
    positions = set()
    while True:
        positions.add((r, c))
        nR, nC = r+dR, c+dC
        if not (0 <= nR < M and 0 <= nC < N):
            break
        if lines[nR][nC] == '#':
            newIdx = (dirs.index((dR, dC)) + 1) % len(dirs)
            dR, dC = dirs[newIdx]
        r, c = r+dR, c+dC

    print(len(positions))


if __name__ == '__main__':
    main()
