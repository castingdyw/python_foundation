# 使用列表推导式生成列表，元素为 0-10 之间的所有偶数。(结果不含10)
# a = [x for x in range(1,10) if x % 2 == 0]
# print(a)


# 把列表[11,11,22,22,33,33,44,44,55,55]转换为集合，并分析集合的特点
# a = [11,11,22,22,33,33,44,44,55,55]
# b = set(a)
# print(b)
# 没有重复，没有顺序，不能直接查看和修改

# 1. 打开test.txt文件，写入"wow,\nso beautiful!"，并关闭文件
# 2. 打开test.txt文件，使用 read() 读取文件内容。并分析 read() 的执行效果是什么。
# 3. 打开test.txt文件，使用 read(5) 读取文件内容。并分析 read(5) 的执行效果是什么。
# 4. 打开test.txt文件，使用 readlines() 读取文件内容。并分析 readlines() 的执行效果是什么。
# 5. 打开test.txt文件，使用 readline() 读取文件内容。并分析 readline() 的执行效果是什么。
# f = open('test.txt','r')
#
# # f.write('wow,\nso beautiful')
#
# # content = f.read()
# # print(content)
#
# content = f.read()
# print(repr(content))
#
# f.close()


# 1. 使用os模块创建一个名为“盖伦”的文件夹
# 2. 切换工作路径到盖伦文件夹
# 3. 获取盖伦文件夹当前所在目录
# 4. 获取当前路径的文件列表
# 5. 将盖伦文件夹删除
import os
# os.mkdir('盖伦')

# os.chdir('盖伦')

print(os.getcwd())
print(os.listdir())
os.rmdir('盖伦')

