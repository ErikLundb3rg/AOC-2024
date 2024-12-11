def getLines(fileName):
    with open(fileName) as f:
        return f.read().splitlines()


def main():
    lines = getLines('input.in')
    # group categories
    # for each category, go over pairs of points
    # for a pair of points, get delta of (r, c)
    # loop up and down with delta from point, place points in pointsSet
    antinodes = set()
    from collections import defaultdict
    groupToPoints = defaultdict(list)

    M = len(lines)
    N = len(lines[0])
    for r in range(M):
        for c in range(N):
            if lines[r][c] != '.':
                groupToPoints[lines[r][c]].append((r, c))

    def inside(r, c):
        return 0 <= r < M and 0 <= c < N

    for letter, points in groupToPoints.items():
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                a, b = points[i], points[j]
                dR = b[0] - a[0]
                dC = b[1] - a[1]

                c = b
                while inside(*c):
                    antinodes.add(c)
                    c = c[0] + dR, c[1]+dC
                d = a
                while inside(*d):
                    antinodes.add(d)
                    d = d[0] - dR, d[1] - dC
    print(len(antinodes))


if __name__ == '__main__':
    main()
