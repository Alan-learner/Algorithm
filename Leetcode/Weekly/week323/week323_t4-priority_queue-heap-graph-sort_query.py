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
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        priority_queue = [(grid[0][0], 0, 0)]
        grid[0][0] = 0  # 标记为访问过的
        m, n = len(grid), len(grid[0])
        l = len(queries)
        ans = [0] * l
        cnt = 0
        for qi, q in sorted(enumerate(queries), key=lambda k: k[1]):
            # 按照值从大到小排序，便于增量累计查询
            while priority_queue and priority_queue[0][0] < q:
                cnt += 1
                val, x, y = heappop(priority_queue)
                for x_, y_ in (x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1):
                    if 0 <= x_ < m and 0 <= y_ < n and grid[x_][y_]:
                        # 属于范围内合法坐标，并且没有被访问
                        heappush(priority_queue, (grid[x_][y_], x_, y_))
                        grid[x_][y_] = 0  # 置为访问后的状态
            ans[qi] = cnt
        return ans


class Solution2:
    # 排序后使用bfs增量查询
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        l = len(queries)
        ans = [0] * l
        m, n = len(grid), len(grid[0])
        queries = sorted([(a, b) for a, b in zip(queries, range(l))])

        def bfs(k, se):
            visited = se
            q = deque(se)
            if grid[0][0] < k:
                q.append((0, 0))
                visited.add((0, 0))
            while q:
                x, y = q.popleft()
                for x_, y_ in (x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1):
                    if 0 <= x_ < m and 0 <= y_ < n:
                        if grid[x_][y_] < k and (x_, y_) not in visited:
                            q.append((x_, y_))
                            visited.add((x_, y_))
            return len(visited), visited

        se = set()
        for val, idx in queries:
            v, se2 = bfs(val, se)
            se = se2
            ans[idx] = v
        return ans


def main():
    s = Solution()
    res = s.maxPoints([[1, 2, 3], [2, 5, 7], [3, 5, 1]], [5, 6, 2])
    print(res)


if __name__ == '__main__':
    main()
