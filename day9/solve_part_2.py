def getLines(fileName):
    with open(fileName) as f:
        return f.read().splitlines()


def main():
    lines = getLines('input.in')
    line = lines[0]

    nums = [int(x) for x in line]

    xss = []
    spaces = []
    files = []
    # get spaces of (pos, length)
    # get files of (pos, id, length)
    # we try and fill space with a file from the back
    # remember to add new space if we move a file

    pos = 0
    for i, value in enumerate(nums):
        if i % 2 == 0:
            files.append((pos, i//2, value))
            for _ in range(value):
                xss.append(i//2)
                pos += 1
        else:
            spaces.append((pos, value))
            for _ in range(value):
                xss.append(None)
                pos += 1

    for filePos, fileId, fileLength in reversed(files):
        for spaceIndex, (spacePos, spaceLength) in enumerate(spaces):
            if spacePos < filePos and fileLength <= spaceLength:
                for i in range(fileLength):
                    xss[spacePos+i] = fileId
                    xss[filePos+i] = None

                spaces[spaceIndex] = (
                    spacePos+fileLength, spaceLength-fileLength)
                break

    x = 0
    for i, value in enumerate(xss):
        if value is not None:
            x += i*value
    print(x)


if __name__ == '__main__':
    main()
