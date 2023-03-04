# encoding: utf-8
# author: Alan-learner
from collections import Counter, defaultdict


def main():
    n, k = map(int, input().split())
    idles = list(map(int, input().split()))
    costs = list(map(int, input().split()))
    dic = defaultdict(list)
    for idle, cost in sorted(zip(idles, costs), key=lambda x: x[1], reverse=True):
        dic[idle].append(cost)
    tmp = []
    for k, v in dic.items():
        mx = max(v)
        idx = v.index(mx)
        v.pop(idx)
        # if not v:
        #     v = [0]
        tmp.extend(v)
    tmp.sort()
    print(sum(tmp[:k - len(dic)]))


if __name__ == '__main__':
    main()
