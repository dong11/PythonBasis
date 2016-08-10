# IO操作

# 读文件 open():传入文件名和标识符'r':表示读
f = open('/Users/dong/PythonBasis/hello.py', 'r')  # 如果文件不存在,open()会抛出IOError的错误(FileNotFoundError)
content = f.read()
f.close()  # 文件打开使用完之后, 必须关闭, 避免占用资源
print(content)  # f.read()  将文件中的内容读取出来


with open('/Users/dong/PythonBasis/hello.py', 'r') as file:  # 利用with..as..来自动关闭
    for line in file.readlines():
        print(line.strip())

# f = open('/Users/michael/test.jpg', 'rb')  # 'rb':读取二进制文件
#
# f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')  # 读取非UTF-8的文件 需要在后面添加文件的编码
#
#
# f = open('/Users/michael/test.txt', 'w')  # 'w':写文件
# f.write('Hello, world!')
# f.close()


# with open('/Users/michael/test.txt', 'w') as f:
#     f.write('Hello, world!')

print('*****************************************')
# StringIO:在内存中读写字符串
from io import StringIO
f = StringIO()
f.write("hello")
print('write:' + f.getvalue())  # 通过getvalue()来读取内存中的字符串

f2 = StringIO('hello\nHi\nGoodBye')
while True:
    s = f2.readline()
    if s == '':
        break
    print(s)


#  BytesIO: 操作二进制文件   StringIO只能操作字符串
from io import BytesIO
b = BytesIO()
b.write('中文'.encode('utf-8'))
print(b.getvalue())

b2 = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(b2.getvalue())
print(b2.read())
