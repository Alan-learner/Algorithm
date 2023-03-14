# encoding: utf-8
# author: Alan-learner

from Platform.Leetcode.Libs import *

"""
已知矩阵行和、列和，并且行列总和相等
构造矩阵
"""


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        r = len(rowSum)
        c = len(colSum)
        ans = [[0] * c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if rowSum[i] < colSum[j]:
                    cur = rowSum[i]
                else:
                    cur = colSum[j]
                ans[i][j] = cur
                rowSum[i] -= cur
                colSum[j] -= cur
        return ans


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
