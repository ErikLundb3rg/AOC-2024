def getLines(fileName):
    with open(fileName) as f:
        return f.read().splitlines()


def main():
    lines = getLines('input.in')

    data = []
    for line in lines:
        target, rest = line.split(': ')
        numbers = [int(x) for x in rest.split()]
        data.append((int(target), numbers))

    res = 0
    for target, numbers in data:
        combinations = [numbers[0]]
        for number in numbers[1:]:
            newCombinations = []
            for c in combinations:
                newCombinations.append(number*c)
                newCombinations.append(number+c)
                joined = int(str(c)+str(number))
                newCombinations.append(joined)
            combinations = newCombinations
        if target in combinations:
            res += target
    print(res)


if __name__ == '__main__':
    main()
