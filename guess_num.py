import random

num = random.choice(range(100))
guess = int(input('请输入一个数:'))
while True:
    if guess > num:
        print('输入数字过大')
    elif guess < num:
        print('输入数字过小')
    else:
        print('恭喜,猜对了')
        break
    guess = int(input('请输入一个数:'))
