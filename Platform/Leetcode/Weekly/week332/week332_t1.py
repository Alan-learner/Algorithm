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
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        ans = 0
        while nums:
            n = len(nums)
            if n >= 2:
                x = nums.pop()
                y = nums.pop(0)
                ans += int(str(y)+str(x))
            else:
                ans += nums.pop()
        return ans


def main():
    s = Solution()
    res = s
    # res = s.closetTarget(words = ["a","b","leetcode"], target = "leetcode", startIndex = 0)
    print(res)


if __name__ == '__main__':
    main()
