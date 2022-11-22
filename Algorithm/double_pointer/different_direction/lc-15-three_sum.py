# encoding: utf-8
# author: Alan-learner

from Leetcode.Libs import *


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        for i, v in enumerate(nums):
            if i > 0 and v == nums[i - 1]:
                continue
            if v + nums[i + 1] + nums[i + 2] > 0:
                break
            if v + nums[n - 3] + nums[n - 4] < 0:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                s = v + nums[j] + nums[k]
                if s < 0:
                    j += 1
                elif s > 0:
                    k -= 1
                else:
                    ans.append([v, nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return ans


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
