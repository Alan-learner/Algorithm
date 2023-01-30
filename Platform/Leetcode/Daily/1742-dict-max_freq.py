# encoding: utf-8
# author: Alan-learner

from Platform.Leetcode.Libs import *


def get_res(x: int) -> int:
    # 返回int各位数之和 345 -> 13
    s = 0
    while x:
        a, b = divmod(x, 10)
        s += b
        x = a
    return s


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        # 求解给定边界内，数位之和的最大频率
        dic = defaultdict(int)
        ans = -inf
        for num in range(lowLimit, highLimit + 1):
            v = get_res(num)
            dic[v] += 1
            if dic[v] > ans:
                ans = dic[v]
        return ans


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
