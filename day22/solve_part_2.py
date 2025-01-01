import sys
import re
from collections import defaultdict, Counter
import pyperclip as pc


def getLines(fileName):
    with open(fileName) as f:
        return f.read().splitlines()


DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def pr(s):
    print(s)
    pc.copy(s)


MOD = 16777216


def evolve(num):
    s1 = ((num*64) ^ num) % MOD
    s2 = ((s1 // 32) ^ s1) % MOD
    s3 = ((s2*2048) ^ s2) % MOD
    return s3


def main():
    lines = getLines('input.in')
    nums = [int(x) for x in lines]
    from collections import defaultdict
    sequenceToAddition = defaultdict(int)
    added = set()  # whether we added (line, sequence) to our defaultdict

    for i, num in enumerate(nums):
        res = num
        last4 = []
        lastDigit = res % 10
        for _ in range(2000):
            if len(last4) == 4:
                last4.pop(0)
            res = evolve(res)
            nextDigit = res % 10
            diff = lastDigit - nextDigit
            last4.append(diff)
            key = (i, *last4)
            if key not in added:
                added.add(key)
                sequenceToAddition[tuple(last4)] += nextDigit
            lastDigit = nextDigit
    print(max(sequenceToAddition.values()))


if __name__ == '__main__':
    main()
