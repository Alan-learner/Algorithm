# encoding: utf-8
# author: Alan-learner
from collections import Counter


def get_res(lst):
    cnt = Counter(lst)
    total = cnt[1] + 2 * cnt[2]
    if total % 2 == 1:
        return "NO"
    if cnt[2] % 2 == 1:
        if cnt[1] >= 2 and cnt[1] % 2 == 0:
            return "YES"
    else:
        if cnt[1] % 2 == 0:
            return "YES"
    return "NO"


def main():
    n = int(input())
    for _ in range(n):
        _ = int(input())
        nums = list(map(int, input().split()))
        res = get_res(nums)
        print(res)


if __name__ == '__main__':
    main()
