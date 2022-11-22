# encoding: utf-8
# author: Alan-learner

from Leetcode.Libs import *

MOD = 10 ** 9 + 7


class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        n = len(nums) - 1
        for i, v in enumerate(nums):
            ans += (pow(2, i, MOD) - pow(2, n - i, MOD)) * v
        return ans % MOD


def main():
    s = Solution()
    res = s.sumSubseqWidths(nums=[2, 1, 3])
    print(res)


if __name__ == '__main__':
    main()
