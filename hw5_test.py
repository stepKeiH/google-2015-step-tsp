#!/usr/bin/env python3

import sys
import math
import itertools

from common import print_solution, read_input


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def solve(cities):

    N = len(cities)

    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    current_city = 0
    seq = [x for x in range(1,N)]
    ans_list = itertools.permutations(seq)

    best_ans = float("inf")
    best_root = None

    for a_root in ans_list:
        new_ans = 0
        for i in range(1,len(a_root)):
            new_ans += dist[a_root[i-1]][a_root[i]]
        new_ans += dist[0][a_root[0]] + dist[0][a_root[-1]]
        if new_ans < best_ans:
            best_ans = new_ans
            best_root = [0] + list(a_root)
    return best_root

if __name__ == '__main__':
    assert len(sys.argv) > 1
    solve(read_input(sys.argv[1]))
    solution = solve(read_input(sys.argv[1]))
    print_solution(solution)
