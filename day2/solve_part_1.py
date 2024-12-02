
def getLines(fileName):
    with open(fileName) as f:
        return f.read().splitlines()


def isValid(numbers):
    sortedNums = sorted(numbers)
    if not (numbers == sortedNums or list(reversed(numbers)) == sortedNums):
        return False
    previous = numbers[0]
    for number in numbers[1:]:
        if not (1 <= abs(number-previous) <= 3):
            return False
        previous = number
    return True


def main():
    lines = getLines('input.in')
    res = 0

    for line in lines:
        numbers = [int(x) for x in line.split()]
        if isValid(numbers):
            res += 1

    print(res)


if __name__ == '__main__':
    main()
