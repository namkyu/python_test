#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import sys

# check할 대상 서버 리스트 입력 받기
print("please write server list")
print("and then if you finish writing server list you have to press ctrl+d !!")
data = sys.stdin.read()

# 서버 정보 파싱
server_info_list = data.split("\n")
for server_info in server_info_list:
    if len(server_info) > 0:
        server = server_info.split(" ")
        host = server[0]
        ip = int(server[1])

        try:
            # 소켓 생성
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)

            # 소켓 연결 확인
            s.connect((host, ip))
        except Exception, e:
            print "Checking Host : %s:%s ==> connection failed" % (host, ip)
        finally:
            s.close()
print("Done!!")