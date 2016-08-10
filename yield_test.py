#  yield:生成器   生成一个迭代器

import sys


def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a       # 将a放入迭代器中  最后返回迭代器
        a, b = b, a + b
        counter += 1
f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

# while True:
#     try:
#         print(next(f), end=" ")
#     except StopIteration:
#         sys.exit()


def test(n):
    for x in range(n):
        yield x

t = test(10)
while True:
    try:
        print(next(t), end=' ')
    except StopIteration:
        sys.exit()
