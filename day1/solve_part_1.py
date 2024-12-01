def getLines(fileName):
    with open(fileName) as f:
        return f.read().splitlines()


def main():
    lines = getLines('input.in')
    left, right = [], []

    for line in lines:
        a, b = map(int, line.split())
        left.append(a)
        right.append(b)

    left.sort()
    right.sort()

    diff = 0
    for a, b in zip(left, right):
        diff += abs(a-b)

    print(diff)


if __name__ == '__main__':
    main()
