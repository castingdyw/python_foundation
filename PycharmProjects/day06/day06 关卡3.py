# 1. 在python用户目录下创建python06基础班文件夹
# 2. 在文件夹中创建gailun.txt文件
# 3. 打开文件在gailun.txt中写入"德玛西亚！人在塔在！"，并关闭文件
# 4. 读取文件内容，将输入的数据输出到终端上，并关闭文件
# 5. 在文件夹中创建gailun副本.txt文件
# 6. 读取gailun.txt文件中的数据，写入gailun副本.txt文件中，并关闭两个文件
# 7. 打开副本文件，查看文件中是否有内容

import os
# os.mkdir('python20')
print(os.getcwd())
os.chdir('python20')
print(os.getcwd())
#写入
# f = open('gailun.txt','w')
# f.write('德玛西亚，人在他在')
# f.close()
# #读取
# f = open('gailun.txt','r')
# content = f.read()
# print(content)
# f.close()
#创建副本
f = open('gailun.txt','r')
content = f.read()

f1 = open('gailun[fuben].txt','a')
f1.write(content)

f.close()
f1.close()