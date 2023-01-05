# encoding: utf-8
# author: Alan-learner

from Leetcode.Libs import *


# time complexity:O（n）
# space complexity:O（1）
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 只交易一次，从上帝视角看一段股票的最大收益
        ans = 0
        pre_min = prices[0]  # 维护之前股票的最低价格
        for p in prices:
            # 动态更新收益的最大值
            ans = max(ans, p - pre_min)
            if p < pre_min:
                pre_min = p
        return ans


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
