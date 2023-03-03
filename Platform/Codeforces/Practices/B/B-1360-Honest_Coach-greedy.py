# encoding: utf-8
# author: Alan-learner

import math


def main():
    n = int(input())
    for _ in range(n):
        _ = int(input())
        nums = list(map(int, input().split()))
        nums.sort()
        pre = nums[0]
        ans = math.inf
        for i, v in enumerate(nums):
            if i:
                ans = min(v - pre, ans)
                pre = v
        print(ans)


if __name__ == '__main__':
    main()
