# 初始化socket(套接字)
# 发送数据
# 关闭
import socket  # 导入包


def main():
    """创建一个udp客户端"""
    # 初始化socket
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 发送数据
    # 第一个参数是发送的数据，必须进行编码，以后都是utf-8
    # 第二个参数是ip地址和端口，元组进行包括（ip是字符串）
    socket_client.sendto('data'.encode('utf-8'), ('192.168.35.84', 8081))

    # 接收数据
    # 接收到的数据格式
    # 1024代表一次最大接收数据
    data = socket_client.recvfrom(1024)
    # 网络助手返回的信息，必须对应我的ip和端口号（变化）
    print(data[0].decode('utf-8'))
    print(data[1])

    # 关闭
    socket_client.close()

main()
