# 初始化
# 发送消息
# 关闭
# 广播地址255.255.255.255
import socket

def main():
    """创建UDP客户端"""
    # 初始化
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #设置广播发送
    socket_client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)

    # 发送消息
    socket_client.sendto('ditrewtreng'.encode('utf-8'), ('255.255.255.255', 8080))

    # 关闭
    socket_client.close()


main()