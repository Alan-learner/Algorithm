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
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans = 0
        for i, n in enumerate(nums):
            x = bisect_left(nums, lower - n)
            y = bisect_left(nums, upper - n + 1) - 1
            ans += y - x + 1
            if x <= i <= y:
                ans -= 1
        return ans // 2


def main():
    s = Solution()
    # res = s.countFairPairs(nums=[0, 1, 7, 4, 4, 5], lower=3, upper=6)
    # res = s.countFairPairs(nums=[1, 7, 9, 2, 5], lower=11, upper=11)
    # res = s.countFairPairs(nums=[0, 0, 0, 0, 0, 0], lower=0, upper=0)
    # res = s.countFairPairs(nums=[-5, -7, -5, -7, -5], lower=-12, upper=-12)
    res = s.countFairPairs(nums=[0, 1, 7, 4, 4, 5], lower=3, upper=6)
    print(res)


if __name__ == '__main__':
    main()
