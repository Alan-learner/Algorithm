# encoding: utf-8
# author: Alan-learner

from Leetcode.Libs import *


class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        # 求解最大值处于[left, right]的子数组
        ans = 0
        lft = rgt = -1
        for i, num in enumerate(nums):
            # 枚举满足题意区间的右边界，动态记录可行的左边界
            if num > right:
                # 满足题意区间的左边界的左界
                lft = i
            if num >= left:
                # 满足题意区间的左边界的右界
                rgt = i
            # 统计所有符合题意的边界数量，即为左边界的可变范围
            ans += rgt - lft
        return ans


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
