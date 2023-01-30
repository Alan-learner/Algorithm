# encoding: utf-8
# author: Alan-learner

from Platform.Leetcode.Libs import *


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def is_red(idx: int) -> bool:
            # 红色表示当前二分的位置idx在 target 左侧
            end = nums[-1]
            if nums[idx] > end:
                # 当前下标位于第一段递增区间
                # target也同时处于第一段递增区间
                return nums[idx] > target > end
            else:
                return target > end or nums[idx] > target

        left = -1
        right = len(nums)  # 开区间(0,n-1)
        while left + 1 < right:
            mid = left + (right - left) // 2
            if is_red(idx=mid):
                right = mid
            else:
                left = mid
        if nums[left] != target:
            return -1
        return left


def main():
    s = Solution()
    res = s.search([3, 5, 1], 3)
    print(res)


if __name__ == '__main__':
    main()
