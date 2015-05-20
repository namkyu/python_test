#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import sys, os


# check?�� ???�� ?���? 리스?�� ?��?�� 받기
print("===============================================================================")
print("please write server list")
print("and then if you finish writing server list you have to press CTRL+D !!")
print("===============================================================================")
data = sys.stdin.read()

# ?���? ?��?�� 구분?�� (tuple)
separator_list = (' ', ':')

# ?���? ?���? ?��?��
server_info_list = data.split("\n")
for server_info in server_info_list:
    if len(server_info) > 0:
        # ?���? ?��?�� 구분?�� ?��?�� ?�� ?��?��
        for separator in separator_list:
            if server_info.find(separator) > -1:
                server = server_info.split(separator)
                break

        host = server[0]
        ip = int(server[1])

        try:
            # ?���? ?��?��
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)

            # ?���? ?���? ?��?��
            s.connect((host, ip))

            # ?���? 로그
            print "Checking Host : %s:%s ==> Connection Successed" % (host, ip)

        except Exception, e:
            print "Checking Host : %s:%s ==> Connection Failed" % (host, ip)
        finally:
            s.close()

print("Done!!")