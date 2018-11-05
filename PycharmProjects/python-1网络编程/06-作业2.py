# 创建一个udp服务器,循环接收udp客户端的请求,服务器如果接收到'class'
# 服务器端返回Python20,如果发送'time',返回现在的时间.如果接收到其他信息
# 那显示功能正在完善中......
import socket
import time

def send_error(socket_server, addr):

    # f发送数据
    info = '功能正在完善中.....'
    socket_server.socket_send.sendto(info.encode('utf-8'), addr)
    # 关闭
    # socket_server.close()

def send_time(socket_server, addr):

    # f发送数据
    info = time.ctime()
    socket_server.sendto(info.encode('utf-8'), addr)
    # 关闭
    # socket_server.close()

def send_class(socket_server, addr):
    # f发送数据
    info = 'python20'
    socket_server.sendto(info.encode('utf-8'), addr)
    # 关闭
    # socket_server.close()



def main():
    # 初始化socket
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定ip
    socket_server.bind(('',8084))

    while True:
        # 接收数据
        data = socket_server.recvfrom(1024)
        data_rec = data[0].decode('utf-8')
        print(data[1])
        if data_rec == 'class':
            send_class(socket_server, data[1])
        elif data_rec == 'time':
            send_time(socket_server, data[1])
        else:
            send_error(socket_server, data[1])
    # 关闭
    socket_server.close()

main()