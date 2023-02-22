# encoding: utf-8
# author: Alan-learner

from Platform.Leetcode.Libs import *


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        suf_fix = [sum(piles)]
        for p in piles:
            # 后缀和
            val = suf_fix[-1] - p
            suf_fix.append(val)

        @cache
        def dfs(idx, m):
            if 2 * m >= len(piles) - idx:
                # 剩下的全部都能拿
                return suf_fix[idx]
            max_profit = -inf
            for x in range(1, 2 * m + 1):
                # 枚举所有决策，动态记录收益最大的那次
                max_profit = max(suf_fix[idx] - dfs(idx + x, max(m, x)), max_profit)
            return max_profit

        return dfs(0, 1)


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
