# 查找，是不是字母数字，开头结尾，大小写，对齐，空格，分割
# find  rfind  index  rindex
# isalpha  isdigit  isalnum isspace
# startswith  endswith
# captalize  title  upper  lower
# ljust  rjust  center
# strip  rstrip  lstrip
# split splitlines
# partition  rpartition
# replace  count join


a = 'hello world itcast and itcastcpp'

print(a.find('itcast'))
print((a.rfind('itcast')))
print(a.index('itcast'))
print(a.rindex('itcast'))

print(a.isalpha())
print(a.isdigit())
print(a.isalnum())
print(a.isspace())

print(a.startswith('h'))
print(a.endswith('pp'))

print(a.capitalize())
print(a.title())
print(a.upper())
print(a.lower())

print(a.ljust(50))
print(a.rjust(50))
print(a.center(50))

print(a.split('i'))


print(a.partition('itcast'))

print(a.count('itcast'))

print(a.replace('itcast','bbbbbb'))

b=['a','b','c']
print('='.join(b))

