# encoding: utf-8
# author: Alan-learner

from Platform.Leetcode.Libs import *


class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:

        def dist(x, y, x_, y_):
            tp = abs(x - x_) * abs(x - x_) + abs(y - y_) * abs(y - y_)
            return pow(tp, 0.5)

        ans = set()

        def bfs(circle):
            a, b, r = circle
            nonlocal ans
            vis = set()
            vis.add((a, b))
            q = deque([(a, b)])
            while q:
                tmp = deque()
                for nd in q:
                    x, y = nd
                    ans.add(nd)
                    for nst in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                        x_, y_ = nst
                        if nst not in vis:
                            if dist(a, b, x_, y_) <= r:
                                tmp.append(nst)
                        vis.add(nst)
                q = tmp

        for c in circles:
            bfs(c)

        return len(ans)


def main():
    s = Solution()
    res = s.countLatticePoints(circles=[[2, 2, 2], [3, 4, 1]])
    print(res)


if __name__ == '__main__':
    main()
