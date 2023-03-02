# encoding: utf-8
# author: Alan-learner


def main():
    n = int(input())
    for _ in range(n):
        cnt = 0
        _ = input()
        arr = map(int, input().split())
        odd_diff = 0
        for i, v in enumerate(arr):
            if (i + v) % 2 == 1:
                cnt += 1
                if i % 2:
                    odd_diff += 1
        m, r = divmod(cnt, 2)
        if r != 0 or m != odd_diff:
            print(-1)
        else:
            print(m)


if __name__ == '__main__':
    main()
