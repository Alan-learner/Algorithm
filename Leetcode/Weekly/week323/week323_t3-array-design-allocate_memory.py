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


class Allocator:

    def __init__(self, n: int):
        self.array = [0] * n  # mID大于0

    def allocate(self, size: int, mID: int) -> int:
        cnt = 0
        for i, v in enumerate(self.array):
            # 从左到右遍历，保证向左开始分配
            if v == 0:
                cnt += 1
                if cnt == size:
                    idx = i - size + 1
                    # 找到并分配大小为size的空间
                    self.array[idx:i + 1] = [mID] * size
                    return idx
            else:
                cnt = 0
        # 没找到则返回-1
        return -1

    def free(self, mID: int) -> int:
        cnt = 0
        for i, v in enumerate(self.array):
            if v == mID:
                self.array[i] = 0
                cnt += 1
        return cnt


class Allocator2:

    def __init__(self, n: int):
        self.room = [-1] * n
        # self.room = defaultdict(int)
        # self.room[0] = n

    def get_loc(self, sz):
        free = 0
        for idx, val in enumerate(self.room):
            if val == -1:
                free += 1
            else:
                free = 0
            if free >= sz:
                return idx - sz + 1
        return -1

    def allocate(self, size: int, mID: int) -> int:
        loc = self.get_loc(size)
        if loc == -1:
            return -1
        for k in range(size):
            self.room[loc] = mID
            loc += 1
        return loc - size

    def free(self, mID: int) -> int:
        cnt = 0
        for i, room in enumerate(self.room):
            if room == mID:
                self.room[i] = -1
                cnt += 1
        return cnt


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
