import os
'''
# os.mkdir('test')
os.chdir('C:\\Users\\MyPC\\PycharmProjects\\day06\\test')
print(os.getcwd())
# f = open('test.txt','w')
# f1 = open('test1.txt','w')
# f2 = open('test2.txt','w')
# f.close()
# f1.close()
# f2.close()
#获取所有文件
file_all = os.listdir()
print(file_all)
#for批量重命名
for i in file_all:
    os.rename(i,'[cc]'+i)
'''
t_dir = input('请输入文件夹：')
#获取所有文件
file_all = os.listdir(t_dir)
# print(file_all)
#切换到目标文件夹下
print(os.getcwd())
os.chdir(t_dir)
print(os.getcwd())
#批量修改
for i in file_all:
    os.rename(i,'[ww]'+i)
