# encoding: utf-8
# author: Alan-learner

from Platform.Leetcode.Libs import *


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        ans = []
        folder.sort()
        for f in folder:
            if f == "/":
                continue
            if not ans:
                ans.append(f)
                continue
            if len(f) >= len(ans[-1]) and ans[-1] + "/" in f[:len(ans[-1]) + 1]:
                continue
            ans.append(f)
        return ans


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
