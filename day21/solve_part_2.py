import sys
import re
from collections import defaultdict, Counter
import pyperclip as pc
import itertools
from functools import cache


def getLines(fileName):
    with open(fileName) as f:
        return f.read().splitlines()


DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def pr(s):
    print(s)
    pc.copy(s)


def main():
    lines = getLines('input.in')
    numberPad = [
        ['7', '8', '9'],
        ['4', '5', '6'],
        ['1', '2', '3'],
        [None, '0', 'A'],
    ]
    keyPad = [
        [None, '^', 'A'],
        ['<', 'v', '>'],
    ]
    from collections import deque
    # I had an earlier bug in my compute_seqs code which
    # would permute and give impossible traversals,
    # seeing the code from youtube: hyperneutrino made me find the bug

    def compute_seqs(keypad):
        positions = {
            keypad[r][c]: (r, c)
            for r in range(len(keypad))
            for c in range(len(keypad[r]))
            if keypad[r][c] is not None
        }
        sequences = {}
        for start_key in positions:
            for end_key in positions:
                if start_key == end_key:
                    sequences[(start_key, end_key)] = ["A"]
                    continue

                queue = deque([(positions[start_key], "")])
                possible_sequences = []
                shortest_path = float("inf")

                while queue:
                    (current_row, current_col), path = queue.popleft()

                    for next_row, next_col, move in [
                        (current_row - 1, current_col, "^"),  # Up
                        (current_row + 1, current_col, "v"),  # Down
                        (current_row, current_col - 1, "<"),  # Left
                        (current_row, current_col + 1, ">")   # Right
                    ]:
                        if not (0 <= next_row < len(keypad) and 0 <= next_col < len(keypad[0])):
                            continue
                        if keypad[next_row][next_col] is None:
                            continue

                        if keypad[next_row][next_col] == end_key:
                            if len(path) + 1 > shortest_path:
                                continue
                            shortest_path = len(path) + 1
                            possible_sequences.append(path + move + "A")
                        else:
                            queue.append(((next_row, next_col), path + move))
                sequences[(start_key, end_key)] = possible_sequences
        return sequences

    numberP = compute_seqs(numberPad)
    keyP = compute_seqs(keyPad)

    @cache
    def dfs(code, depth, useNumberPad):
        length = 0
        code = 'A' + code
        if depth == 0:
            for i in range(len(code)-1):
                a, b = code[i], code[i+1]
                perms = (numberP[(a, b)] if useNumberPad else keyP[(a, b)])
                length += len(perms[0])
            return length
        for i in range(len(code)-1):
            a, b = code[i], code[i+1]
            mn = float('inf')
            for perm in (numberP[(a, b)] if useNumberPad else keyP[(a, b)]):
                mn = min(mn, dfs(perm, depth-1, False))
            length += mn
        return length

    res = 0
    for line in lines:
        res += dfs(line, 25, True) * int(line[:-1])
    print(res)


if __name__ == '__main__':
    main()
