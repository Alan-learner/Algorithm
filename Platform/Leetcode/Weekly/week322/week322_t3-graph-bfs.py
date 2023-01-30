# encoding: utf-8
# author: Alan-learner

import math
from collections import deque, defaultdict, Counter
from math import inf
from typing import List, Optional
from bisect import bisect_left, bisect_right
from functools import reduce
from heapq import heappush, heappop, heapreplace, heapify
from math import comb
from executing import cache
from yarl import cache_clear

from numpy import lcm
from sortedcontainers import SortedList
from itertools import permutations, combinations, accumulate

lowbit = lambda x: x & -x
MOD = int(1e9 + 7)
INF = int(1e20)


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        ans = inf
        graph = defaultdict(list)
        for i, j, cnt in roads:
            graph[i].append((j, cnt))
            graph[j].append((i, cnt))
        right = {0}
        right.add(n)

        def bfs(g, s):
            nonlocal right
            q = deque()
            q.append(s)
            visited = {s}
            while q:
                cur = q.popleft()
                for nst, score in g[cur]:
                    if nst in visited:
                        continue
                    right.add(nst)
                    visited.add(nst)
                    q.append(nst)

        bfs(graph, 0)
        bfs(graph, n)
        for x in right:
            for nst, score in graph[x]:
                # 动态记录符合条件的路径中最短的一条
                ans = min(ans, score)
        return ans


def main():
    s = Solution()
    res = s.minScore(28,
                     [[13, 1, 7712], [10, 26, 8243], [27, 13, 214], [16, 10, 5757], [26, 2, 1461], [6, 19, 5731], [22,
                                                                                                                   17,
                                                                                                                   7599], [
                          14, 21, 2123], [26, 28, 8857], [19, 17, 5478], [19, 25, 534], [12, 26, 5019], [10, 19,
                                                                                                         6315], [26, 24,
                                                                                                                 6965], [
                          8, 19, 7719], [1, 15, 5928], [13, 16, 7338], [5, 13, 1800], [9, 23, 6607], [13, 19, 5763], [
                          15, 11, 19], [24, 2, 542], [12, 24, 4507], [19, 28, 3891], [1, 19, 1074], [20, 12, 6900], [8,
                                                                                                                     6,
                                                                                                                     7278], [
                          16, 26, 7075], [27, 22, 1056], [19, 12, 554], [4, 18, 5824], [25, 28, 352], [6, 25, 8807], [7,
                                                                                                                      5,
                                                                                                                      9808], [
                          11, 7, 8298], [17, 8, 6415], [5, 26, 5034], [5, 16, 6159], [2, 27, 8001], [16, 19, 720], [19,
                                                                                                                    22,
                                                                                                                    2295], [
                          10, 20, 5053]])
    print(res)


if __name__ == '__main__':
    main()
