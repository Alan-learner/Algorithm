# encoding: utf-8
# author: Alan-learner

from Leetcode.Libs import *


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = -1
        right = len(nums) -1 # 开区间
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid
        return right


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
