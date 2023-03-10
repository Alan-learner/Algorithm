# encoding: utf-8
# author: Alan-learner

from Platform.Leetcode.Libs import *


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # (x - y) % p = s % p
        # x % P - s % p = y % p
        # (x - s) % p = y % p
        ac = list(accumulate(nums, initial=0))
        sum_mod = ac[-1] % p
        if sum_mod == 0:
            return 0
        ans = n = len(nums)
        pre_mod = dict()
        for cur_idx, cur_sum in enumerate(ac):
            pre_mod[cur_sum % p] = cur_idx
            pre_idx = pre_mod.get((cur_sum - sum_mod) % p, -n)
            ans = min(cur_idx - pre_idx, ans)
        return ans if ans < n else -1


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
