# encoding: utf-8
# author: Alan-learner

from Leetcode.Libs import *


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # 判断给定图中，环的数目
        n = len(isConnected)
        ufs = UnionFindSet(n)
        s = set()
        for i in range(n):
            for j in range(i, n):
                if isConnected[i][j]:
                    # 将连接的两个节点加入并查集和集合
                    s.add(i)
                    s.add(j)
                    ufs.merge(i, j)
        s_ = set()
        for valid_nd in s:
            # 判断最后组成的连通块的代表元有多少个，则有多多少个环
            s_.add(ufs.find(valid_nd))
        return len(s_)


def main():
    s = Solution()
    res = s


if __name__ == '__main__':
    main()
