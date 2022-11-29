# encoding: utf-8
# author: Alan-learner

from Leetcode.Libs import *


class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        # 将数组划分为k个子数组，使得总的平均值最大
        n = len(nums)
        # f[i][j]为前i个元素划分为j个子数组的平均值之和的最大值, 1 <= i <= n, 1 <= j <= k
        f = [[0] * (k + 1) for _ in range(n + 1)]
        # 前缀和优化区间和查询效率
        ac = list(accumulate(nums, initial=0))
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                if j == 1:
                    # 转移的起点
                    f[i][j] = ac[i] / i
                    continue
                f[i][j] = -inf
                for m in range(j - 1, i):
                    # 枚举最后一个可划分子数组的位置
                    tmp = f[m][j - 1] + (ac[i] - ac[m]) / (i - m)
                    if tmp > f[i][j]:
                        f[i][j] = tmp
        return f[n][k]


def main():
    s = Solution()
    res = s.largestSumOfAverages(nums=[9, 1, 2, 3, 9], k=3)
    print(res)


if __name__ == '__main__':
    main()
