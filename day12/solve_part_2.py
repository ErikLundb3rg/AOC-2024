import sys
import re
from collections import defaultdict, Counter, deque
import pyperclip as pc


def getLines(fileName):
    with open(fileName) as f:
        return f.read().splitlines()


def neighbors(r, c):
    return [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]  # down, up, right, left


def hNeighbors(r, c):
    return [(r, c+1), (r, c-1)]


def vNeighbors(r, c):
    return [(r+1, c), (r-1, c)]


def pr(s):
    print(s)
    pc.copy(s)


class UnionFind:
    """A minimalist standalone union-find implementation."""

    def __init__(self, n):
        self.count = n               # number of disjoint sets
        self.parent = list(range(n))  # parent of given nodes
        self.rank = [1]*n            # rank (aka size) of sub-tree

    def find(self, p):
        """Find with path compression."""
        if p != self.parent[p]:
            self.parent[p] = self.find(self.parent[p])  # path compression
        return self.parent[p]

    def union(self, p, q):
        """Union with ranking."""
        prt, qrt = self.find(p), self.find(q)
        if prt == qrt:
            return False
        self.count -= 1  # one more connection => one less disjoint
        if self.rank[prt] > self.rank[qrt]:
            prt, qrt = qrt, prt  # add small sub-tree to large sub-tree for balancing
        self.parent[prt] = qrt
        self.rank[qrt] += self.rank[prt]  # ranking
        return True

    def connectedComponents(self):
        return self.count


def main():
    lines = getLines('input.in')
    grid = lines

    visited = set()
    M = len(lines)
    N = len(lines[0])
    price = 0

    for bR in range(M):
        for bC in range(N):
            if (bR, bC) not in visited:
                q = [(bR, bC)]
                region = grid[bR][bC]
                area = 0
                visited.add((bR, bC))
                edges = []  # (r, c), facing

                while q:
                    r, c = q.pop(0)

                    # for face in ['u', 'r', 'd', 'l']:
                    #     edges.append((r, c, face))
                    area += 1

                    for (nR, nC), face in zip(neighbors(r, c), ['d', 'u', 'r', 'l']):
                        if not (0 <= nR < M and 0 <= nC < N):
                            edges.append((nR, nC, face))
                            continue
                        if grid[nR][nC] != region:
                            edges.append((nR, nC, face))
                            continue
                        if (nR, nC) in visited:
                            continue
                        visited.add((nR, nC))
                        q.append((nR, nC))
                uf = UnionFind(len(edges))
                for i in range(len(edges)):
                    for j in range(i+1, len(edges)):
                        (xR, xC, xFace), (yR, yC, yFace) = edges[i], edges[j]
                        if (yR, yC) in hNeighbors(xR, xC) and xFace == yFace and xFace in ['u', 'd']:
                            uf.union(i, j)
                        if (yR, yC) in vNeighbors(xR, xC) and xFace == yFace and xFace in ['l', 'r']:
                            uf.union(i, j)
                print(grid[bR][bC], area, uf.count)
                price += area*uf.count
    pr(price)


if __name__ == '__main__':
    main()
