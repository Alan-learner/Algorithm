# encoding: utf-8
# author: Alan-learner

from Platform.Leetcode.Libs import *


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])

        @cache
        def dfs(x, y):
            if x == 0 and y == 0:
                return set([grid[0][0]])
            res = set()
            if x - 1 >= 0:
                for v in dfs(x - 1, y):
                    res.add(v * grid[x][y])
            if y - 1 >= 0:
                for v in dfs(x, y - 1):
                    res.add(v * grid[x][y])
            return res

        ans = max(dfs(r - 1, c - 1))
        if ans >= 0:
            ans = ans % MOD
        else:
            ans = -1
        return ans


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
