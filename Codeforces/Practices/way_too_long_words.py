# encoding: utf-8
# author: Alan-learner

def get_ans(s: str):
    if len(s) <= 10:
        return s
    ans = s[0] + str(len(s) - 2) + s[-1]
    return ans


def main():
    for k in range(int(input())):
        res = get_ans(input())
        print(res)


if __name__ == '__main__':
    main()
