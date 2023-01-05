# encoding: utf-8
# author: Alan-learner

from Leetcode.Libs import *


# time complexity: O(m+n)
# space complexity: O(1)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # （原地）合并两个有序数组
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tail = m + n  # 指向待合并的位置
        m -= 1
        n -= 1
        while m > -1 or n > -1:
            tail -= 1
            if m == -1:
                nums1[tail] = nums2[n]
                n -= 1
            elif n == -1:
                nums1[tail] = nums1[m]
                m -= 1
            elif nums1[m] < nums2[n]:
                nums1[tail] = nums2[n]
                n -= 1
            else:
                nums1[tail] = nums1[m]
                m -= 1


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
