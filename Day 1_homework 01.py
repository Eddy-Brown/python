# 作业 1
a = input('请输入一个数：')
a= int(a)
if a % 2 == 0:
    print('平方值为：',a**2)
else:
    print('立方值为：',a**3)

# 作业 2  成绩满分为 100
while True:
    b = input('请输入成绩：')
    b = int(b)

    if b < 0 or b > 100:
        print('错误输入')
    elif b >= 90:
        print('等级为A')
    elif b >= 80:
        print('等级为B')
    elif b >= 70:
        print('等级为C')
    elif b >= 60:
        print('等级为D')
    else:
        print('等级为E')