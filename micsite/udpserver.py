#!/usr/bin/python
# -*- coding:utf8 -*-
import socket

class UdpServer(object):
    def tcpServer(self,targetHost):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('', 9527))       # 绑定同一个域名下的所有机器
        self.tcpclient(targetHost)

        sock.settimeout(0.8)
        try :
            revcData, (remoteHost, remotePort) = sock.recvfrom(1024)
        except socket.timeout:
            sock.close()
            raise socket.timeout
            return None

        print("[%s:%s] connect" % (remoteHost, remotePort))     # 接收客户端的ip, port
            
        sendDataLen = sock.sendto("this is send  data from server", (remoteHost, remotePort))
        print "revcData: ", revcData
        print "sendDataLen: ", sendDataLen
        sock.close()
        return revcData

    def tcpclient(self,targetHost):
        clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        sendDataLen = clientSock.sendto("start", (targetHost, 9528))
        #recvData = clientSock.recvfrom(1024)
        #print "sendDataLen: ", sendDataLen
        #print "recvData: ", recvData

        clientSock.close()

            
if __name__ == "__main__":
    udpServer = UdpServer()
    udpServer.tcpServer('192.168.1.157')
#    udpServer.tcpclient('192.168.1.157')
