# encoding: utf-8
# author: Alan-learner

from Platform.Leetcode.Libs import *


class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = -inf
        left = 0
        right = len(height) - 1
        while left < right:
            area = (right - left) * min(height[left], height[right])
            if area > ans:
                ans = area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
