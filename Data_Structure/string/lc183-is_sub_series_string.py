# encoding: utf-8
# author: Alan-learner

from Platform.Leetcode.Libs import *


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt1 = Counter(ransomNote)
        cnt2 = Counter(magazine)
        for k, v in cnt1.items():
            if v > cnt2[k]:
                return False
        return True


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
