from collections import Counter


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

    count = Counter(right)

    res = 0
    for num in left:
        res += count[num] * num

    print(res)


if __name__ == '__main__':
    main()
