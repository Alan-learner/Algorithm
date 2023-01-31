# encoding: utf-8
# author: Alan-learner

from Platform.Leetcode.Libs import *


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        ans = []
        q = [root]
        while q:
            t = []
            tmp = []
            for nd in q:
                tmp.append(nd.val)
                if nd.left: t.append(nd.left)
                if nd.right: t.append(nd.right)
            q = t
            ans.append(tmp)
        return ans


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
