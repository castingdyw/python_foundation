import socket

def send_info():
    try:
        info = input('信息:')
        addr = input('ip地址：')
        port = int(input('端口：'))
        socket_send = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        socket_send.sendto(info.encode('utf-8'), (addr, port))
        socket_send.close()
    except exception  as e:
        print('错误')

def recv_info():
    socket_send = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_send.bind(('',8084))
    data = socket_send.recvfrom(1024)
    print(data[0].decode('utf-8'))
    print(data[1])
    socket_send.close()


while True:
    print("=" * 30)
    print("1:发送消息")
    print("2:接收消息")
    print("=" * 30)
    op_num = input("请输入要操作的功能序号:")
    if op_num == '1':
        send_info()
    elif op_num == '2':
        recv_info()
    else:
        print('输入有误，重新输入')