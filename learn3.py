#  枚举 Enum
from enum import Enum, unique
import logging

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)  # 默认给成员附上int类型的值,从1开始计数


# 自定义枚举类
@unique  # @unique装饰器可以帮助我们检查保证没有重复值。
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


day1 = Weekday.Sun
print(day1, ':', day1.value)


# 使用元类:metaclass


class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)


h = Hello()
h.hello()
print(type(Hello))
print(type(h))


# 利用type创建类
# 1.先定义函数


def fn(self, name='world'):
    print('hello', name)


# type() 三个参数:
# class的名称；
# 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
Hello2 = type('Hello2', (object,), dict(hello=fn))  # 创建Hello2 class
h2 = Hello2()
h2.hello()

# 错误处理
try:
    print('try...')
    r = 10 / 2
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')


def foo(s1):
    return 10 / int(s1)


def bar(s2):
    return foo(s2) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)


# main()
print('END main')

# 断言assert


def foo1(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n


def main1():
    foo1('0')

# main1()
print('END main1')


s = '0'
n = int(s)
logging.info('n = %d' % n)
# print(10 / n)


def fact(num):
    """

    Function to calculate n!
    Example:
    >>> fact(0)
    Traceback (most recent call last):
    ...
    ValueError
    >>> fact(2)
    2
    >>> fact(3)
    6
    >>> fact(10)
    3628800
    :param num:

    """

    if num < 1:
        raise ValueError()
    if num == 1:
        return 1
    return num * fact(n - 1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
