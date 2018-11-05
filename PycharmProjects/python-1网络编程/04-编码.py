a = '我是中国人'
print(a)

encode_a = a.encode('utf-8') # 编码
print(encode_a)
print(type(encode_a))

decode_a = encode_a.decode('utf-8') # 解码，解码与编码对应
print(decode_a)

# gb_a = encode_a.decode('gb2312')
# print(gb_a)
gb_a1 = encode_a.decode('gb2312', errors='ignore') # ignore，尽量去解码
print(gb_a1)
gb_a1 = encode_a.decode('gb2312', errors='strict') # 默认strict，解码不对就报错
print(gb_a1)