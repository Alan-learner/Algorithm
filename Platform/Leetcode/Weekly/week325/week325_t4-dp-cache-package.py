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
    def countPartitions(self, nums: List[int], k: int) -> int:
        # 逆向思维：找坏分区：任意分组之和小于k的分区
        if sum(nums) < 2 * k:
            return 0
        MOD = int(1e9 + 7)

        # @cache
        # def dfs(i, left):
        #     if i == -1:
        #         return 1 if left > 0 else 0
        #     return dfs(i - 1, left) % MOD + dfs(i - 1, left - nums[i]) % MOD
        #
        # n = len(nums)
        # bad = dfs(n - 1, k)
        # ans = pow(2, n, MOD)
        # ans -= 2 * bad
        # return ans % MOD

        f = [0] * k
        # f[i] 表示总和小于i的选择数目
        f[0] = 1
        for x in nums:
            for j in range(k - 1, x - 1, -1):
                f[j] = (f[j] + f[j - x]) % MOD
        ans = pow(2, len(nums), MOD)
        ans -= sum(f) * 2
        return ans % MOD


def main():
    s = Solution()
    res = s.countPartitions(nums=[1, 2, 3, 4], k=4)
    print(res)


if __name__ == '__main__':
    main()
