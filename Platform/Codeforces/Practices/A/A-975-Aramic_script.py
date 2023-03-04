# encoding: utf-8
# author: Alan-learner


def main():
    _ = int(input())
    lst = input().split()
    s = set()
    for c in lst:
        val = tuple(sorted(list(set(c))))
        s.add(val)
    print(len(s))


if __name__ == '__main__':
    main()
