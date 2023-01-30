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
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        idx = inf
        for i, w in enumerate(words[startIndex:]+words[:startIndex]):
            if w == target:
                idx = i
                break
        for i, w in enumerate(words[:startIndex+1][::-1]+words[startIndex:][::-1]):
            if w == target:
                return min(idx, i)
        return -1


def main():
    s = Solution()
    res = s.closetTarget(
        ["odjrjznxpn", "cyulttuabe", "zqxkdoeszk", "yeewpgriok", "odjrjznxpn", "btqpvxpjzv", "ukyudladhk", "ukyudladhk",
         "odjrjznxpn", "yeewpgriok"],
        "odjrjznxpn",
        5)
    # res = s.closetTarget(words = ["a","b","leetcode"], target = "leetcode", startIndex = 0)
    print(res)


if __name__ == '__main__':
    main()
