def getLines(fileName):
    with open(fileName) as f:
        return f.read().splitlines()


def main():
    lines = getLines('input.in')
    line = lines[0]

    nums = [int(x) for x in line]

    xss = []
    for i, value in enumerate(nums):
        for _ in range(value):
            myId = i // 2 if i % 2 == 0 else None
            xss.append(myId)

    while None in xss:
        if xss[-1] == None:
            xss.pop()
        else:
            xss[xss.index(None)] = xss.pop()

    res = sum(i*num for i, num in enumerate(xss))
    print(res)


if __name__ == '__main__':
    main()
