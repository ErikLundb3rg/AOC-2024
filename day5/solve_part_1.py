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

    def valid(row):
        seen = set()
        rowSet = set(row)
        for number in row:
            seen.add(number)
            for req in previous[number]:
                if req not in seen and req in rowSet:
                    return False
        return True

    for row in rows:
        if valid(row):
            middleNumbers.append(row[len(row)//2])
    print(sum(middleNumbers))


if __name__ == '__main__':
    main()
