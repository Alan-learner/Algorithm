# encoding: utf-8
# author: Alan-learner

from Leetcode.Libs import *


class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        sm = sum(nums)
        nums = [nums[k] * n - sm for k in range(n)]
        m = n // 2
        s = set()
        for k in range(1, m + 1):
            for c in combinations(nums[:m], k):
                sm = sum(c)
                if sm == 0:
                    return True
                s.add(sum(c))
        for j in range(1, n - m):
            for b in combinations(nums[m:], j):
                sm = sum(b)
                if -sm in s or sm == 0:
                    return True
        return False


def main():
    s = Solution()
    res = s.splitArraySameAverage(nums=
                                  [18, 0, 16, 2])
    print(res)


if __name__ == '__main__':
    main()
