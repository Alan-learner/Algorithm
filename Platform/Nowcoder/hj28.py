import math

"""
题目描述
若两个正整数的和为素数，则这两个正整数称之为“素数伴侣”，如2和5、6和13，它们能应用于通信加密。现在密码学会请你设计一个程序，从已有的 N （ N 为偶数）个正整数中挑选出若干对组成“素数伴侣”，挑选方案多种多样，例如有4个正整数：2，5，6，13，如果将5和6分为一组中只能得到一组“素数伴侣”，而将2和5、6和13编组将得到两组“素数伴侣”，能组成“素数伴侣”最多的方案称为“最佳方案”，当然密码学会希望你寻找出“最佳方案”。

输入:

有一个正偶数 n ，表示待挑选的自然数的个数。后面给出 n 个具体的数字。

输出:

输出一个整数 K ，表示你求得的“最佳方案”组成“素数伴侣”的对数。


数据范围： 1 \le n \le 100 \1≤n≤100  ，输入的数据大小满足 2 \le val \le 30000 \2≤val≤30000 
输入描述：
输入说明
1 输入一个正偶数 n
2 输入 n 个整数

输出描述：
求得的“最佳方案”组成“素数伴侣”的对数。

"""


def check(num):  # 判断是否是素数
    for i in range(2, int(math.sqrt(num)) + 2):  # 除去1和本身的数没有其他的因子称为素数，但其实检验到int(math.sqrt(num)) + 1即可（数学证明略），不然会超时
        if num % i == 0:
            return False
    return True


def find(odd, visited, choose, evens):  # 配对的过程
    for j, even in enumerate(evens):
        if check(odd + even) and not visited[j]:  # 如果即能配对，这两个数之前没有配过对（即使两个不能配对visit值为0，
            # 但是也不能过是否是素数这一关，所以visit就可以看为两个能配对的素数是否能配对）
            visited[j] = True  # 代表这两个数能配对
            if choose[j] == 0 or find(choose[j], visited, choose,
                                      evens):  # 如果当前奇数没有和任何一个偶数现在已经配对，那么认为找到一组可以连接的，
                # 如果当前的奇数已经配对，那么就让那个与之配对的偶数断开连接，让他再次寻找能够配对的奇数
                choose[j] = odd  # 当前奇数已经和当前的偶数配对
                return True
    return False  # 如果当前不能配对则返回False


while True:
    try:
        num = int(input())
        a = input()
        a = a.split()
        b = []
        count = 0
        for i in range(len(a)):
            a[i] = int(a[i])
        evens = []
        odds = []
        for i in a:  # 将输入的数分为奇数和偶数
            if i % 2 == 0:
                odds.append(i)
            else:
                evens.append(i)
        choose = [0] * len(evens)  # choose用来存放当前和这个奇数配对的那个偶数
        for odd in odds:
            visited = [False] * len(evens)  # visit用来存放当前奇数和偶数是否已经配过对
            if find(odd, visited, choose, evens):
                count += 1
        print(count)
    except:
        break
