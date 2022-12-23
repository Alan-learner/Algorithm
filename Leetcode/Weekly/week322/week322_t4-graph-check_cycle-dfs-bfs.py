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
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        # 建图
        for x, y in edges:
            x -= 1
            y -= 1
            graph[x].append(y)
            graph[y].append(x)

        time = [0] * n
        clock = 0

        def bfs(start: int) -> int:
            # 返回当前起始点所能获取的最大编号
            mx = 0
            nonlocal clock
            clock += 1
            time[start] = clock
            q = deque([(start, base)])
            while q:
                nd, idx = q.popleft()
                # 动态记录所有点的编号，保留最大编号
                mx = max(mx, idx)
                for nst in graph[nd]:
                    if time[nst] != clock:
                        # 时间不相同，未被访问
                        time[nst] = clock
                        q.append((nst, idx + 1))
            return mx

        color = [0] * n

        def dfs(nd: int, col: int) -> bool:
            color[nd] = col  # 给当前节点染色
            node.append(nd)
            for nst in graph[nd]:
                if color[nst] == col:
                    # 相邻节点被染成了同一种颜色，则存在奇数环
                    return False
                if color[nst] == 0:
                    # 下一个节点还未被染色
                    if not dfs(nst, -col):
                        # 邻居不行的话，同样不行
                        return False
            return True

        ans = 0
        for i, c in enumerate(color):
            if c:
                # 已经被访问（染色）过
                continue
            node = []
            if not dfs(i, 1):
                # 存在奇数环
                return -1
            base = ans + 1
            for x in node:
                # 枚举每一个节点所产生的最大编号
                ans = max(ans, bfs(x))
        return ans


def main():
    s = Solution()
    res = s.magnificentSets(92,
                            [[67, 29], [13, 29], [77, 29], [36, 29], [82, 29], [54, 29], [57, 29], [53, 29], [68, 29],
                             [26, 29], [21, 29], [46, 29], [41, 29], [45, 29], [56, 29], [88, 29], [2, 29], [7, 29],
                             [5, 29], [16, 29], [37, 29], [50, 29], [79, 29], [91, 29], [48, 29], [87, 29], [25, 29],
                             [80, 29], [71, 29], [9, 29], [78, 29], [33, 29], [4, 29], [44, 29], [72, 29], [65, 29],
                             [61, 29]])
    print(res)


if __name__ == '__main__':
    main()
