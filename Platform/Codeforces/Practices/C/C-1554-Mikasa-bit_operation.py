# encoding: utf-8
# author: Alan-learner

def get_ans(x, y):
    ans = 0
    y += 1
    for i in range(30, -1, -1):
        # 从高位到低位依次考虑
        a = x >> i & 1
        b = y >> i & 1
        if a > 0 and b == 0:
            break
        if a == 0 and b > 0:
            ans |= 1 << i
    return ans


def main():
    x = int(input())
    for _ in range(x):
        n, m = map(int, input().split())
        ans = get_ans(n, m)
        print(ans)

        # s = set()
        # for i in range(m + 1):
        #     s.add(i ^ n)
        # j = 0
        # if j not in s:
        #     print(j)
        # while j in s:
        #     j += 1
        #     if j not in s:
        #         print(j)
        #         break


if __name__ == '__main__':
    main()
