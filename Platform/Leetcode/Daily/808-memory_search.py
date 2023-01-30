# encoding: utf-8
# author: Alan-learner

from Platform.Leetcode.Libs import *


class Solution:
    def soupServings(self, n: int) -> float:
        @cache
        def f(i, j):
            # 定义 f(i,j) 为剩下i份A汤、j份B汤时的概率
            if i <= 0 and j <= 0:
                return 0.5
            if i <= 0:
                return 1
            if j <= 0:
                return 0
            return 0.25 * (f(i - 4, j) + f(i - 3, j - 1) + f(i - 2, j - 2) + f(i - 1, j - 3))

        return f((n + 24) // 25, (n + 24) // 25) if n <= 4800 else 1


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
