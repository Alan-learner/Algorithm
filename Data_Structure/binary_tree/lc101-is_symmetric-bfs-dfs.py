# encoding: utf-8
# author: Alan-learner

from Platform.Leetcode.Libs import *


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # q = [root]
        # while q:
        #     t = []
        #     tmp = []
        #     for nd in q:
        #         if nd.left:
        #             t.append(nd.left)
        #             tmp.append(nd.left.val)
        #         else:
        #             tmp.append("")
        #         if nd.right:
        #             t.append(nd.right)
        #             tmp.append(nd.right.val)
        #         else:
        #             tmp.append("")
        #     q = t
        #     if tmp != tmp[::-1]:
        #         return False
        # return True

        if not (root.left or root.right):
            return True

        def dfs(nd1, nd2):
            if not (nd1 or nd2):
                # 判断两个节点均为空的情况
                return True
            try:
                # 两个节点至少有一个不为空的情况
                cond = nd1.val == nd2.val
            except:
                cond = False
            if not cond:
                return False
            # 递归得判断左右子树对称情况
            if not dfs(nd1.left, nd2.right):
                return False
            if not dfs(nd1.right, nd2.left):
                return False
            return True

        return dfs(root.left, root.right)


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
