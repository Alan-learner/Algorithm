# encoding: utf-8
# author: Alan-learner

def get_ans(n: int):
    s = set()
    for i in range(2, 101, 2):
        for j in range(2, 101, 2):
            s.add(i + j)
    if n in s:
        return "YES"
    return "NO"


def main():
    res = get_ans(int(input()))
    print(res)


if __name__ == '__main__':
    main()
