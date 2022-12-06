# encoding: utf-8
# author: Alan-learner

from Leetcode.Libs import *


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = n * [0]
        for i, v in enumerate(boxes):
            if v == "1":
                for j in range(n):
                    ans[j] += abs(i - j)
        return ans


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
