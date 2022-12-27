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
    def maximumTastiness(self, price: List[int], k: int) -> int:
        def check(x):
            q = deque()
            q.append(0)
            idx = bisect_left(price, price[q[-1]] + x)
            while len(q) < k and idx < len(price):
                q.append(idx)
                idx = bisect_left(price, price[q[-1]] + x)
            return len(q) == k

        price.sort()
        left = 0
        right = price[-1]
        while left + 1 < right:
            mid = left + (right - left) // 2
            if check(mid):
                left = mid
            else:
                right = mid
        return left


def main():
    s = Solution()
    res = s.maximumTastiness(price=[13, 5, 1, 8, 21, 2], k=3)
    print(res)


if __name__ == '__main__':
    main()
