def getLines(fileName):
    with open(fileName) as f:
        return f.read().splitlines()


def main():
    lines = getLines('input.in')

    stones = [int(x) for x in lines[0].split()]
    blinks = 75
    # if we re encounter a number, what do we know?
    # map number to count
    from collections import defaultdict, Counter
    numberToCount = Counter(stones)

    for _ in range(blinks):
        nextNumberToCount = defaultdict(int)
        for stone, amount in numberToCount.items():
            if stone == 0:
                nextNumberToCount[1] += amount
            elif len(str(stone)) % 2 == 0:
                digits = str(stone)
                half = len(digits) // 2
                firstHalf = int(digits[:half])
                secondHalf = int(digits[half:])
                nextNumberToCount[firstHalf] += amount
                nextNumberToCount[secondHalf] += amount
            else:
                nextNumberToCount[stone*2024] += amount
        numberToCount = nextNumberToCount

    # print(numberToCount)
    res = sum(v for v in numberToCount.values())
    print(res)


if __name__ == '__main__':
    main()
