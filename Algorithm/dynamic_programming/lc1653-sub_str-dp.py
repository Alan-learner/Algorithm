# encoding: utf-8
# author: Alan-learner

from Platform.Leetcode.Libs import *


# 使得字符串成为递增子串的最小删除次数
class Solution:
    def minimumDeletions(self, s: str) -> int:
        # 方法一，观察被删除字符的特点，从左到右枚举所有分割线，动态记录最小删除次数
        # ans = a_count = s.count("a")
        # b_count = 0
        # for c in s:
        #     # 枚举所有的分割线
        #     if c == "b":
        #         b_count += 1
        #     else:
        #         a_count -= 1
        #     ans = min(a_count + b_count, ans)
        # return ans

        # 方法二，动态规划，遍历每一个字符，判断组成最长递增字符的最小代价
        f = b_count = 0
        for i, c in enumerate(s):
            if c == "a":
                f = min(b_count, f + 1)  # 判断删除前面所有的b、删除当前a两种决策哪种代价更小
            else:
                b_count += 1  # 保留b，顺便统计b的数量
        return f


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
