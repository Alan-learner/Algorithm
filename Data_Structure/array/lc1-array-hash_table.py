# encoding: utf-8
# author: Alan-learner

from Platform.Leetcode.Libs import *


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 找到数组中两个和为target的数组
        ans = []
        s = set()  # 哈希表存储target的补数，以便O(1)查询
        for i, n in enumerate(nums):
            tmp = target - n
            if tmp in s:
                ans.append(i)
                j = nums.index(tmp)
                ans.append(j)
                return ans
            s.add(n)


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
