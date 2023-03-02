# encoding: utf-8
# author: Alan-learner


def main():
    n = int(input())
    ans = 0
    for _ in range(n):
        if sum(map(int, input().split())) >= 2:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
