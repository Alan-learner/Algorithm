# encoding: utf-8
# author: Alan-learner

from Leetcode.Libs import *


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0] * (k + 1) for k in range(query_row + 10)]
        dp[0][0] = poured
        for i in range(query_row):
            for j in range(i + 1):
                if dp[i][j] <= 1:
                    continue
                res = dp[i][j] - 1
                dp[i + 1][j] += res / 2
                dp[i + 1][j + 1] += res / 2
        return min(1, dp[query_row][query_glass])


def main():
    s = Solution()
    res = s.champagneTower(poured=100000009, query_row=33, query_glass=17)
    print(res)


if __name__ == '__main__':
    main()
