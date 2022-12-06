# encoding: utf-8
# author: Alan-learner

from Leetcode.Libs import *


def lower_bound_left(nums: List[int], target: int) -> int:
    # bisect_left
    # 二分， 在闭区间 [left, right] 查询第一个小于等于target的值
    n = len(nums)
    left = 0
    right = n - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1
    return left


def lower_bound_right(nums: List[int], target: int) -> int:
    # bisect_right(nums, target) - 1
    # 二分， 在闭区间 [left, right] 查询最后一个大于等于target的值
    n = len(nums)
    left = 0
    right = n - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return right


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 返回第一个大于等于target的数、第一个大于target的数
        n = len(nums)
        if n == 0:
            return [-1, -1]
        left = lower_bound_left(nums, target)
        # left = bisect_left(nums, target)
        # right = bisect_right(nums, target) -1 # nums中最后一个大于target的数
        right = lower_bound_right(nums, target)
        if left >= n or nums[left] != target:
            left = -1
        if right >= n or nums[right] != target:
            right = -1
        return [left, right]


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
