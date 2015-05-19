#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import sys, os

# 파일 오픈
print os.getcwd()
data = open("ACL_CHECK_SERVER_LIST.txt", "r")

# 서버 포트 구분자 (tuple)
separator_list = (' ', ':')

# 서버 정보 파싱
for server_info in data:
    if len(server_info) > 0:
        # 서버 포트 구분자 확인 후 파싱
        for separator in separator_list:
            if server_info.find(separator) > -1:
                server = server_info.split(separator)
                break

        host = server[0]
        ip = int(server[1])

        try:
            # 소켓 생성
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)

            # 소켓 연결 확인
            s.connect((host, ip))

            # 성공 로그
            print "Checking Host : %s:%s ==> Connection Successed" % (host, ip)

        except Exception, e:
            print "Checking Host : %s:%s ==> Connection Failed" % (host, ip)
        finally:
            s.close()

data.close()
print("Done!!")