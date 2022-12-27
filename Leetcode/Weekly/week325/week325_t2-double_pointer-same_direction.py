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
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        cnt = Counter(s)
        if k != 0 and len(cnt) < 3:
            return -1
        for v in cnt.values():
            if v < k:
                return -1
        n = len(s)
        ct = Counter()
        right = 0
        while ct["a"] < k or ct["b"] < k or ct["c"] < k:
            right += 1
            ct[s[-right]] += 1
        ans = right
        for left, val in enumerate(s):
            ct[val] += 1
            while right > 0 and ct[s[-right]] > k:
                ct[s[-right]] -= 1
                right -= 1
            ans = min(ans, left + right + 1)
        return ans


def main():
    s = Solution()
    res = s.takeCharacters("acba", 1)
    # res = s.takeCharacters(s="aabaaaacaabc", k=2)
    print(res)


if __name__ == '__main__':
    main()
