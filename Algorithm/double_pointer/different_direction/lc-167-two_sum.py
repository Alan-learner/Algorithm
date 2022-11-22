# encoding: utf-8
# author: Alan-learner

from Leetcode.Libs import *


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 数组已经有序，可以利用其性质，及时弹出无用数据
        left = 0
        right = len(numbers) - 1
        s = numbers[left] + numbers[right]
        while s != target:
            if s > target:
                right -= 1
            else:
                left += 1
            s = numbers[left] + numbers[right]
        return [left + 1, right + 1]


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
