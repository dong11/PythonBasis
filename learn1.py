import functools
import hello
import sys


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print('2015-3-25')


now()


def logger(text=''):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('begin call')
            print('%s, %s()' % (text, func.__name__))
            print('end call')
            # return func(*args, **kw)

        return wrapper

    return decorator


@logger('DEBUG')
def today():
    print('2015-3-25')


today()


# print(today.__name__)


@logger('DEBUG')
def today2():
    print('2015-3-25')


today2()

print(int('123456'))

print(int('100000', base=2))  # base=N 转换成几进制, 打印出还是以十进制的方式, 也就是字符串以N进制的形式转换成十进制

int2 = functools.partial(int, base=2)

print(int2('100'))

hello.test()

print(hello.__doc__)
print(hello.__author__)


# print(sys.path)


class Student(object):  # Student 类名   object:Student所继承的父类
    def __init__(self, name=None, score=0):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 80:
            print('A')
        elif 60 <= self.score < 80:
            print('B')
        else:
            print('C')


stu1 = Student('zhangsan', 80)
stu2 = Student()
stu2.name = 'lisi'
stu2.score = 55
stu1.print_score()
stu2.print_score()
stu1.get_grade()
stu2.get_grade()

print(stu1)


class Teacher(object):
    def print_name(self):
        print("This is a Teacher")


tech1 = Teacher()
tech2 = Teacher()
tech1.name = 'zhangsan'  # 使用动态绑定   因此tech2没有name属性    所以打印tech2.name会报错
print(tech1.name)


# print(tech2.name)


# 访问限制   __name  私有变量

class Person(object):
    def __init__(self, name, age, **kwargs):
        self.__name = name
        self.__age = age
        self.__kwargs = kwargs

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def print_info(self):
        print('%s:%s:%s' % (self.__name, self.__age, list(self.__kwargs)))


p1 = Person('zhangsan', 21)
p2 = Person('lisi', 22, gender='man')
p1.print_info()
p2.print_info()

print(type(p1))


# 继承与多态

class Animal(object):
    def run(self):
        print('Animal is running')


class Dog(Animal):
    def run(self):
        print('Dog is running')


class Cat(Animal):
    def run(self):
        print('Cat is running')


a = Animal()
d = Dog()
c = Cat()
a.run()
d.run()
c.run()

print(isinstance(a, Animal))
print(isinstance(d, Animal))
print(isinstance(c, Animal))
print(isinstance(d, Dog))
print(isinstance(c, Dog))


def run_twice(animal):
    animal.run()
    animal.run()


run_twice(d)
run_twice(c)

#  获取对象信息

d.name = 'husky'

if hasattr(d, 'name'):
    print(getattr(d, 'name'))

if hasattr(c, 'name'):
    print(getattr(c, 'name'))
else:
    setattr(c, 'name', 'cat')
    print(c.name)
