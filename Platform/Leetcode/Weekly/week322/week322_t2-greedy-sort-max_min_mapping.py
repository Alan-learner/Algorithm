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
    def dividePlayers(self, skill: List[int]) -> int:
        # 排序后总是让最小值和最大值匹配
        skill.sort()
        skill = deque(skill)
        ans = 0
        tmp = skill[0] + skill[-1]
        while skill:
            if skill[0] + skill[-1] != tmp:
                return -1
            ans += skill.pop() * skill.popleft()
        return ans


def main():
    s = Solution()
    res = s.dividePlayers(skill=[3, 2, 5, 1, 3, 4])
    print(res)


if __name__ == '__main__':
    main()
