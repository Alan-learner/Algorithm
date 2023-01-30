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
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for g in grid:
            g.sort()
        ans = 0
        # while grid[0]:
        #     tmp = -inf
        #     for g in grid:
        #         tmp = max(g.pop(),tmp)
        #     ans += tmp
        # return ans
        for col in zip(*grid):
            # 将grid解包为不同行，再用zip一同迭代
            # 枚举每一列的更优雅写法
            ans += max(col)
        return ans


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
