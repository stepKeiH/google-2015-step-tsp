#!/usr/bin/env python3

import sys
import math

from common import print_solution, read_input
import solver_greedy
import hw5_kruskal

def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def solve(cities):
    N = len(cities)

    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    def or_opt(size, path):
        total = 0
        while True:
            count = 0
            for i in range(size - 2):
                i1 = i + 1
                for j in range(i + 2, size):
                    if j == size - 1:
                        j1 = 0
                    else:
                        j1 = j + 1
                    if i != 0 or j1 != 0:
                        l1 = dist[path[i]][path[i1]]
                        l2 = dist[path[j]][path[j1]]
                        l3 = dist[path[i]][path[j]]
                        l4 = dist[path[i1]][path[j1]]
                        if l1 + l2 > l3 + l4:
                            new_path = path[i1:j+1]
                            path[i1:j+1] = new_path[::-1]
                            count += 1
            total += count
            if count == 0: break
        return path, total


    def opt_2(size, path):
        total = 0
        while True:
            count = 0
            for i in range(size):
                i0 = i - 1
                i1 = i + 1
                if i0 < 0: i0 = size - 1
                if i1 == size: i1 = 0
                for j in range(size):
                    j1 = j + 1
                    if j1 == size: j1 = 0
                    if j != i and j1 != i:
                        l1 = dist[path[i0]][path[i]]
                        l2 = dist[path[i]][path[i1]]
                        l3 = dist[path[j]][path[j1]]
                        l4 = dist[path[i0]][path[i1]]
                        l5 = dist[path[j]][path[i]]
                        l6 = dist[path[i]][path[j1]]
                        if l1 + l2 + l3 > l4 + l5 + l6:
                            p = path[i]
                            path[i:i + 1] = []
                            if i < j:
                                path[j:j] = [p]
                            else:
                                path[j1:j1] = [p]
                            count += 1
            total += count
            if count == 0: break
        return path, total

    def optimize1(size, path):
        while True:
            path, _ = opt_2(size, path)
            path, flag = or_opt(size, path)
            if flag == 0: return path

    def optimize2(size, path):
        while True:
            path, _ = or_opt(size, path)
            path, flag = opt_2(size, path)
            if flag == 0: return path

    path = hw5_kruskal.solve(cities)
    return optimize1(N, path)


if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    print_solution(solution)
