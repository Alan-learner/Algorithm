# encoding: utf-8
# author: Alan-learner


def main():
    n = int(input())
    for _ in range(n):
        x = int(input())
        ans = 0
        while x >= 10:
            m, r = divmod(x, 10)
            ans += x - r
            x = m + r
        print(ans + x)


if __name__ == '__main__':
    main()
