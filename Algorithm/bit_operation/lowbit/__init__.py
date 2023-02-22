# encoding: utf-8
# author: Alan-learner

from Platform.Leetcode.Libs import *


class Solution:
    def alan_ac_1024(self, nums: List[int]) -> List[int]:
        ac = accumulate(nums, initial=0)
        return list(ac)


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
