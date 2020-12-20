# 单行注释  快捷键ctrl+/
"""
多行注释
"""
'''
三对单引号或双引号
'''

print('Hello Python')
print("\n*****数据类型定义*****")
a = 12
aa = 3.4
bbb = False
stt = '蔡程昱'
print(stt)

print('\n*****检验数据类型*****')
# 声明一个变量为age
age = 17.44
# 检验类型
cls = type(stt)
print(cls)

print('\n*****运算符*****')
print(13//5)  # 2
print(-13//5) # -3
print(2**3)  # 8

m = 10
m **= 2
print(m)  # 100

print('\n*****逻辑运算符*****')
x = 10
y = 11
print(x > y and y < 20)  # False
print(x > y or y < 20)   # True
print(not x > y and y < 20)  # False

nums = [1,2,3,4,5]
print(2 in nums)  # True
print(7 not in nums)  # True

print(1 is 1)  # True
print(id(1) == id(1))  # True

print('\n*****if分支语句*****')
# 输入春夏秋冬  输出对应季节描述
season = input('请输入春夏秋冬中的任意一个')

if '春' in season:
    print('春天来啦')
elif '夏' in season:
    print('夏天来啦')
elif '秋' in season:
    print('秋天来啦')
elif '冬' in season:
    print('冬天来啦')
else:
    print('错误输入')

print('\n*****输入数据*****')
value = input('输入数据: ')
print(type(value))
vvv = int(value)
print(type(vvv))

valu = input('输入数据: ')
print(type(valu))
vv = float(valu)
print(type(vv))
