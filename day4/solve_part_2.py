
def getLines(fileName):
    with open(fileName) as f:
        return f.read().splitlines()


def main():
    lines = getLines('input.in')

    M = len(lines)
    N = len(lines[0])
    res = 0

    def valid(coords):
        for r, c in coords:
            if not (0 <= r < M and 0 <= c < N):
                return False
        return True

    for bR in range(M):
        for bC in range(N):
            cross1 = [(bR, bC), (bR+1, bC+1), (bR+2, bC+2)]
            cross2 = [(bR+2, bC), (bR+1, bC+1), (bR, bC+2)]
            if not valid(cross1) or not valid(cross2):
                continue
            cross1 = "".join([lines[r][c] for r, c in cross1])
            cross2 = "".join([lines[r][c] for r, c in cross2])
            # print(cross1, cross2, bR)
            if cross1[::-1] != "MAS" and cross1 != "MAS":
                continue
            if cross2[::-1] != "MAS" and cross2 != "MAS":
                continue
            res += 1
    print(res)


if __name__ == '__main__':
    main()
