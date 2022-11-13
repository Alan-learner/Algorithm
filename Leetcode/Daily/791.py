# encoding: utf-8
# author: Alan-learner

from Leetcode.Libs import *


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        cnt = Counter(s)
        ans = ""
        for c in order:
            if c in cnt:
                ans += c * cnt[c]
                del cnt[c]
        while cnt:
            ch, feq = cnt.popitem()
            ans += ch * feq
        return ans


def main():
    s = Solution()
    res = s.customSortString(order="cba", s="abcd")
    print(res)


if __name__ == '__main__':
    main()
