#!/usr/bin/env python3

import sys
import math

from common import print_solution, read_input

def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def solve(cities):
    N = len(cities)

    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    def make_edge(N):
        edges = [(i, j) for i in range(N - 1) for j in range(i + 1, N)]
        edges.sort(key = lambda x: dist[x[0]][x[1]])
        return edges

    def edge_to_path(edges, N):
        def search_edge(x):
            r = []
            for i in range(N):
                if edges[i][0] == x:
                    r.append(edges[i][1])
                elif edges[i][1] == x:
                    r.append(edges[i][0])
            return r

        path = [0] * N
        for i in range(N - 1):
            x, y = search_edge(path[i])
            if i == 0:
                path[i + 1] = x
                path[-1] = y
            elif path[i - 1] == x:
                path[i + 1] = y
            else:
                path[i + 1] = x
        return path

    def kruskal(N):
        edges = make_edge(N)
        edge_count = [0] * N
        u = UF(N)
        i = 0
        select_edge = []
        for e in edges:
            if edge_count[e[0]] < 2 and edge_count[e[1]] < 2 and (u.find(e[0]) != u.find(e[1]) or len(select_edge) == N - 1):
                u.union(e[0], e[1])
                edge_count[e[0]] += 1
                edge_count[e[1]] += 1
                select_edge.append(e)
                if len(select_edge) == N:
                    break
        return edge_to_path(select_edge, N)
    return kruskal(N)

def main():
    solution = solve(read_input(sys.argv[1]))
    print_solution(solution)

class UF:
    """An implementation of union find data structure.
    It uses weighted quick union by rank with path compression.
    """

    def __init__(self, N):
        """Initialize an empty union find object with N items.

        Args:
            N: Number of items in the union find object.
        """

        self._id = list(range(N))
        self._count = N
        self._rank = [0] * N

    def find(self, p):
        """Find the set identifier for the item p."""

        id = self._id
        while p != id[p]:
            id[p] = id[id[p]]   # Path compression using halving.
            p = id[p]
        return p

    def count(self):
        """Return the number of items."""

        return self._count

    def connected(self, p, q):
        """Check if the items p and q are on the same set or not."""

        return self.find(p) == self.find(q)

    def union(self, p, q):
        """Combine sets containing p and q into a single set."""

        id = self._id
        rank = self._rank

        i = self.find(p)
        j = self.find(q)
        if i == j:
            return

        self._count -= 1
        if rank[i] < rank[j]:
            id[i] = j
        elif rank[i] > rank[j]:
            id[j] = i
        else:
            id[j] = i
            rank[i] += 1

    def __str__(self):
        """String representation of the union find object."""
        return " ".join([str(x) for x in self._id])

    def __repr__(self):
        """Representation of the union find object."""
        return "UF(" + str(self) + ")"

if __name__ == '__main__':
    main()
