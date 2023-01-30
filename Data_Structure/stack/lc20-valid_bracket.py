# encoding: utf-8
# author: Alan-learner

from Platform.Leetcode.Libs import *


class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        dic = {")": "(", "}": "{", "]": "["}
        for c in s:
            if c in dic and stk and stk[-1] == dic[c]:
                stk.pop()
            else:
                stk.append(c)
        return False if stk else True


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
