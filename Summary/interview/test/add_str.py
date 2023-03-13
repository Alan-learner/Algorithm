# encoding: utf-8
# author: Alan-learner
import re

"""
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和并同样以字符串形式返回。
不能直接将输入的字符串转换为整数形式。
用例一： 输入：num1 = “11”, num2 = “123” 输出：“134”
"""

"""999 + 1"""

"""
def add(x, y):
    return x + y

add = lambda x, y: x + y

lst = re.findall(pattern="/d+", string="asdas123dad")
re.match()
re.search()"""


def get_res(num1: str, num2: str) -> str:
    res = []
    lst1 = list(num1)
    lst2 = list(num2)
    add = 0  # 表示进位
    while lst1 and lst2:
        x = int(lst1.pop())
        y = int(lst2.pop())
        s = x + y + add
        if s < 10:
            # 不存在进位
            res.append(str(s))
        else:
            # 存在进位
            res.append(str(s % 10))  # 当前位
            add = 1  # 进位
    while lst1:
        res.append(lst1.pop())
    while lst2:
        res.append(lst2.pop())
    ans = res[::-1]
    return ans


def main():
    res = get_res("112434", "123")
    print(res)


if __name__ == '__main__':
    main()
