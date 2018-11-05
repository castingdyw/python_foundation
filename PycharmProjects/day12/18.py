# 用代码创建一个text.txt文档，分别写入heimaniubi ，woaixuexi（需要换行），
# 然后把text文档里面的内容读出来，打印i出现的次数

# 新建文件，写入内容
# f = open('text.txt','w')
# f.write('heimaniubi')
# f.write('\n')
# f.write('woaixuexi')
# f.close()
# 打开文件，读取内容
f = open('text.txt','r')
content = f.read()
print(content)
cou = content.count('i')
print('i出现的次数是：%d' % cou)
f.close()