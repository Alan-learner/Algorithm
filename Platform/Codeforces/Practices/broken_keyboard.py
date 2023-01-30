# encoding: utf-8
# author: Alan-learner

from collections import deque


def Solution():
    def get_res():
        _ = int(input())
        q = deque(input())
        flag = 1
        while q:
            if flag:
                q.popleft()
            else:
                if len(q) < 2 or q.popleft() != q.popleft():
                    print("NO")
                    return
            flag ^= 1
        print("YES")

    n = int(input())
    for _ in range(n):
        get_res()


def main():
    Solution()


if __name__ == '__main__':
    main()
