# encoding: utf-8
# author: Alan-learner

from Leetcode.Libs import *


# https://leetcode.cn/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 和大于等于target，并且长度最短的子数组长度
        ans = float("inf")
        left = s = 0
        for right, v in enumerate(nums):
            s += v
            while s >= target:
                ans = min(ans, right - left + 1)
                s -= nums[left]
                left += 1
        return ans if ans != float("inf") else 0


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
