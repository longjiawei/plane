import random

while True:
    a = int(input('请输入你猜测的数字：'))
    b = random.randint(1,10)
    if a  == b :
        print('你猜对了😃')
    else:
        print('你猜错了(┬＿┬)')