# __slots__使用
# 使用 __slots__ 来限制该class实例能添加的属性


class Student(object):  # 创建一个空的类
    pass


stu = Student()  # 创建一个Student的实例
stu.name = 'zhangsan'  # 动态给实例绑定一个属性
print(stu.name)


# 给实例绑定一个方法
def set_age(self, age):
    self.age = age


from types import MethodType

stu.set_age = MethodType(set_age, stu)  # 给实例绑定一个方法
stu.set_age(22)
print(stu.age)

stu2 = Student()  # 创建新的实例


# print(stu2.age)  # 尝试调用方法   会报错


class Person(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


p = Person()
p.name = 'lisi'
p.age = 23


# p.gender = 'man'   # 限定了允许动态绑定的属性名称 只有 name 和 age   所以绑定gender时会报错

class Teacher(Person):
    pass


t = Teacher()
t.name = 'wangwu'
t.age = 24
t.gender = 'man'  # __slots__定义的属性进队当前类实例起作用,对继承的子类不起作用


# @property使用
class Student2(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s = Student2()
s.score = 90


# s.score = '90'  # 会报错


# Test:利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution


class Screen(object):
    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, width):
        self._width = width

    @height.setter
    def height(self, height):
        self._height = height

    @property
    def resolution(self):
        return self._width * self._height


s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)


# 多重继承: 即可以继承多个父类   (与Java不同, Java是单继承)
class Animal(object):
    pass


class Mammal(Animal):
    pass


class Bird(Animal):
    pass


class Runnable(object):
    pass


class Flyable(object):
    pass


class Dog(Mammal, Runnable):  # 继承两个父类
    pass


class Parrot(Bird, Flyable):
    pass


# 定制类: 即重写原有的方法


class Fruit(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):  # 重写了__str__方法
        return 'Fruit object(name: %s)' % self.name

    __repr__ = __str__  # 重写__repr__ , 内部实现和__str__一样

print(Fruit('Apple'))

fruit = Fruit('Banana')
print(fruit)


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100000:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值

for n in Fib():
    print(n)
