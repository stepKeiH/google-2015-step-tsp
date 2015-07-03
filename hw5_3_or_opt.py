#!/usr/bin/env python3
#3-opt

import sys
import math

from common import print_solution, read_input
import solver_greedy
import hw5_kruskal
from collections import defaultdict

def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def solve(cities):
    N = len(cities)

    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    def opt_3(size, path):
        total = 0
        Graph = defaultdict(dict)
        def add_edge(e1, e2):
            Graph[e1][e2] = Graph[e2][e1] = 1

        def remove_edge(e1, e2):
            del Graph[e1][e2]
            del Graph[e2][e1]

        for i in range(size):
            add_edge(path[i-1], path[i])

        def make_path():
            C = [0]
            s = list(Graph[0].keys())[0]
            p = 0
            while s != 0:
                a, b = Graph[s].keys()
                C.append(s)
                if a != p:
                    n = a
                else:
                    n = b
                p = s
                s = n
            return C

        while True:
            count = 0
            if size < 6:
                break
            for i in range(size - 4):
                i1 = i + 1
                for j in range(i + 2, size - 2):
                    j1 = j + 1
                    for k in range(j + 2, size):
                        if k == size - 1:
                            k1 = 0
                        else:
                            k1 = k + 1

                        if i != 0 or k1 != 0:
                            l1 = dist[path[i]][path[i1]]
                            l2 = dist[path[j]][path[j1]]
                            l3 = dist[path[k]][path[k1]]
                            l4 = dist[path[i]][path[k]]
                            l5 = dist[path[i1]][path[j1]]
                            l6 = dist[path[j]][path[k1]]
                            l7 = dist[path[i]][path[j1]]
                            l8 = dist[path[j]][path[k]]
                            l9 = dist[path[i1]][path[k1]]
                            l10 = dist[path[i1]][path[k]]
                            l11 = dist[path[i]][path[j]]
                            l12 = dist[path[j1]][path[k1]]

                            A = l1 + l2 + l3 - l4 - l5 - l6
                            B = l1 + l2 + l3 - l7 - l8 - l9
                            C = l1 + l2 + l3 - l7 - l10 - l6
                            D = l1 + l2 + l3 - l11 - l12 - l10
                            E = l1 + l2 - l11 - l5
                            F = l3 + l2 - l12 - l8
                            G = l1 + l3 - l4 - l9
                            change_value = max(A, B, C, D, E, F, G)
                            # print('change_val', change_value, file=sys.stderr)

                            if change_value > 0:
                                if change_value == A:
                                    # print('A')
                                    remove_edge(path[i],path[i1])
                                    remove_edge(path[j],path[j1])
                                    remove_edge(path[k],path[k1])
                                    add_edge(path[i],path[k])
                                    add_edge(path[j1],path[i1])
                                    add_edge(path[k1],path[j])
                                elif change_value == B:
                                    # print('B')
                                    remove_edge(path[i],path[i1])
                                    remove_edge(path[j],path[j1])
                                    remove_edge(path[k],path[k1])
                                    add_edge(path[i],path[j1])
                                    add_edge(path[k],path[j])
                                    add_edge(path[k1],path[i1])
                                elif change_value == C:
                                    # print('C')
                                    remove_edge(path[i],path[i1])
                                    remove_edge(path[j],path[j1])
                                    remove_edge(path[k],path[k1])
                                    add_edge(path[i],path[j1])
                                    add_edge(path[k],path[i1])
                                    add_edge(path[j],path[k1])
                                elif change_value == D:
                                    # print('D')
                                    remove_edge(path[i],path[i1])
                                    remove_edge(path[j],path[j1])
                                    remove_edge(path[k],path[k1])
                                    add_edge(path[i],path[j])
                                    add_edge(path[k],path[i1])
                                    add_edge(path[k1],path[j1])
                                elif change_value == E:
                                    # print('E')
                                    remove_edge(path[i],path[i1])
                                    remove_edge(path[j],path[j1])
                                    add_edge(path[i],path[j])
                                    add_edge(path[i1],path[j1])
                                elif change_value == F:
                                    # print('F')
                                    remove_edge(path[j],path[j1])
                                    remove_edge(path[k],path[k1])
                                    add_edge(path[j1],path[k1])
                                    add_edge(path[j],path[k])
                                elif change_value == G:
                                    # print('G')
                                    remove_edge(path[i],path[i1])
                                    remove_edge(path[k],path[k1])
                                    add_edge(path[i],path[k])
                                    add_edge(path[i1],path[k1])
                                path = make_path()
                                count += 1
            total += count
            if count == 0:
                break
        return path, total


    def or_opt(size, path):
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
            path, _ = opt_3(size, path)
            path, flag = or_opt(size, path)
            print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", file=sys.stderr)
            if flag == 0: return path

    def optimize2(size, path):
        while True:
            path, _ = or_opt(size, path)
            path, flag = opt_3(size, path)
            print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", file=sys.stderr)
            if flag == 0: return path

    path = hw5_kruskal.solve(cities)
    return optimize1(N, path)


if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    print_solution(solution)
