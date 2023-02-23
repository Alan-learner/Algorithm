# encoding: utf-8
# author: Alan-learner

from Platform.Leetcode.Libs import *


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = [root]
        while q:
            t = []
            tmp = []
            for nd in q:
                if nd.left:
                    t.append(nd.left)
                    tmp.append(nd.left.val)
                else:
                    tmp.append("")  # 判断是否结构对称
                if nd.right:
                    t.append(nd.right)
                    tmp.append(nd.right.val)
                else:
                    tmp.append("")
            q = t
            if tmp != tmp[::-1]:
                return False
        return True


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
