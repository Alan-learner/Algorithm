# encoding: utf-8
# author: Alan-learner

from Leetcode.Libs import *


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # 酒杯金字塔从顶端倒 poured 数量 的香槟，求指定酒杯的香槟包含量
        dp = [[0] * (k + 1) for k in range(query_row + 10)]  # 第(i,j)杯子所流过的香槟
        dp[0][0] = poured  # 转移起点
        for i in range(query_row):
            for j in range(i + 1):
                if dp[i][j] <= 1:
                    # 香槟不会往下流了
                    continue
                res = dp[i][j] - 1  # 往下流的液体总和
                # 左右分半
                dp[i + 1][j] += res / 2
                dp[i + 1][j + 1] += res / 2
        return min(1, dp[query_row][query_glass])  # 按题意调整


def main():
    s = Solution()
    res = s.champagneTower(poured=100000009, query_row=33, query_glass=17)
    print(res)


if __name__ == '__main__':
    main()
