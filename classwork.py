#循环操作
# while循环

print('*****if循环*****')
count = 1
while count <= 5:
    print(count)
    count +=1

# 随机数的生成
# 1. 指定容器中获取
import random
ele = random.choice("akhgiuwaehohaohweihgoweh")
print(ele)

ele = random.choice([11,22,33,44,55])
print(ele)
# 2. 在指定区间中随机生成 区间前后闭
ele = random.randint(1,100)
print(ele)
# 3. 在【0，1）中随机生成一个小数
ele = random.random()
print(ele)
# 4. 在指定容器中，随机生成指定个数的不重复元素
ele = random.sample("kdsjeiuigaseib",3)
print(ele)

# for 遍历容器序列
for i in 'aasdfg':
    print(i)

for ele in [11,22,33]:
    print(ele)

# range---生成等差序列
'''
range(stop)
生成从0开始，步长为1，到stop结束的等差

range（start，stop，step）
   步长省略  默认为1
'''

print(list(range(10)))

v = list(range(0,10,2))
print(v)

# 数数
for i in range (1,6):
    print(i)

for odd in range(2,11,2):
    print(odd)

print('******字符串str*****')
'''
1. 字符串str

有序的序列---添加元素的顺序和显示的顺序相同
序列中每个元素都对应有自己的编号，从0开始
索引表示法
【0，长度-1】
【-长度，-1】
'''
s = '1234567890'
length = len(s)
print(length)
print(s)
# 可以通过下标获取指定位置下标
ch = s[-2]
print(ch)
ch = s[3]
print(ch)

print('******切片******')
# 切片---提取子序列
'''
序列[start：stop：step]
 ：step 可省
 默认从start下标对应的元素开始，步长为1，提取到stop
 start stop 为元素下标 可用正负数表示
 
 start 可省
     步长为正 默认左边开始
     步长为负 默认右边开始
 stop 可省
     步长为正 默认到右边结束
          负      左边
 stop 设置下标 不包含在提取之内  左闭右开
'''
sub_s = s[:] # 拷贝自身
print(sub_s)

sub_s = s[::-1] # 反转字符串
print(sub_s)

sub_s = s[:-1] # 除了最后一个其他都提取
print(sub_s)
# 提取前三个
sub_s = s[:3]
print(sub_s)
# 提取前5个并反转
sub_s = s[4::-1]
print(sub_s)

'''
1. 格式化字符串
1.1 字符串的拼接+完成两个字符串拼接
弊端 只能与字符串类型的数据进行拼接
'''
print('*****字符串拼接*****')
s1 = 'hello'
s2 = ' wolld '
new_s = s1 + s2 + str(1234)
print(new_s)

'''
1.2. f标记字符串 进行格式化
按照指定格式 输出字符串
'''
'''

print('*****字符串格式化*****')
name = input('姓名 ')
age = int(input('年龄 '))
score = float(input('成绩 '))
# :.nf 保留n为小数
# 按照n位数格式化年级排名 不足三位前面补0 :0nd
info = f'我叫{name}，今年{age}，成绩{score:.2f}, 年级排名{15:03d}'
print(info)
'''
'''
1.3 r标记字符串
\---转义符
r 让\ 保持本意
\n 换行
'''
print('*****字符串转义*****')
v = "good \night"
print(v)
v = r'good \night'
print(v)

'''
2. 切割字符串---按照指定符号 将字符切割成n段
提取每个单词---按照空格分割

'''
print('*****切割字符串*****')
seq = 'nice to meet you'
word = seq.split(' ')
print(word)

'''
列表 list
有序的可变容器
'''

print('*****列表*****')
num = [1,2,3,4,5]
lengh = len(num)
print(length)
print(num[-1]) # 获取最后一个
#切片
sub_s = num[::-1]
print(sub_s)
'''
列表长度可变  元素可变
'''
num[0] = 6
print(num)

# 追加
num.append(8)
print(num)
# 在指定位置添加
num.insert(3,0)
print(num)
# 移除指定元素
num.remove(3)
print(num)
#  移除最后一个元素
num.pop()
print(num)
# 移除指定位置元素
num.pop(1)
print(num)
#  合并其他序列  将其他序列中的元素追加到当前列表中

num.extend([11,22,33,44,55])
print(num)
#  列表生成式---快速生成一个列表

v = [1,2,3,4,5,6,7,8,9,0]
#  获取偶数数据，生成新的列表
new_v = []
#  遍历原列表
for ele in v:
    if ele % 2 ==0:
        new_v.append(ele)
print(new_v)

#  使用列表生成式 【存放元素 来源 筛选】
odd_list = [ele for ele in v if ele % 2 ==0]
print(odd_list)

w = ['nice','to','meet']
len_list = [len(ele) for ele in w]
print(len_list)
