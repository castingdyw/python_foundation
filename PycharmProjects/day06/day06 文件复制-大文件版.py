#获取文件名
scr_name = input('请输入文件名:')
index = scr_name.rfind('.')
new_name = scr_name[:index] + '-副本-' + scr_name[index:]

#打开文件
f = open(scr_name, 'r')
f1 = open(new_name, 'w')
while True:
    #读取数据
    content = f.read(1024 * 8)
    #if content == '':
    if len(content) == 0:
        break
    #写入数据
    f1.write(content)

#关闭文件
f.close()
f1.close()

