# encoding: utf-8
# author: Alan-learner

from Platform.Leetcode.Libs import *

MOD = 10 ** 9 + 7


class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        # 二分
        lm = lcm(a, b)  # 最小公倍数
        left, right = 0, min(a, b) * n  # 左右均为开区间
        while left + 1 < right:
            mid = left + (right - left) // 2  # 防止数组越界
            if mid // a + mid // b - mid // lm <= n:
                # 二分的判断标准
                left = mid
            else:
                right = mid
        return right % MOD

    def nthMagicalNumber2(self, n: int, a: int, b: int) -> int:
        # 暴力枚举
        if a == b:
            return a * n % MOD
        a, b = min(a, b), max(a, b)
        x = 1
        y = 0
        while n > 1:
            n -= 1
            if (x + 1) * a > (y + 1) * b:
                y += 1
            elif (x + 1) * a < (y + 1) * b:
                x += 1
            else:
                x += 1
                y += 1
        ans = max(a * x, b * y) % MOD
        return ans


def main():
    s = Solution()
    res = s.nthMagicalNumber(8, 8, 8)
    print(res)


if __name__ == '__main__':
    main()
