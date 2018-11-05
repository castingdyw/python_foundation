# 初始化socket(套接字)
# 绑定端口
# 接收数据
# 关闭
import socket

def main():
    """创建UDP服务器"""
    # 初始化socket
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定端口
    # 传的数据是元组（host地址，port端口）
    # 一般host地址不写，表示本机的任何一个ip（127.0.0.1，局域网ip，广域网（外网））
    socket_server.bind(('',8081)) # 端口号不能与网络传输助手本地相同，与目标相同

    # 接收数据
    data = socket_server.recvfrom(1024) # 接收的数据（二进制，（'ip'，端口））
    print(data[0].decode('utf-8'))
    print(data[1])

    # 关闭
    socket_server.close()

if __name__ == '__main__':
    main()
