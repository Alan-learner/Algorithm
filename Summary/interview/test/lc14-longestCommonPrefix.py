# encoding: utf-8
# author: Alan-learner

from Platform.Leetcode.Libs import *


def get_pre_fix(x: str, y: str) -> str:
    length = 0
    for a, b in zip(x, y):
        if a == b:
            length += 1
        else:
            break
    return x[:length]


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]
        for s in strs:
            ans = get_pre_fix(ans, s)
        return ans


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
