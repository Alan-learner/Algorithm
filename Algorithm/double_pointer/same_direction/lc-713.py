# encoding: utf-8
# author: Alan-learner

from Leetcode.Libs import *


# https://leetcode.cn/problems/subarray-product-less-than-k/

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # 乘积小于k的子数组个数
        if k <= 1:
            return 0
        ans = left = 0
        m = 1
        for right, v in enumerate(nums):
            m *= v
            while m >= k:
                m /= nums[left]
                left += 1
            ans += (right - left + 1)
        return ans


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
