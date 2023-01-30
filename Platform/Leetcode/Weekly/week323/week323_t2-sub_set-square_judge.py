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
    def longestSquareStreak(self, nums: List[int]) -> int:
        # 子序列 + 排序 => 子集
        s = set(nums)
        ans = -1
        for n in nums:
            tmp = 1
            while n in s:
                # log(n)复杂度
                tmp += 1
                n = n ** 2
            if tmp != 1:
                ans = max(ans, tmp)
        return ans


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
