# encoding: utf-8
# author: Alan-learner

from Platform.Leetcode.Libs import *


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 求最大（连续）子数组和
        ans = max_pre_sum = nums[0]
        # 动态规划，定义f[i]为以nums[i]结尾并且和最大的子（连续）数组
        for n in nums[1:]:
            # 考察当前元素对答案的贡献
            if max_pre_sum > 0:
                # 值为正，有贡献
                # f[i] += nums[i]
                max_pre_sum += n
            else:
                # 值为负，无贡献
                # f[i] = nums[i]
                max_pre_sum = n
            ans = max(ans, max_pre_sum)
        return ans


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
