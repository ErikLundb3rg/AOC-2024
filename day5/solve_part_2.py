def getLines(fileName):
    with open(fileName) as f:
        return f.read().splitlines()


def main():
    lines = getLines('input.in')
    from collections import defaultdict
    previous = defaultdict(list)
    modeRules = True
    rows = []

    for line in lines:
        if not line:
            modeRules = False
            continue
        if modeRules:
            a, b = map(int, line.split('|'))
            previous[b].append(a)
        else:
            rows.append([int(x) for x in line.split(',')])

    middleNumbers = []

    def update(row):
        xToRank = defaultdict(int)

        for number in row:
            for otherNumber in row:
                if number != otherNumber and otherNumber in previous[number]:
                    xToRank[number] -= 1
                    xToRank[otherNumber] += 1

        row.sort(key=lambda x: xToRank[x])
        return row

    for row in rows:
        correct = update(row)
        print(row, correct)
        middleNumbers.append(correct[len(correct)//2])
    print(sum(middleNumbers))


if __name__ == '__main__':
    main()
