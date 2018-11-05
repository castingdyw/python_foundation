import socket

def send_info(udp_socket):
    try:
        info = input('信息:')
        addr = input('ip地址：')
        port = int(input('端口：'))
        # socket_send = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_socket.sendto(info.encode('utf-8'), (addr, port))
        udp_socket.close()
    except exception as e:
        print('错误')

def recv_info(udp_socket):
    # socket_send = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # udp_socket.bind(('',8084))
    data = udp_socket.recvfrom(1024)
    print(data[0].decode('utf-8'))
    print(data[1])
    udp_socket.close()


while True:
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(('',8084))
    print("=" * 30)
    print("1:发送消息")
    print("2:接收消息")
    print("3:退出")
    print("=" * 30)
    op_num = input("请输入要操作的功能序号:")
    if op_num == '1':
        send_info(udp_socket)
    elif op_num == '2':
        recv_info(udp_socket)
    elif op_num == '3':
        break
    else:
        print('输入有误，重新输入')