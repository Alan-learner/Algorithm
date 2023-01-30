# encoding: utf-8
# author: Alan-learner

from Platform.Leetcode.Libs import *

MOD = 10 ** 9 + 7


class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        increasing_stack_left = []
        increasing_stack_right = []
        decreasing_stack_left = []
        decreasing_stack_right = []
        n = len(nums)
        max_right = [n] * n
        min_right = [n] * n
        for i in range(n - 1, -1, -1):
            while increasing_stack_right and nums[i] < nums[increasing_stack_right[-1]]:
                increasing_stack_right.pop()
            if increasing_stack_right:
                min_right[i] = increasing_stack_right[-1]
            increasing_stack_right.append(i)
            while decreasing_stack_right and nums[i] > nums[decreasing_stack_right[-1]]:
                decreasing_stack_right.pop()
            if decreasing_stack_right:
                max_right[i] = decreasing_stack_right[-1]
            decreasing_stack_right.append(i)
        ans = 0
        for i, num in enumerate(nums):
            while increasing_stack_left and num < nums[increasing_stack_left[-1]]:
                increasing_stack_left.pop()
            min_left = increasing_stack_left[-1] if increasing_stack_left else -1
            ans -= ((i - min_left) * (min_right[i] - i) - 1) * num
            increasing_stack_left.append(i)
            while decreasing_stack_left and nums[i] > nums[decreasing_stack_left[-1]]:
                decreasing_stack_left.pop()
            max_left = decreasing_stack_left[-1] if decreasing_stack_left else -1
            ans += ((i - max_left) * (max_right[i] - i) - 1) * num
            decreasing_stack_left.append(i)
        return ans % MOD


def main():
    s = Solution()
    res = s.sumSubseqWidths(nums=[2, 1, 3])
    print(res)


if __name__ == '__main__':
    main()
