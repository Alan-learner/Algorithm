# encoding: utf-8
# author: Alan-learner

from Platform.Leetcode.Libs import *


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        gray = lambda x : x ^ (x >> 1)
        # nums = [gray(i) for i in range(1 << n)]
        # idx = nums.index(start)
        # return nums[idx:] + nums[:idx]
        return [gray(i) ^ start for i in range(1 << n)]


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
