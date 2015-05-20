#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import sys, os


# ?��?�� ?��?��
print os.getcwd()
data = open("ACL_CHECK_SERVER_LIST.txt", "r")

# ?���? ?��?�� 구분?�� (tuple)
separator_list = (' ', ':')

# ?���? ?���? ?��?��
for server_info in data:
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

data.close()
print("Done!!")