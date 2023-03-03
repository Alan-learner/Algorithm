# encoding: utf-8
# author: Alan-learner


def main():
    n = int(input())
    for _ in range(n):
        x = int(input())
        length = len(str(x))
        ans = 9 * (length - 1)
        ans += max(int(str(x)[0]) - 1, 0)
        if str(x) >= str(x)[0] * length:
            ans += 1
        print(ans)


if __name__ == '__main__':
    main()
