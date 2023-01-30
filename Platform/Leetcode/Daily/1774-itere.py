# encoding: utf-8
# author: Alan-learner

from Platform.Leetcode.Libs import *


class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        ans = inf
        diff = inf
        size = len(toppingCosts)
        # 三进制数枚举
        for base in baseCosts:
            for k in range(0, pow(3, size)):
                tmp = base
                cnt = 0
                while k:
                    mul, res = divmod(k, 3)
                    tmp += res * toppingCosts[cnt]
                    k = mul
                    cnt += 1
                dif = abs(target - tmp)
                if dif == diff:
                    ans = min(ans, tmp)
                    diff = dif
                if dif < diff:
                    ans = tmp
                    diff = dif
        return ans


def main():
    s = Solution()
    res = s.closestCost(baseCosts=[9, 10, 1], toppingCosts=[1, 8, 8, 1, 1, 8], target=8)
    print(res)


if __name__ == '__main__':
    main()
