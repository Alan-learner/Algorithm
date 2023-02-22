# encoding: utf-8
# author: Alan-learner

from Platform.Leetcode.Libs import *


class Solution:
    def minOperations(self, n: int) -> int:
        # bfs
        # lst = [2**k for k in range(19)]
        # q = set()
        # q.add(n)
        # step = 0
        # while q:
        #     tmp = set()
        #     step += 1
        #     for nd in q:
        #         for m in lst:
        #             v1 = nd + m
        #             v2 = nd - m
        #             if v1 == 0 or v2 == 0:
        #                 return step
        #             tmp.add(v1)
        #             tmp.add(v2)
        #     q = tmp
        # return step

        def f(x: int) -> int:
            if x == 0:
                return 0
            lbt = lowbit(x)
            if x == lbt:
                return 1
            return 1 + min(f(x - lbt), f(x + lbt))

        return f(n)


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
