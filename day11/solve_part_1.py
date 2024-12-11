def getLines(fileName):
    with open(fileName) as f:
        return f.read().splitlines()


def main():
    lines = getLines('input.in')

    stones = [int(x) for x in lines[0].split()]
    blinks = 30

    for _ in range(blinks):
        newStones = []
        for stone in stones:
            if stone == 0:
                newStones.append(1)
            elif len(str(stone)) % 2 == 0:
                digits = str(stone)
                half = len(digits) // 2
                newStones.append(int(digits[:half]))
                newStones.append(int(digits[half:]))
            else:
                newStones.append(stone*2024)
        stones = newStones
    print(len(stones))


if __name__ == '__main__':
    main()
