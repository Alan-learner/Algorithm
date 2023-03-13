# encoding: utf-8
# author: Alan-learner
# 自带库
import math
from collections import deque, defaultdict, Counter
from math import inf
from typing import List, Optional
from bisect import bisect_left, bisect_right
import functools
from functools import reduce
from heapq import heappush, heappop, heapreplace, heapify
from math import comb
from executing import cache
from yarl import cache_clear
from string import ascii_lowercase
# 第三方库
from numpy import lcm
from sortedcontainers import SortedList
from itertools import permutations, combinations, accumulate
# 拓展库
from Data_Structure.unionfind_set.UnionFindSet import UnionFindSet
from copy import copy

MOD = 10 ** 9 + 7
lowbit = lambda x_: x_ & -x_
inf = int(1e20)


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def main():
    pass


if __name__ == '__main__':
    main()
